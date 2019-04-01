FROM ansible/ansible:ubuntu1604


RUN sudo apt-get update \
    && apt-get install -y --no-install-recommends --fix-missing tcl tk expect \
    && git clone https://github.com/XLab-Tongji/Ansible_Operator.git ~/Ansible_Operator \
    && chmod 777 ~/Ansible_Operator/auto_ssh.sh \
    && rm /etc/ansible/hosts \
    && cp ~/Ansible_Operator/hosts /etc/ansible/ \
    && pip install --upgrade pip \
    && pip2 install ansible \
    && pip2 install flask \
    && pip2 install flask_httpauth \
    && pip2 install requests \
    && git -C /root/Ansible_Operator pull \
    && /usr/bin/expect /root/Ansible_Operator/auto_ssh.sh root 123456 10.60.38.181 2331\
    && chmod 777 ~/Ansible_Operator/run.sh


CMD ["sh", "/root/Ansible_Operator/run.sh"]





