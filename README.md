
# Crowdsourcing policing - Automatic Number Plate Recognition

## Local development

This project is built using the [Flask](http://flask.pocoo.org/) web
framework. It runs on Python 3.6+.

To run the app locally:

1. Clone this repository and `cd` into it

   ```bash
   git clone git@github.com:TwilioDevEd/whatsapp-media-tutorial-flask.git
   cd whatsapp-media-tutorial-flask
   ```

1. Create a new virtual environment using
   [virtualenv](https://virtualenv.pypa.io/en/latest/)

   ```bash
   virtualenv -p python3 venv
   source venv/bin/activate
   ```

1. Install the requirements

   ```bash
   pip install -r requirements.txt
   ```

1. Run the application

   ```bash
   flask run
   ```

1. Expose your application to the wider internet using
   [ngrok](http://ngrok.com/). This step is important because the
   application won't work as expected if you run it through localhost.

   ```bash
   ngrok http -host-header=localhost 5000
   ```


1. Configure Twilio's Sandbox for WhatsApp to call your webhook URL

   You will need to configure your [Twilio Sandbox for WhatsApp](https://www.twilio.com/console/sms/whatsapp/sandbox) to call your application (exposed via ngrok) when your Sandbox number receives an incoming message. Your URL will look something like this:

   ```
   http://6b5f6b6d.ngrok.io/whatsapp/
   ```


1. Check it out at http://localhost:5000

## How to Demo

1. Send a message with a image attachment of a vehicle  to your WhatsApp Sandbox phone number

2. The number plate number will be sent to you

