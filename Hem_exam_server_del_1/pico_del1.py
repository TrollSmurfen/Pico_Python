import machine
import time
import socket
import network
# Manages an LED connected to a specified pin, allowing it to be turned on, turned off, and its state to be checked
class LEDController:
    """Class to control the LED state."""
    def __init__(self, pin_name):
        self.led = machine.Pin(pin_name, machine.Pin.OUT)

    def turn_on(self):
        self.led.value(1)

    def turn_off(self):
        self.led.value(0)

    def get_state(self):
        return 'On' if self.led.value() == 1 else 'OFF'
# Handles connecting to a WiFi network using provided SSID and password, and prints the connection status
class WiFiConnector:
    """Class to handle WiFi connection."""
    def __init__(self, ssid, password):
        self.ssid = ssid
        self.password = password
        self.wifi_status = network.WLAN(network.STA_IF)
        self.wifi_status.disconnect()
        self.wifi_status.active(True)

    def connect(self):
        self.wifi_status.connect(self.ssid, self.password)
        while not self.wifi_status.isconnected():
            time.sleep(1)
            print('Connecting to a wireless network...')
        print('WiFi connected successfully')
        print(self.wifi_status.ifconfig())
# Sets up a simple web server that serves a webpage to control the LED. It handles HTTP requests to turn the LED on or off and generates the corresponding HTML response
class WebServer:
    """Class to handle the web server."""
    def __init__(self, led_controller):
        self.led_controller = led_controller
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(('', 80))
        self.socket.listen(5)

    def web_page(self):
        gpio_state = self.led_controller.get_state()
        html = f"""
        <html>
            <head>
                <title>Pico W Web Server</title>
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <link rel="icon" href="data:,">
                <style>
                    html{{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}}
                    h1{{color: #0F3376; padding: 2vh;}}
                    p{{font-size: 1.5rem;}}
                    button{{display: inline-block; background-color: #4286f4; border: none;border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}}
                    button2{{background-color: #4286f4;}}
                </style>
            </head>
            <body>
                <h1>Pico W Web Server</h1>
                <p>GPIO state: <strong>{gpio_state}</strong></p>
                <p><a href="/?led=on"><button class="button">ON</button></a></p>
                <p><a href="/?led=off"><button class="button button2">OFF</button></a></p>
            </body>
        </html>
        """
        return html

    def handle_request(self):
        conn, addr = self.socket.accept()
        req = conn.recv(1024).decode()
        print('Request:', req)
        if '/?led=on' in req:
            self.led_controller.turn_on()
        elif '/?led=off' in req:
            self.led_controller.turn_off()
        response = self.web_page()
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()

# main
ssid = 'SSID'          # Enter the router name
password = 'PASSWORD'      # Enter the router password

wifi_connector = WiFiConnector(ssid, password)
wifi_connector.connect()

led_controller = LEDController("LED")
web_server = WebServer(led_controller)

try:
    while True:
        web_server.handle_request()
except Exception as e:
    print("Exception -", e)
    web_server.socket.close()
