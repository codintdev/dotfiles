#!/bin/sh

if [ "$(/usr/sbin/ifconfig eth0 | grep 'inet ' | awk 'NF{print $2}')" != "" ] && [ "$(/usr/sbin/ifconfig wlan0 | grep 'inet ' | awk 'NF{print $2}')" != "" ]; then
  echo "%{F#2495e7} %{F#ffffff}$(/usr/sbin/ifconfig eth0 | grep 'inet ' | awk '{print $2}')%{u-}"
elif [ "$(/usr/sbin/ifconfig eth0 | grep 'inet ' | awk 'NF{print $2}')" != "" ] && [ "$(/usr/sbin/ifconfig wlan0 | grep 'inet ' | awk 'NF{print $2}')" = "" ]; then
  echo "%{F#2495e7} %{F#ffffff}$(/usr/sbin/ifconfig eth0 | grep 'inet ' | awk '{print $2}')%{u-}"
elif [ "$(/usr/sbin/ifconfig wlan0 | grep 'inet ' | awk 'NF{print $2}')" != "" ] && [ "$(/usr/sbin/ifconfig eth0 | grep 'inet ' | awk 'NF{print $2}')" = "" ]; then
  echo "%{F#2495e7} %{F#ffffff}$(/usr/sbin/ifconfig wlan0 | grep 'inet ' | awk '{print $2}')%{u-}"
else
  echo "%{F#2495e7}%{F#ffffff} No ethernet%{u-}"
fi
