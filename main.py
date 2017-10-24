import sys
import uwebsockets
from machine import Pin, PWM
led = PWM(Pin(14, mode=Pin.OUT), freq=400) # SCK LED on WeMos D1

CONTENT = """\
HTTP/1.0 200 OK
Content-Type: text/html

<html>
<head>
  <script type="text/javascript">
  var ws = new WebSocket("ws://iot.koodur.com:80/ws/olx/");
  ws.onopen = function (event) { console.info("websocket connected"); };
  ws.onmessage = function (event) { console.log(event.data); }
  var lastValue = false;
  function duty(e) {
    if (lastValue == e.value) return;
    lastValue = e.value;
    ws.send("duty:" + e.value);
  }
  </script>
</head>
<body>
  <input type="range" min="0" max="1023" step="10" onMouseMove="duty(this);" onTouchMove="duty(this);"/>
</body>
</html>
"""

def main():
    uri = "ws://iot.koodur.com:80/ws/olx"
    print("Connecting to:", uri)
    conn = uwebsockets.connect(uri)
    conn.send("alive")
    while True:
        print("Reading message...")
        try:
            fin, opcode, data = conn.read_frame()
        except OSError: # Connection timeout or reset
            sys.exit() # Soft reset
        if data.startswith(b"duty:"):
            led.duty(int(data[5:]))
        else:
            print("Got unknown command:", data)

main() # Press Ctrl-C to stop web server
