from flask import Flask,request,redirect,render_template
from twilio.rest import TwilioRestClient
import twilio.twiml
import random
app = Flask(__name__)


protiens=['meat','fish','eggs','dairy products','nuts','seeds','legumes']
carbohydrates=['fruits','legumes','whole grains','white rice','white bread']
fibre=['fruits','whole grains','vegetables']
fat=['butter','red meat','whole milk','cheese']
iron=['lean meats','legumes','poultry','fish','beans','fish']
zinc=['beef','pork','lamb','dark chicken meat','nuts','yeast','legumes','whole grains']
calcium=['milk','tofu','almonds','ornage juice']
vitamina=['cheese','fish oil,carrots', 'broccoli','spinach','pumpkins','milk']
vitaminb=['avocados','bananas','beans','meat','nuts','poultry','wholegrains']
vitaminc=['orange','straberries','red pepper','broccoli']



"""Updated the array of nutrient_name above"""


@app.route("/",methods=['GET','POST'])
def hello():
    return "HI!"

@app.route("/r/",methods=['GET','POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
    message=request.form['Body']
    if(message== "Hi"):
        message="Hello"
    if(message== "PROTEINS"):
        value= random.sample(protiens,3)
        answer=""
        for i in value:
            answer=answer+i
        message=answer
    resp = twilio.twiml.Response()
    resp.message(message)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
