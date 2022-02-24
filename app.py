from flask import Flask, render_template, request, jsonify
import os,sys,requests,json
from random import randint

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello, world!</h1>'


@app.route('/parse',methods=['POST'] )
def extract():
  text=str(request.form['value1'])
  payload = json.dumps({"sender": "Rasa","message": text})
  headers = {'Content-type': 'application/json', 'Accept':     'text/plain'}
  response = requests.request("POST",   url="http://localhost:5005/webhooks/rest/webhook", headers=headers, data=payload)
  response=response.json()
  resp=[]
  #print(response)
  for i in range(len(response)):
    try:
      resp.append(response[i]['text'])
    except:
      continue
  result=resp
  #return render_template('index.html', result=result,text=text)
  return jsonify(sender="Rasa",message=response)

  
if __name__ == "__main__":
  app.run(debug=True) 
