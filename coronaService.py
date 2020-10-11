from flask import Flask , request
import json
import coronaRequests

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to COVID-19 API"

@app.route("/status")
def status():
    return coronaRequests.getStatus()

@app.route("/newCasesPeak")
def newCasesPeak():
    country = request.args.get('country')
    return coronaRequests.getDataTypePeak(country, "new_confirmed" ,"newCasesPeak")

@app.route("/recoveredPeak")
def recoveredPeak():
    country = request.args.get('country')
    return coronaRequests.getDataTypePeak(country, "new_recovered" ,"recoveredPeak" )

@app.route("/deathsPeak")
def deathsPeak():
    country = request.args.get('country')
    return coronaRequests.getDataTypePeak(country, "new_deaths" , "deathsPeak")

@app.route('/<path:path>')
def catch_all(path):
    return json.dumps({})

if __name__ == "__main__":
    app.run(port='8080')
