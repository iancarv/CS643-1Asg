from flask import Flask,request,redirect,render_template
from twilio.rest import TwilioRestClient
import twilio.twiml
app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def hello():
    return "HI!"

@app.route("/r/",methods=['GET','POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
    message=request.form['body']
    resp = twilio.twiml.Response()
    resp.message("You said " + message)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
