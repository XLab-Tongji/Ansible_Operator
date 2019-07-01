#!/usr/bin/expect
set timeout 10
set username [lindex $argv 0]
set password [lindex $argv 1]
set hostname [lindex $argv 2]
set port [lindex $argv 3]
spawn ssh-copy-id -f -i /root/.ssh/id_rsa.pub -p $port $username@$hostname
expect {
    #first connect, no public key in ~/.ssh/known_hosts
    "*(yes/no)?" {
        send "yes\r"
        expect "*assword:"
        send "$password\r"
        }
    #already has public key in ~/.ssh/known_hosts
    "*assword:" {
        send "$password\r"
        }
    }
expect eof
