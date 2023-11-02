from flask import Flask,render_template,request
import requests 

app = Flask(__name__) 

@app.route("/homepage")
def homepage():
    return render_template("index.html") 

@app.route("/weatherapp",methods=['POST','GET'])
def inputs_by_form():
    url = "https://api.openweathermap.org/data/2.5/weather" 
    params={
        'q':request.form.get("city"),
        'appid':request.form.get("appid"),
        'units':request.form.get("units")
        }

    responsefromapi = requests.get(url,params)
    final_output = responsefromapi.json()
    return final_output 



if __name__=="__main__":
    app.run(host="0.0.0.0",port=5002)
