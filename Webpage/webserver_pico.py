import machine
import network
import socket
from time import sleep
import secrets

led = machine.Pin(15 , machine.Pin.OUT)

# Change SSID and PASSWORD for the correct WIFI network
ssid = "SSID"
password = "PASSWORD"

def connect():
  #Connect to WLAN
  wlan = network.WLAN(network.STA_IF)
  wlan.active(True)
  wlan.connect(ssid, password)
  while wlan.isconnected() == False:
    print('Waiting for connection...')
    sleep(1)     
  ip = wlan.ifconfig()[0]
  print(f'Connected on {ip}')
  return ip

def open_socket(ip):
  # Open a socket
  address = (ip, 80)
  connection = socket.socket()
  connection.bind(address)
  connection.listen(1)
  return connection

def webpage(state):
  #Template HTML
  html = f"""
      <!DOCTYPE html>
      <html>
      <form action="./lighton">
      <input type="submit" value="Light on" />
      </form>
      <form action="./lightoff">
      <input type="submit" value="Light off" />
      </form>
      <p>LED is {state}</p>
      </body>
      </html>
      """
  return str(html)

def serve(connection):
  #Start a web server
  state = 'OFF'
  led.off()
  while True:
    client = connection.accept()[0]
    request = client.recv(1024)
    request = str(request)
    try:
      request = request.split()[1]
    except IndexError:
      pass
    if request == '/lighton?':
      led.on()
      state = 'ON'
    elif request =='/lightoff?':
      led.off()
      state = 'OFF'
    html = webpage(state)
    client.send(html)
    client.close()

try:
  ip = connect()
  connection = open_socket(ip)
  serve(connection)
except KeyboardInterrupt:
  machine.reset()
