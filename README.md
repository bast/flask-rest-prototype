
[![License](https://img.shields.io/badge/license-%20MPL--v2.0-blue.svg)](LICENSE)


# REST API prototype

Built following https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask.


## How to test it out

First install dependencies into a virtual environment.

In one terminal start the server:

```
$ cd server
$ env FLASK_APP=server.py flask run

* Serving Flask app "server.py"
* Environment: production
  WARNING: Do not use the development server in a production environment.
  Use a production WSGI server instead.
* Debug mode: off
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

In another terminal test the client:

```
$ cd client
$ python example.py

testing: starting a calculation
{'result': "b'starting calculation\\nreading model from file /tmp/tmpne3ts8ge\\nreading parameters from file /tmp/tmpw3ux89_n\\n'"}
testing: getting info about a calculation
{'result': "b'information about calculation 137 ...\\n'"}
testing: modifying a calculation
{'result': "b'modifying calculation 137\\nreading parameters from file /tmp/tmprkefyzip\\n'"}
testing: deleting a calculation
{'result': "b'deleting calculation 137\\n'"}
```
