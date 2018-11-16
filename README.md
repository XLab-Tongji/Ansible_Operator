# Ansible Operator

## Introduction

The bottleneck-toolkit based on ansible2.7 python API, using flask web api to run playbook and execute ad-hoc.

Support both ad-hoc and playbook.

##### [!] : This tool can be only running with ansidble version 2.4 and above.
To use this tool with ansible version 2.3 and below, plz refer `./old_version` 

The project dir tree:

```bash
├── LICENSE
├── README.md
├── app.py
├── old_version
│   └── flask_ansible.py
├── services
│   ├── __init__.py
│   ├── k8s_observer.py
├── static
│   └── playbook
│       ├── get_deployment.yaml
│       ├── get_namespace.yaml
│       ├── get_pod.yaml
│       └── get_svc.yaml
├── utils
│   ├── __init__.py
│   ├── ansible_runner.py
│   ├── config.py
└── view_model
    ├── __init__.py
    └── k8s_repository.py
```

## How to Use It

### Environment Requirements

- Python ~> 2.7
- Ansible ~> 2.4
- Flask ~>0.12.2

### Config and run demo

1. Install ansible with `pip install ansible`, python2(2.6 or higher) and Flask are needed
2. Config hosts at `/etc/ansible/hosts`
3. Set up SSH agent and put your public SSH key into the `authorized_keys` file located in the remote hosts
4. Run `app.py`
5. Now you can use Flask web api to control ansible 

```bash
$ curl -u lab:409 -i http://localhost:5000/tool/api/v1.0/get_namespace
```
## Interface Specifications

The specifications of interfaces used in interactions among subsystems

---
### */tool/api/v1.0/get_namespace*   

#### Description

Get existing namespaces

| | |
|-|-|
| Request Method | Get |
| Authorization | No Auth |

#### Parameters

No parameters

#### Responses

| Code | Description | Schema |
|:----:|:--------|:--|
| 200 | Successful response |  |
| 404 | Not found           | *error*: string   |

#### Request Sample

```bash
$ curl -u lab:409 -i http://localhost:5000/tool/api/v1.0/get_namespace
```

#### Response Sample

```json
{
    "failed": {},
    "skipped": {},
    "status": {},
    "success": [
        {
            "creationTimestamp": "2018-11-11T12:25:42Z",
            "name": "default",
            "uid": "e815b8e1-e5ac-11e8-88c1-0243cc3600b5"
        },
        {
            "creationTimestamp": "2018-11-11T12:25:43Z",
            "name": "kube-public",
            "uid": "e8e5e930-e5ac-11e8-88c1-0243cc3600b5"
        },
        {
            "creationTimestamp": "2018-11-11T12:25:40Z",
            "name": "kube-system",
            "uid": "e702a7f5-e5ac-11e8-88c1-0243cc3600b5"
        },
        {
            "creationTimestamp": "2018-11-11T14:05:20Z",
            "name": "sock-shop",
            "uid": "d372d697-e5ba-11e8-a684-0243cc34389c"
        }
    ],
    "unreachable": {}
}
```
---

### *tool/api/v1.0/get_svc/:name-space*  

#### Description

Get existing Services

|                |            |
| -------------- | ---------- |
| Request Method | Get        |
| Authorization  | Basic Auth |

#### Parameters

No parameters

#### Responses

| Code | Description         | Schema          |
| :--: | :------------------ | :-------------- |
| 200  | Successful response |  |
| 403  | Unauthorized access | *error*: string   |
| 404  | Not found           | *error*: string   |

#### Request Sample

```bash
$ curl -u lab:409 -i http://localhost:5000/tool/api/v1.0/get_svc/sock-shop
```

#### Response Sample

```json
{
    "failed": {},
    "skipped": {},
    "status": {},
    "success": [
        {
            "clusterIP": "10.43.8.180",
            "creationTimestamp": "2018-11-14T07:53:34Z",
            "labels": {
                "name": "carts"
            },
            "name": "carts",
            "namespace": "sock-shop"
        },
        {
            "clusterIP": "10.43.146.0",
            "creationTimestamp": "2018-11-14T07:53:29Z",
            "labels": {
                "name": "carts-db"
            },
            "name": "carts-db",
            "namespace": "sock-shop"
        },
        {
            "clusterIP": "10.43.127.203",
            "creationTimestamp": "2018-11-14T07:53:41Z",
            "labels": {
                "name": "catalogue"
            },
            "name": "catalogue",
            "namespace": "sock-shop"
        },
        {
            "clusterIP": "10.43.43.31",
            "creationTimestamp": "2018-11-14T07:53:37Z",
            "labels": {
                "name": "catalogue-db"
            },
            "name": "catalogue-db",
            "namespace": "sock-shop"
        },
        {
            "clusterIP": "10.43.220.37",
            "creationTimestamp": "2018-11-14T07:53:46Z",
            "labels": {
                "name": "front-end"
            },
            "name": "front-end",
            "namespace": "sock-shop"
        },
        {
            "clusterIP": "10.43.154.0",
            "creationTimestamp": "2018-11-14T07:54:13Z",
            "labels": {
                "name": "user-db"
            },
            "name": "user-db",
            "namespace": "sock-shop"
        }
    ],
    "unreachable": {}
}
```

