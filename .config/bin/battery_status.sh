#!/bin/sh

battery_level="$(acpi | awk 'NF{print $4}' | tr -d ',%')"

if [ $battery_level -ge 80 ] && [ $battery_level -le 100 ]; then
  echo "%{F#D2DE32} %{F#ffffff}$battery_level%%{u-}"
elif [ $battery_level -ge 40 ] && [ $battery_level -lt 80 ]; then
  echo "%{F#F4CE14} %{F#ffffff}$battery_level%%{u-}"
elif [ $battery_level -ge 20 ] && [ $battery_level -lt 40 ]; then
  echo "%{F#C63D2F} %{F#ffffff}$battery_level%%{u-}"
else
  echo "%{F#FF5B22} %{F#ffffff}$battery_level%%{u-}"
fi
