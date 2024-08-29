#!/bin/sh

# systray battery icon
cbatticon -u 5 &
# systray volume
volumeicon &
feh --bg-fill /home/codintdev/Pictures/wallpaper.jpg &
#picom --config /home/codintdev/.config/picom/picom.conf &
nm-applet &
udiskie -t &
