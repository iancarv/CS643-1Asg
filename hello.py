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
            answer=answer+i + ""
        message=answer
    if(message== "CARBOHYDRATES"):
        value= random.sample(carbohydrates,3)
        answer=""
        for i in value:
            answer=answer+i+ ""
        message=answer
    if(message== "FIBRE"):
        value= random.sample(fibre,3)
        answer=""
        for i in value:
            answer=answer+i + ""
        message=answer
    if(message== "FAT"):
        value= random.sample(fat,3)
        answer=""
        for i in value:
            answer=answer+i + ""
        message=answer
    if(message== "IRON"):
        value= random.sample(iron,3)
        answer=""
        for i in value:
            answer=answer+i + ""
        message=answer
    if(message== "ZINC"):
        value= random.sample(zinc,3)
        answer=""
        for i in value:
            answer=answer+i + ""
        message=answer
    if(message== "CALCIUM"):
        value= random.sample(calcium,3)
        answer=""
        for i in value:
            answer=answer+i + ""
        message=answer
    if(message== "VITAMIN A"):
        value= random.sample(vitamina,3)
        answer=""
        for i in value:
            answer=answer+i + ""
        message=answer
    if(message== "VITAMIN B"):
        value= random.sample(vitaminb,3)
        answer=""
        for i in value:
            answer=answer+i + ""
        message=answer
    if(message== "VITAMIN C"):
        value= random.sample(vitaminc,3)
        answer=""
        for i in value:
            answer=answer+i + ""
        message=answer
    # else:
    #     message="Please enter Nutrients from FAT,CALCIUM,VITAMIN A/B/C,ZINC,FIBRE,FAT,CARBOHYDRATES,PROTEINS one at a time to receive appropiate food items"
    resp = twilio.twiml.Response()
    resp.message(message)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
