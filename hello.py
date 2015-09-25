from flask import Flask,request,redirect,render_template
from twilio.rest import TwilioRestClient
import twilio.twiml
app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def hello():


    return render_template('in.html')




@app.route("/r/",methods=['GET','POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""

    resp = twilio.twiml.Response()
    resp.message("Hello!!! This is dhruv testing")
    return str(resp)

@app.route("/sendsms/")
def send_page():
    return render_template('send.html')

@app.route("/t/",methods=['GET','POST'])
def send():
    number=request.form['number']
    message=request.form['message']
    account_sid = "AC57ca6ef8bb59068da941ad8b6d271271"
    auth_token = "a76f950ce8c879fad071f22e4c3376ec"
    client = TwilioRestClient(account_sid, auth_token)

    message = client.messages.create(to=number, from_="+17327092519",
                                     body=message)

    ackk= "Your message has been sent to " + number + " !!!!"
    return render_template('response.html',mess=ackk)


if __name__ == "__main__":
    app.run(debug=True)