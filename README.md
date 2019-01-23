## USB Light API

#### A REST API that lets you change the color of a USB blinkstick.

https://www.blinkstick.com/

----

##### Install project dependencies:

libusb is required so the API can communicate with a USB device

```$: brew install libusb```

Install package dependencies

```$: pip install -r requirements.txt```

---

To run the API:

```$: python app.py```

To change the color of the blinkstick light:

GET

```http://127.0.0.1:5000/light/{HEX_CODE}```

Example: 
http://127.0.0.1:5033/light/ff0000

To set the light to red.

---

To run the CPU load monitor:

```$: python cpu.py```

The blinkstick LED will light up dynamically based on CPU load. The lights move from green to shades of yellow and orange to red.

---

