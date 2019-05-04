#!/bin/bash
source $1
awk -F":" '{if($1 == "Root") print "User Root Found"}' /etc/passwd
#if [ $? = 0 ] ;then
#  echo "$username user exists"
#else
#  echo "$username user not found"
#fi
