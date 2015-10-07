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

nutrients = {
    "PROTEINS" : protiens,
    "CARBOHYDRATES" : carbohydrates,
    "FIBRE" : fibre,
    "FAT" : fat,
    "IRON" : iron,
    "ZINC" : zinc,
    "CALCIUM" : calcium,
    "VITAMIN A" : vitamina,
    "VITAMIN B" : vitaminb,
    "VITAMIN C" : vitaminc
}


"""Updated the array of nutrient_name above"""


@app.route("/",methods=['GET','POST'])
def hello():
    return "HI!"

@app.route("/r/",methods=['GET','POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
    print("Hello")
    message=request.form['Body'].upper()
    message = response_string(message)
    resp = twilio.twiml.Response()
    resp.message(message)
    return str(resp)

def response_string(message):
    if(message== "HI"):
        message="Hello"
    elif(message in nutrients):
        nutrient = nutrients[message]
        value = random.sample(nutrient, 3)
        answer = ""
        for i in value:
            if (answer == ""):
                answer = i
            else:
                answer = answer + " " + i
        message = answer
    else:
        message="Please enter Nutrients from FAT,CALCIUM,VITAMIN A/B/C,ZINC,FIBRE,FAT,CARBOHYDRATES,PROTEINS one at a time to receive appropiate food items"

    return message



if __name__ == "__main__":
    app.run(debug=True)
