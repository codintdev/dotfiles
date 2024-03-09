#!/bin/bash
 
ip_address="10.10.112.78"
machine_name="Startup"
 
if [ $ip_address ] && [ $machine_name ]; then
    echo "%{F#A73121} %{F#ffffff}$ip_address%{u-} - $machine_name"
else
    echo "%{F#A73121} %{u-}%{F#ffffff} No target"
fi
