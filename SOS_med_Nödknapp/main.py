from machine import Pin # Import the Pin class from the machine module
from utime import sleep # Import the sleep function from the utime module

led = Pin(15, Pin.OUT) #Initialize the LED pin as an output
button = Pin(14, Pin.IN, Pin.PULL_DOWN) #Initialize the button pin as an input with a pull-down resistor
#Define the time intervals for Morse code
dot = 0.25 # Duration of a dot
dash = 3 * dot # Duration of a dash(3 times the duration of a dot)
short_wait = dot # Short wait time between blinks
nextChar = 3 * dot # Wait time between characters

# Number of times the SOS will be sent
num_of_sos = 10
# Function to blink the LED for a short duration(dot)
def short_blink():
#  print('S = ...')
  led.on()
  sleep(dot)
  led.off()
  sleep(short_wait)

#Function to blink the LED for a long duration(dash)
def long_blink():
#  print('O = ---')
  led.on()
  sleep(dash)
  led.off()
  sleep(short_wait)
#Function to send the SOS signal a specified number of times
def send_sos(num_of_sos):
  for i in range(num_of_sos):
    if button.value(): #Check if the button is pressed
      print("Sending SOS in 2 seconds")
      sleep(2) #Wait for 2 seconds before sending the SOS signal
      for i in range(3):# Send 'S' in Morse code (three short blinks)
        short_blink()
      sleep(nextChar)# Wait before sending the next character
      for i in range(3):# Send 'O' in Morse code (three long blinks)
        long_blink()
      sleep(nextChar)# Wait before sending the next character
      for i in range(3):# Send 'S' in Morse code (three short blinks)
        short_blink()

while True: #Main loop to continuously check the button is pressed
  if button.value(): #If the button is pressed
    send_sos(num_of_sos)# Send SOS signal
    