------

### *tool/api/v1.0/get_deployment/:name-space*   

#### Description

Get existing Deployments

|                |            |
| -------------- | ---------- |
| Request Method | Get        |
| Authorization  | Basic Auth |

#### Parameters

No parameters

#### Responses

| Code | Description         | Schema          |
| :--: | :------------------ | :-------------- |
| 200  | Successful response |  |
| 403  | Unauthorized access | *error*: string   |
| 404  | Not found           | *error*: string   |

#### Request Sample

```bash
$ curl -u lab:409 -i http://localhost:5000/tool/api/v1.0/get_deployment/sock-shop
```

#### Response Sample

```json
{
    "failed": {},
    "skipped": {},
    "status": {},
    "success": [
        {
            "container_spec": [
                {
                    "env": [
                        {
                            "name": "ZIPKIN",
                            "value": "zipkin.jaeger.svc.cluster.local"
                        },
                        {
                            "name": "JAVA_OPTS",
                            "value": "-Xms64m -Xmx128m -XX:PermSize=32m -XX:MaxPermSize=64m -XX:+UseG1GC -Djava.security.egd=file:/dev/urandom"
                        }
                    ],
                    "image": "weaveworksdemos/shipping:0.4.8",
                    "imagePullPolicy": "IfNotPresent",
                    "name": "shipping",
                    "ports": [
                        {
                            "containerPort": 80,
                            "protocol": "TCP"
                        }
                    ],
                    "resources": {},
                    "securityContext": {
                        "capabilities": {
                            "add": [
                                "NET_BIND_SERVICE"
                            ],
                            "drop": [
                                "all"
                            ]
                        },
                        "readOnlyRootFilesystem": true,
                        "runAsNonRoot": true,
                        "runAsUser": 10001
                    },
                    "terminationMessagePath": "/dev/termination-log",
                    "terminationMessagePolicy": "File",
                    "volumeMounts": [
                        {
                            "mountPath": "/tmp",
                            "name": "tmp-volume"
                        }
                    ]
                }
            ],
            "creationTimestamp": "2018-11-14T07:54:06Z",
            "labels": {
                "name": "shipping"
            },
            "name": "shipping",
            "namespace": "sock-shop"
        },
        {
            "container_spec": [
                {
                    "env": [
                        {
                            "name": "MONGO_HOST",
                            "value": "user-db:27017"
                        }
                    ],
                    "image": "weaveworksdemos/user:0.4.7",
                    "imagePullPolicy": "IfNotPresent",
                    "name": "user",
                    "ports": [
                        {
                            "containerPort": 80,
                            "protocol": "TCP"
                        }
                    ],
                    "resources": {},
                    "securityContext": {
                        "capabilities": {
                            "add": [
                                "NET_BIND_SERVICE"
                            ],
                            "drop": [
                                "all"
                            ]
                        },
                        "readOnlyRootFilesystem": true,
                        "runAsNonRoot": true,
                        "runAsUser": 10001
                    },
                    "terminationMessagePath": "/dev/termination-log",
                    "terminationMessagePolicy": "File"
                }
            ],
            "creationTimestamp": "2018-11-14T07:54:19Z",
            "labels": {
                "name": "user"
            },
            "name": "user",
            "namespace": "sock-shop"
        },
        {
            "container_spec": [
                {
                    "image": "weaveworksdemos/user-db:0.4.0",
                    "imagePullPolicy": "IfNotPresent",
                    "name": "user-db",
                    "ports": [
                        {
                            "containerPort": 27017,
                            "name": "mongo",
                            "protocol": "TCP"
                        }
                    ],
                    "resources": {},
                    "securityContext": {
                        "capabilities": {
                            "add": [
                                "CHOWN",
                                "SETGID",
                                "SETUID"
                            ],
                            "drop": [
                                "all"
                            ]
                        },
                        "readOnlyRootFilesystem": true
                    },
                    "terminationMessagePath": "/dev/termination-log",
                    "terminationMessagePolicy": "File",
                    "volumeMounts": [
                        {
                            "mountPath": "/tmp",
                            "name": "tmp-volume"
                        }
                    ]
                }
            ],
            "creationTimestamp": "2018-11-14T07:54:11Z",
            "labels": {
                "name": "user-db"
            },
            "name": "user-db",
            "namespace": "sock-shop"
        }
    ],
    "unreachable": {}
}
```

