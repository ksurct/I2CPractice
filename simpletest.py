# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096
servo_cur = 100	 # Starting value for 'off' arg in set_pwm()


# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 10khz for our motors.
pwm.set_pwm_freq(10000)

print('Enter value between 0 and 4000 for the motors:')
# 'try' is used to check for a ctrl+c break -- on ctrl+c, we move to 'finally'
try:
  while True:
    response = int(input())  # Convert string into actual numerical value to transmit to motor.
    pwm.set_pwm(15, 0, response) # Set channel 15 on board (motor) to the 0-4000 value.

# Generates an exception to remove common ctrl+c error
except KeyboardInterrupt :
    pass

# 'finally' is thrown to, once 'try' catches a ctrl+c at the commmand line
finally:
    pwm.set_pwm(15,0,0)
