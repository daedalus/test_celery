#!/bin/bash
set -x

USER=rb_user
PASSWD=rb_passwd
VHOST=rb_vhost
TAG=rb_user_tag

sudo pip3 install flower
sudo pip3 install celery

sudo apt-get install rabbitmq-server -y

rabbitmqctl add_user $USER $PASSWD
rabbitmqctl add_vhost $VHOST
rabbitmqctl set_user_tags $USER $TAG
rabbitmqctl set_permissions -p $VHOST $USER ".*" ".*" ".*"
