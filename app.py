# -*- coding: utf-8 -*

from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask_httpauth import HTTPBasicAuth

from services.k8s_observer import K8sObserver
from utils.config import config

auth = HTTPBasicAuth()
app = Flask(__name__)


@auth.get_password
def get_password(username):
    if username == config['user_name']:
        return config['password']
    return None


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)


@app.errorhandler(404)
@auth.login_required
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/tool/api/v1.0/get_namespace', methods=['GET'])
@auth.login_required
def get_namespace():
    return jsonify(K8sObserver.get_namespace())


@app.route('/tool/api/v1.0/get_svc/<namespace>', methods=['GET'])
@auth.login_required
def get_svc(namespace):
    return jsonify(K8sObserver.get_svc(namespace=namespace.encode('raw_unicode_escape')))


@app.route('/tool/api/v1.0/get_deployment/<namespace>', methods=['GET'])
@auth.login_required
def get_deployment(namespace):
    return jsonify(K8sObserver.get_deployment(namespace=namespace.encode('raw_unicode_escape')))


@app.route('/tool/api/v1.0/get_pods/<namespace>', methods=['GET'])
@auth.login_required
def get_pods(namespace):
    return jsonify(K8sObserver.get_pods(namespace))

# ================
#
# @app.route('/todo/api/v1.0/tasks', methods=['GET'])
# @auth.login_required
# def get_tasks():
#     return jsonify({'tasks': tasks})
#
#
# @app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
# def get_task(task_id):
#     task = filter(lambda t: t['id'] == task_id, tasks)
#     if len(task) == 0:
#         abort(404)
#     return jsonify({'task': task[0]})
#
#
# @app.route('/todo/api/v1.0/tasks', methods=['POST'])
# def create_task():
#     if not request.json or not 'title' in request.json:
#         abort(400)
#     task = {
#         'id': tasks[-1]['id'] + 1,
#         'title': request.json['title'],
#         'description': request.json.get('description', ""),
#         'done': False
#     }
#     tasks.append(task)
#     return jsonify({'task': task}), 201
#


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
