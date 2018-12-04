FROM ansible/ansible:ubuntu1404


RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list \
    && apt-get clean \
    && echo "deb http://archive.ubuntu.com/ubuntu trusty main universe restricted multiverse" > /etc/apt/sources.list \
    && sudo apt-get update \
    && apt-get install -y --no-install-recommends tcl tk expect \
    && rm -rf /var/lib/apt/lists/* \
    && git clone https://github.com/Moonlor/AnsibleOperator.git ~/Ansible_Operator \
    && chmod 777 ~/Ansible_Operator/auto_ssh.sh \
    && rm /etc/ansible/hosts \
    && cp ~/Ansible_Operator/hosts /etc/ansible/ \
    && pip install --upgrade pip \
    && pip install ansible \
    && pip install flask \
    && pip install flask_httpauth