------

### *tool/api/v1.0/get_pods/:name-space*   

#### Description

Get existing Pods

|                |            |
| -------------- | ---------- |
| Request Method | Get        |
| Authorization  | Basic Auth |

#### Parameters

No parameters

#### Responses

| Code | Description         | Schema          |
| :--: | :------------------ | :-------------- |
| 200  | Successful response | *name* : string |
| 403  | Unauthorized access | **error**: string   |
| 404  | Not found           | *error*: string   |

#### Request Sample

```bash
$ curl -u lab:409 -i http://localhost:5000/tool/api/v1.0/get_pods/sock-shop
```

#### Response Sample

```json
{
    "failed": {},
    "skipped": {},
    "status": {},
    "success": [
        {
            "creationTimestamp": "2018-11-14T07:53:54Z",
            "hostIP": "192.168.199.22",
            "labels": {
                "name": "payment",
                "pod-template-hash": "2302149242"
            },
            "name": "payment-674658f686-htmlh",
            "namespace": "sock-shop",
            "nodeName": "k8s-node-2",
            "podIP": "10.42.55.34"
        },
        {
            "creationTimestamp": "2018-11-14T07:53:59Z",
            "hostIP": "192.168.199.22",
            "labels": {
                "name": "queue-master",
                "pod-template-hash": "195466823"
            },
            "name": "queue-master-5f98bbd67-d5fdw",
            "namespace": "sock-shop",
            "nodeName": "k8s-node-2",
            "podIP": "10.42.244.95"
        },
        {
            "creationTimestamp": "2018-11-14T07:54:01Z",
            "hostIP": "192.168.199.22",
            "labels": {
                "name": "rabbitmq",
                "pod-template-hash": "4280088402"
            },
            "name": "rabbitmq-86d44dd846-mcz48",
            "namespace": "sock-shop",
            "nodeName": "k8s-node-2",
            "podIP": "10.42.216.132"
        },
        {
            "creationTimestamp": "2018-11-14T07:54:07Z",
            "hostIP": "192.168.199.21",
            "labels": {
                "name": "shipping",
                "pod-template-hash": "3534296512"
            },
            "name": "shipping-79786fb956-cb2nn",
            "namespace": "sock-shop",
            "nodeName": "k8s-node-1",
            "podIP": "10.42.105.141"
        },
        {
            "creationTimestamp": "2018-11-14T07:54:20Z",
            "hostIP": "192.168.199.22",
            "labels": {
                "name": "user",
                "pod-template-hash": "2551540103"
            },
            "name": "user-6995984547-t5f6m",
            "namespace": "sock-shop",
            "nodeName": "k8s-node-2",
            "podIP": "10.42.182.250"
        },
        {
            "creationTimestamp": "2018-11-14T07:54:24Z",
            "hostIP": "192.168.199.23",
            "labels": {
                "name": "user",
                "pod-template-hash": "2551540103"
            },
            "name": "user-6995984547-v6zzb",
            "namespace": "sock-shop",
            "nodeName": "k8s-node-3",
            "podIP": "10.42.133.32"
        },
        {
            "creationTimestamp": "2018-11-14T07:54:24Z",
            "hostIP": "192.168.199.21",
            "labels": {
                "name": "user",
                "pod-template-hash": "2551540103"
            },
            "name": "user-6995984547-wjhtk",
            "namespace": "sock-shop",
            "nodeName": "k8s-node-1",
            "podIP": "10.42.241.172"
        },
        {
            "creationTimestamp": "2018-11-14T07:54:12Z",
            "hostIP": "192.168.199.23",
            "labels": {
                "name": "user-db",
                "pod-template-hash": "973603965"
            },
            "name": "user-db-fc7b47fb9-nv8sn",
            "namespace": "sock-shop",
            "nodeName": "k8s-node-3",
            "podIP": "10.42.206.46"
        }
    ],
    "unreachable": {}
}
```

------




