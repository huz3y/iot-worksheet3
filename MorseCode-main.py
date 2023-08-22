from microbit import *

def traffic_light():
    pin0.write_digital(1)  # Turn on green LED
    sleep(10000)  # Green light for 10 seconds
    pin0.write_digital(0)  # Turn off green LED
    
    pin1.write_digital(1)  # Turn on orange LED
    sleep(5000)  # Orange light for 5 second
    pin1.write_digital(0)  # Turn off orange LED
    
    pin2.write_digital(1)  # Turn on red LED
    sleep(10000)  # Red light for 10 seconds
    pin2.write_digital(0)  # Turn off red LED

while True:
    traffic_light()
