#!/bin/sh

if [ "$(/usr/sbin/ifconfig enp1s0 | grep 'inet ' | awk 'NF{print $2}')" != "" ] && [ "$(/usr/sbin/ifconfig wlp2s0 | grep 'inet ' | awk 'NF{print $2}')" != "" ]; then
  echo "%{F#2495e7} %{F#ffffff}$(/usr/sbin/ifconfig enp1s0 | grep 'inet ' | awk '{print $2}')%{u-}"
elif [ "$(/usr/sbin/ifconfig enp1s0 | grep 'inet ' | awk 'NF{print $2}')" != "" ] && [ "$(/usr/sbin/ifconfig wlp2s0 | grep 'inet ' | awk 'NF{print $2}')" = "" ]; then
  echo "%{F#2495e7} %{F#ffffff}$(/usr/sbin/ifconfig enp1s0 | grep 'inet ' | awk '{print $2}')%{u-}"
elif [ "$(/usr/sbin/ifconfig wlp2s0 | grep 'inet ' | awk 'NF{print $2}')" != "" ] && [ "$(/usr/sbin/ifconfig enp1s0 | grep 'inet ' | awk 'NF{print $2}')" = "" ]; then
  echo "%{F#2495e7} %{F#ffffff}$(/usr/sbin/ifconfig wlp2s0 | grep 'inet ' | awk '{print $2}')%{u-}"
else
  echo "%{F#2495e7}%{F#ffffff} No ethernet%{u-}"
fi
