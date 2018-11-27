FROM ansible/ansible:ubuntu1404

RUN rm /var/lib/apt/lists/* -vf \
    && apt-get update -y \
    && apt-get install -y tcl tk expect \
    && git clone https://github.com/XLab-Tongji/Anisible_Operator.git \
    && chmod 777 ~/Anisible_Operator/auto_ssh.sh \
    && rm /etc/ansible/hosts \
    && cp ~/Anisible_Operator/hosts /etc/ansible/ \
    && pip install ansible \
    && pip install flask \
    && pip install flask_httpauth





