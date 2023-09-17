import time

import psutil


def battery_charge():
    battery = psutil.sensors_battery()
    battery_volume = int(battery.percent)
    i = 0
    for i in range(battery_volume):
        time.sleep(0.05)
        print(f"Count current charge volume: ....... {i}")
        i += 1
    print(f"The volume of battery charge is: {battery_volume}%.")


battery_charge()
