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
| 200 | Successful response | *name* : string |
| 403 | Unauthorized access | error: string |
| 404 | Not found | error: string |

#### Request Sample (示例请求)

```bash
$ curl -u lab:409 -i http://localhost:5000/tool/api/v1.0/get_namespace
```

#### Response Sample (示例结果)

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

### *tool/api/v1.0/get_svc/<name-space>*   

#### Description

Get existing namespaces

|                |         |
| -------------- | ------- |
| Request Method | Get     |
| Authorization  | No Auth |

#### Parameters

No parameters

#### Responses

| Code | Description         | Schema          |
| :--: | :------------------ | :-------------- |
| 200  | Successful response | *name* : string |
| 403  | Unauthorized access | error: string   |
| 404  | Not found           | error: string   |

#### Request Sample (示例请求)

```bash
$ curl -u lab:409 -i http://localhost:5000/tool/api/v1.0/get_namespace
```

#### Response Sample (示例结果)

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

------




