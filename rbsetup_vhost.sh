#!/bin/bash
set -x

USER=rb_user
PASSWD=rb_passwd
VHOST=rb_vhost
TAG=rb_user_tag

apt-get install rabbitmq-server

rabbitmqctl add_user $USER $PASSWD
rabbitmqctl add_vhost $VHOST
rabbitmqctl set_user_tags $USER $TAG
rabbitmqctl set_permissions -p $VHOST $USER ".*" ".*" ".*"
