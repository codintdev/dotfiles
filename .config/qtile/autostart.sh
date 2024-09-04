#!/bin/sh

# systray battery icon
cbatticon -u 5 &
# systray volume
volumeicon &
# Wallpaper
feh --bg-scale /home/codintdev/Pictures/wallpaper.png &
#picom --config /home/codintdev/.config/picom/picom.conf &
nm-applet &
# udiskie -t &
