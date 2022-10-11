import requests
import json

def odeslatJednaciRad(data_sendgrid,data_zaznamy):
  
  emailOdeslan = odeslatEmail(data_sendgrid)
    
  webhook_data = odeslatData(data_zaznamy)
  
  return emailOdeslan, webhook_data

def odeslatEmail(data):
  return requests.post('https://hook.eu1.make.com/wzj5c9swoe0mnh0yle8rv3gofw87hhvw', data=json.dumps(data), headers={'Content-Type': 'application/json'})

def odeslatData(data):
  return requests.post('https://hook.eu1.make.com/8em6i5dm31jn10nz52wc5nlme0tf7w7l', data=json.dumps(data), headers={'Content-Type': 'application/json'})