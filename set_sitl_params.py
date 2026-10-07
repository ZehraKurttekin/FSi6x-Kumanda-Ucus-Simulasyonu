#!/usr/bin/env python3
"""Gercek dronla ayni ArduPilot guvenlik/davranis parametrelerini SITL'e yazar."""
from pymavlink import mavutil

PARAMS = {
    "MOT_SPIN_ARM": 0.15,
    "MOT_SPIN_MAX": 0.95,
    "BATT_MONITOR": 4,      # Analog Voltage and Current
    "BATT_VOLT_MULT": 21.13,
    "BATT_CAPACITY": 5200,
    "BATT_ARM_VOLT": 13.2,
    "BATT_CRT_VOLT": 13.1,
    "BATT_LOW_VOLT": 13.3,
    "BATT_FS_LOW_ACT": 1,   # Low battery -> Land
    "FS_THR_ENABLE": 1,     # RC kaybi -> Always RTL
    "FS_THR_VALUE": 980,
}


def main():
    m = mavutil.mavlink_connection("udp:127.0.0.1:14551")
    m.wait_heartbeat()
    print(f"Baglandi: sysid={m.target_system}")
    AUTOPILOT_COMPONENT = 1  # target_component=0 ArduPilot'ta yanitsiz kaliyor

    for name, value in PARAMS.items():
        m.mav.param_set_send(
            m.target_system, AUTOPILOT_COMPONENT,
            name.encode(), float(value),
            mavutil.mavlink.MAV_PARAM_TYPE_REAL32,
        )
        ack = None
        for _ in range(10):
            msg = m.recv_match(type="PARAM_VALUE", blocking=True, timeout=1)
            if msg and msg.param_id.strip("\x00") == name:
                ack = msg
                break
        print(f"{name} = {value}  ->  {'OK ('+str(ack.param_value)+')' if ack else 'YANIT YOK'}")


if __name__ == "__main__":
    main()
