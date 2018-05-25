import os
import subprocess
import tempfile
from flask import Flask, jsonify, make_response, request
from flask_httpauth import HTTPBasicAuth


app = Flask(__name__)
auth = HTTPBasicAuth()


# this is only a demo, ideally we should not store plain text passwords
# and they should rather be in a database or file
@auth.get_password
def get_password(username):
    if username == 'someuser':
        return '123456'
    if username == 'otheruser':
        return '112233'
    return None


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/api/v1.0/calculation/start/', methods=['POST'])
@auth.login_required
def start_calculation():
    _, model_file = tempfile.mkstemp()
    with open(model_file, 'w') as f:
        model = request.json['model']
        f.write(str(model))
    _, parameter_file = tempfile.mkstemp()
    with open(parameter_file, 'w') as f:
        parameters = request.json['parameters']
        f.write(str(parameters))
    _here = os.path.dirname(os.path.realpath(__file__))
    script = os.path.join(_here, 'start-calculation.sh')
    output = subprocess.check_output(['bash', script, model_file, parameter_file])
    os.remove(model_file)
    os.remove(parameter_file)
    return jsonify({'result': str(output)})


# this is too simple, we should check that
#   1) the calculation actually exists
#   2) the calculation belongs to the user
@app.route('/api/v1.0/calculation/<int:calculation_id>/', methods=['GET'])
@auth.login_required
def info_calculation(calculation_id):
    _here = os.path.dirname(os.path.realpath(__file__))
    script = os.path.join(_here, 'info-calculation.sh')
    output = subprocess.check_output(['bash', script, str(calculation_id)])
    return jsonify({'result': str(output)})


# this is too simple, we should check that
#   1) the calculation actually exists and is running
#   2) the calculation belongs to the user
@app.route('/api/v1.0/calculation/<int:calculation_id>/', methods=['POST'])
@auth.login_required
def modify_calculation(calculation_id):
    _, parameter_file = tempfile.mkstemp()
    with open(parameter_file, 'w') as f:
        parameters = request.json['parameters']
        f.write(str(parameters))
    _here = os.path.dirname(os.path.realpath(__file__))
    script = os.path.join(_here, 'modify-calculation.sh')
    output = subprocess.check_output(['bash', script, str(calculation_id), parameter_file])
    os.remove(parameter_file)
    return jsonify({'result': str(output)})


# this is too simple, we should check that
#   1) the calculation actually exists and is running
#   2) the calculation belongs to the user
@app.route('/api/v1.0/calculation/<int:calculation_id>/', methods=['DELETE'])
@auth.login_required
def delete_calculation(calculation_id):
    _here = os.path.dirname(os.path.realpath(__file__))
    script = os.path.join(_here, 'delete-calculation.sh')
    output = subprocess.check_output(['bash', script, str(calculation_id)])
    return jsonify({'result': str(output)})
