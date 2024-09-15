#!/usr/bin/env python3
#
#############################
import subprocess           #
import time                 #
from libqtile import qtile  #
#############################
#
#

def def_battery():
    try:
        output = subprocess.check_output(['acpi', '-b']).decode('utf-8')
        percent = int(output.split(",")[1].strip().replace('%', ''))
        return percent
    except Exception as e:
        return None

def def_notification(message):
    subprocess.run(['notify-send', '-u', 'critical', message])

def main():
    while True:
        battery_level = def_battery()
        if battery_level is not None and battery_level <= 20:
            def_notification("[!] Batería Baja! Conecta el cargador.")
        time.sleep(300)

if __name__ == "__main__":
    main()
