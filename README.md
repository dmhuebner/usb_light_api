## USB Light API

#### A REST API that lets you change the color of a USB blinkstick.

https://www.blinkstick.com/

----

To run:

```$: python app.py```

Install dependencies:

```$: pip install -r requirements.txt```

To change the color of the blinkstick light:

GET

```http://127.0.0.1:5000/light/{HEX_CODE}```

Example: 
http://127.0.0.1:5000/light/ff0000

To set the light red.