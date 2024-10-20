#!/bin/bash

echo "%{F#ffffff} %{F#ffffff}$(date -u | awk 'NF{print $5}')%{u-}"
