# bottleneck-toolkit2
The bottleneck-toolkit based on ansible2.7 python API, using flask web api to run playbook and execute ad-hoc

Support both ad-hoc and playbook

> ##### [!] : This tool kit can be only running with ansidble version 2.4 and above
> To use this toolkit with ansible version 2.3 and below, plz view `./old_version` 

---

The project dir tree:

```bash
.
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
│       ├── get_pod.yaml
│       └── get_svc.yaml
└── utils
    ├── __init__.py
    ├── ansible_runner.py
    ├── config.py

```

How to:
1. Install ansible with `pip install ansible`, python2(2.6 or higher) and Flask are needed

2. Config hosts at `/etc/ansible/hosts`

3. Set up SSH agent and put your public SSH key into the `authorized_keys` file located in the remote hosts

4. Run `app.py`

5. Now you can use Flask web api to control ansible 

---

#### demo: run a playbook to fetch a list of all k8s service objects

try: 

```bash
$ curl -u lab:409 -i http://localhost:5000/tool/api/v1.0/get_svc
```

get:

```json
{
    "failed": {},
    "skipped": {},
    "status": {},
    "success": {
        "10.60.38.181": {
            "_ansible_no_log": false,
            "_ansible_parsed": true,
            "changed": false,
            "invocation": {
                "module_args": {
                    "api_key": null,
                    "api_version": "v1",
                    "cert_file": null,
                    "context": null,
                    "field_selectors": [],
                    "host": null,
                    "key_file": null,
                    "kind": "Service",
                    "kubeconfig": null,
                    "label_selectors": [],
                    "name": null,
                    "namespace": "sock-shop",
                    "password": null,
                    "ssl_ca_cert": null,
                    "username": null,
                    "verify_ssl": null
                }
            },
            "resources": [
                {
                    "metadata": {
                        "annotations": {
                            "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Service\",\"metadata\":{\"annotations\":{},\"labels\":{\"name\":\"carts\"},\"name\":\"carts\",\"namespace\":\"sock-shop\"},\"spec\":{\"ports\":[{\"port\":80,\"targetPort\":80}],\"selector\":{\"name\":\"carts\"}}}\n"
                        },
                        "creationTimestamp": "2018-11-12T05:58:53Z",
                        "labels": {
                            "name": "carts"
                        },
                        "name": "carts",
                        "namespace": "sock-shop",
                        "resourceVersion": "78686",
                        "selfLink": "/api/v1/namespaces/sock-shop/services/carts",
                        "uid": "08d0cc3b-e640-11e8-a684-0243cc34389c"
                    },
                    "spec": {
                        "clusterIP": "10.43.148.196",
                        "ports": [
                            {
                                "port": 80,
                                "protocol": "TCP",
                                "targetPort": 80
                            }
                        ],
                        "selector": {
                            "name": "carts"
                        },
                        "sessionAffinity": "None",
                        "type": "ClusterIP"
                    },
                    "status": {
                        "loadBalancer": {}
                    }
                },
                {
                    "metadata": {
                        "annotations": {
                            "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Service\",\"metadata\":{\"annotations\":{},\"labels\":{\"name\":\"carts-db\"},\"name\":\"carts-db\",\"namespace\":\"sock-shop\"},\"spec\":{\"ports\":[{\"port\":27017,\"targetPort\":27017}],\"selector\":{\"name\":\"carts-db\"}}}\n"
                        },
                        "creationTimestamp": "2018-11-12T05:58:50Z",
                        "labels": {
                            "name": "carts-db"
                        },
                        "name": "carts-db",
                        "namespace": "sock-shop",
                        "resourceVersion": "78662",
                        "selfLink": "/api/v1/namespaces/sock-shop/services/carts-db",
                        "uid": "071c2799-e640-11e8-a684-0243cc34389c"
                    },
                    "spec": {
                        "clusterIP": "10.43.146.229",
                        "ports": [
                            {
                                "port": 27017,
                                "protocol": "TCP",
                                "targetPort": 27017
                            }
                        ],
                        "selector": {
                            "name": "carts-db"
                        },
                        "sessionAffinity": "None",
                        "type": "ClusterIP"
                    },
                    "status": {
                        "loadBalancer": {}
                    }
                },
                {
                    "metadata": {
                        "annotations": {
                            "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Service\",\"metadata\":{\"annotations\":{},\"labels\":{\"name\":\"catalogue\"},\"name\":\"catalogue\",\"namespace\":\"sock-shop\"},\"spec\":{\"ports\":[{\"port\":80,\"targetPort\":80}],\"selector\":{\"name\":\"catalogue\"}}}\n"
                        },
                        "creationTimestamp": "2018-11-12T05:58:57Z",
                        "labels": {
                            "name": "catalogue"
                        },
                        "name": "catalogue",
                        "namespace": "sock-shop",
                        "resourceVersion": "78724",
                        "selfLink": "/api/v1/namespaces/sock-shop/services/catalogue",
                        "uid": "0b3cdc3a-e640-11e8-a684-0243cc34389c"
                    },
                    "spec": {
                        "clusterIP": "10.43.55.18",
                        "ports": [
                            {
                                "port": 80,
                                "protocol": "TCP",
                                "targetPort": 80
                            }
                        ],
                        "selector": {
                            "name": "catalogue"
                        },
                        "sessionAffinity": "None",
                        "type": "ClusterIP"
                    },
                    "status": {
                        "loadBalancer": {}
                    }
                },
                {
                    "metadata": {
                        "annotations": {
                            "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Service\",\"metadata\":{\"annotations\":{},\"labels\":{\"name\":\"catalogue-db\"},\"name\":\"catalogue-db\",\"namespace\":\"sock-shop\"},\"spec\":{\"ports\":[{\"port\":3306,\"targetPort\":3306}],\"selector\":{\"name\":\"catalogue-db\"}}}\n"
                        },
                        "creationTimestamp": "2018-11-12T05:58:55Z",
                        "labels": {
                            "name": "catalogue-db"
                        },
                        "name": "catalogue-db",
                        "namespace": "sock-shop",
                        "resourceVersion": "78705",
                        "selfLink": "/api/v1/namespaces/sock-shop/services/catalogue-db",
                        "uid": "09bb8dd0-e640-11e8-a684-0243cc34389c"
                    },
                    "spec": {
                        "clusterIP": "10.43.22.36",
                        "ports": [
                            {
                                "port": 3306,
                                "protocol": "TCP",
                                "targetPort": 3306
                            }
                        ],
                        "selector": {
                            "name": "catalogue-db"
                        },
                        "sessionAffinity": "None",
                        "type": "ClusterIP"
                    },
                    "status": {
                        "loadBalancer": {}
                    }
                },
                {
                    "metadata": {
                        "annotations": {
                            "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Service\",\"metadata\":{\"annotations\":{},\"labels\":{\"name\":\"front-end\"},\"name\":\"front-end\",\"namespace\":\"sock-shop\"},\"spec\":{\"ports\":[{\"nodePort\":30001,\"port\":8081,\"targetPort\":8079}],\"selector\":{\"name\":\"front-end\"},\"type\":\"NodePort\"}}\n"
                        },
                        "creationTimestamp": "2018-11-12T05:59:00Z",
                        "labels": {
                            "name": "front-end"
                        },
                        "name": "front-end",
                        "namespace": "sock-shop",
                        "resourceVersion": "78747",
                        "selfLink": "/api/v1/namespaces/sock-shop/services/front-end",
                        "uid": "0d26b394-e640-11e8-a684-0243cc34389c"
                    },
                    "spec": {
                        "clusterIP": "10.43.155.138",
                        "externalTrafficPolicy": "Cluster",
                        "ports": [
                            {
                                "nodePort": 30001,
                                "port": 8081,
                                "protocol": "TCP",
                                "targetPort": 8079
                            }
                        ],
                        "selector": {
                            "name": "front-end"
                        },
                        "sessionAffinity": "None",
                        "type": "NodePort"
                    },
                    "status": {
                        "loadBalancer": {}
                    }
                },
                {
                    "metadata": {
                        "annotations": {
                            "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Service\",\"metadata\":{\"annotations\":{},\"labels\":{\"name\":\"orders\"},\"name\":\"orders\",\"namespace\":\"sock-shop\"},\"spec\":{\"ports\":[{\"port\":80,\"targetPort\":80}],\"selector\":{\"name\":\"orders\"}}}\n"
                        },
                        "creationTimestamp": "2018-11-12T05:59:05Z",
                        "labels": {
                            "name": "orders"
                        },
                        "name": "orders",
                        "namespace": "sock-shop",
                        "resourceVersion": "78781",
                        "selfLink": "/api/v1/namespaces/sock-shop/services/orders",
                        "uid": "0fae15bc-e640-11e8-a684-0243cc34389c"
                    },
                    "spec": {
                        "clusterIP": "10.43.43.32",
                        "ports": [
                            {
                                "port": 80,
                                "protocol": "TCP",
                                "targetPort": 80
                            }
                        ],
                        "selector": {
                            "name": "orders"
                        },
                        "sessionAffinity": "None",
                        "type": "ClusterIP"
                    },
                    "status": {
                        "loadBalancer": {}
                    }
                },
                {
                    "metadata": {
                        "annotations": {
                            "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Service\",\"metadata\":{\"annotations\":{},\"labels\":{\"name\":\"orders-db\"},\"name\":\"orders-db\",\"namespace\":\"sock-shop\"},\"spec\":{\"ports\":[{\"port\":27017,\"targetPort\":27017}],\"selector\":{\"name\":\"orders-db\"}}}\n"
                        },
                        "creationTimestamp": "2018-11-12T05:59:02Z",
                        "labels": {
                            "name": "orders-db"
                        },
                        "name": "orders-db",
                        "namespace": "sock-shop",
                        "resourceVersion": "78764",
                        "selfLink": "/api/v1/namespaces/sock-shop/services/orders-db",
                        "uid": "0e3264b0-e640-11e8-a684-0243cc34389c"
                    },
                    "spec": {
                        "clusterIP": "10.43.139.206",
                        "ports": [
                            {
                                "port": 27017,
                                "protocol": "TCP",
                                "targetPort": 27017
                            }
                        ],
                        "selector": {
                            "name": "orders-db"
                        },
                        "sessionAffinity": "None",
                        "type": "ClusterIP"
                    },
                    "status": {
                        "loadBalancer": {}
                    }
                },
                {
                    "metadata": {
                        "annotations": {
                            "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Service\",\"metadata\":{\"annotations\":{},\"labels\":{\"name\":\"payment\"},\"name\":\"payment\",\"namespace\":\"sock-shop\"},\"spec\":{\"ports\":[{\"port\":80,\"targetPort\":80}],\"selector\":{\"name\":\"payment\"}}}\n"
                        },
                        "creationTimestamp": "2018-11-12T05:59:07Z",
                        "labels": {
                            "name": "payment"
                        },
                        "name": "payment",
                        "namespace": "sock-shop",
                        "resourceVersion": "78804",
                        "selfLink": "/api/v1/namespaces/sock-shop/services/payment",
                        "uid": "1123bab1-e640-11e8-a684-0243cc34389c"
                    },
                    "spec": {
                        "clusterIP": "10.43.60.81",
                        "ports": [
                            {
                                "port": 80,
                                "protocol": "TCP",
                                "targetPort": 80
                            }
                        ],
                        "selector": {
                            "name": "payment"
                        },
                        "sessionAffinity": "None",
                        "type": "ClusterIP"
                    },
                    "status": {
                        "loadBalancer": {}
                    }
                },
                {
                    "metadata": {
                        "annotations": {
                            "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Service\",\"metadata\":{\"annotations\":{\"prometheus.io/path\":\"/prometheus\"},\"labels\":{\"name\":\"queue-master\"},\"name\":\"queue-master\",\"namespace\":\"sock-shop\"},\"spec\":{\"ports\":[{\"port\":80,\"targetPort\":80}],\"selector\":{\"name\":\"queue-master\"}}}\n",
                            "prometheus.io/path": "/prometheus"
                        },
                        "creationTimestamp": "2018-11-12T05:59:10Z",
                        "labels": {
                            "name": "queue-master"
                        },
                        "name": "queue-master",
                        "namespace": "sock-shop",
                        "resourceVersion": "78825",
                        "selfLink": "/api/v1/namespaces/sock-shop/services/queue-master",
                        "uid": "13150714-e640-11e8-a684-0243cc34389c"
                    },
                    "spec": {
                        "clusterIP": "10.43.234.255",
                        "ports": [
                            {
                                "port": 80,
                                "protocol": "TCP",
                                "targetPort": 80
                            }
                        ],
                        "selector": {
                            "name": "queue-master"
                        },
                        "sessionAffinity": "None",
                        "type": "ClusterIP"
                    },
                    "status": {
                        "loadBalancer": {}
                    }
                },
                {
                    "metadata": {
                        "annotations": {
                            "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Service\",\"metadata\":{\"annotations\":{},\"labels\":{\"name\":\"rabbitmq\"},\"name\":\"rabbitmq\",\"namespace\":\"sock-shop\"},\"spec\":{\"ports\":[{\"port\":5672,\"targetPort\":5672}],\"selector\":{\"name\":\"rabbitmq\"}}}\n"
                        },
                        "creationTimestamp": "2018-11-12T05:59:13Z",
                        "labels": {
                            "name": "rabbitmq"
                        },
                        "name": "rabbitmq",
                        "namespace": "sock-shop",
                        "resourceVersion": "78842",
                        "selfLink": "/api/v1/namespaces/sock-shop/services/rabbitmq",
                        "uid": "1483a440-e640-11e8-a684-0243cc34389c"
                    },
                    "spec": {
                        "clusterIP": "10.43.12.33",
                        "ports": [
                            {
                                "port": 5672,
                                "protocol": "TCP",
                                "targetPort": 5672
                            }
                        ],
                        "selector": {
                            "name": "rabbitmq"
                        },
                        "sessionAffinity": "None",
                        "type": "ClusterIP"
                    },
                    "status": {
                        "loadBalancer": {}
                    }
                },
                {
                    "metadata": {
                        "annotations": {
                            "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Service\",\"metadata\":{\"annotations\":{},\"labels\":{\"name\":\"shipping\"},\"name\":\"shipping\",\"namespace\":\"sock-shop\"},\"spec\":{\"ports\":[{\"port\":80,\"targetPort\":80}],\"selector\":{\"name\":\"shipping\"}}}\n"
                        },
                        "creationTimestamp": "2018-11-12T05:59:15Z",
                        "labels": {
                            "name": "shipping"
                        },
                        "name": "shipping",
                        "namespace": "sock-shop",
                        "resourceVersion": "78857",
                        "selfLink": "/api/v1/namespaces/sock-shop/services/shipping",
                        "uid": "161e61fd-e640-11e8-a684-0243cc34389c"
                    },
                    "spec": {
                        "clusterIP": "10.43.107.50",
                        "ports": [
                            {
                                "port": 80,
                                "protocol": "TCP",
                                "targetPort": 80
                            }
                        ],
                        "selector": {
                            "name": "shipping"
                        },
                        "sessionAffinity": "None",
                        "type": "ClusterIP"
                    },
                    "status": {
                        "loadBalancer": {}
                    }
                },
                {
                    "metadata": {
                        "annotations": {
                            "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Service\",\"metadata\":{\"annotations\":{},\"labels\":{\"name\":\"user\"},\"name\":\"user\",\"namespace\":\"sock-shop\"},\"spec\":{\"ports\":[{\"port\":80,\"targetPort\":80}],\"selector\":{\"name\":\"user\"}}}\n"
                        },
                        "creationTimestamp": "2018-11-12T05:59:20Z",
                        "labels": {
                            "name": "user"
                        },
                        "name": "user",
                        "namespace": "sock-shop",
                        "resourceVersion": "78898",
                        "selfLink": "/api/v1/namespaces/sock-shop/services/user",
                        "uid": "18c6c9ae-e640-11e8-a684-0243cc34389c"
                    },
                    "spec": {
                        "clusterIP": "10.43.204.173",
                        "ports": [
                            {
                                "port": 80,
                                "protocol": "TCP",
                                "targetPort": 80
                            }
                        ],
                        "selector": {
                            "name": "user"
                        },
                        "sessionAffinity": "None",
                        "type": "ClusterIP"
                    },
                    "status": {
                        "loadBalancer": {}
                    }
                },
                {
                    "metadata": {
                        "annotations": {
                            "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Service\",\"metadata\":{\"annotations\":{},\"labels\":{\"name\":\"user-db\"},\"name\":\"user-db\",\"namespace\":\"sock-shop\"},\"spec\":{\"ports\":[{\"port\":27017,\"targetPort\":27017}],\"selector\":{\"name\":\"user-db\"}}}\n"
                        },
                        "creationTimestamp": "2018-11-12T05:59:18Z",
                        "labels": {
                            "name": "user-db"
                        },
                        "name": "user-db",
                        "namespace": "sock-shop",
                        "resourceVersion": "78887",
                        "selfLink": "/api/v1/namespaces/sock-shop/services/user-db",
                        "uid": "17ffe92a-e640-11e8-a684-0243cc34389c"
                    },
                    "spec": {
                        "clusterIP": "10.43.139.82",
                        "ports": [
                            {
                                "port": 27017,
                                "protocol": "TCP",
                                "targetPort": 27017
                            }
                        ],
                        "selector": {
                            "name": "user-db"
                        },
                        "sessionAffinity": "None",
                        "type": "ClusterIP"
                    },
                    "status": {
                        "loadBalancer": {}
                    }
                }
            ]
        }
    },
    "unreachable": {}
}
```







