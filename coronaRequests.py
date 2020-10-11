import requests
import json
import pycountry

def getStatus():
    respone = requests.get('http://corona-api.com/')
    if respone.status_code == 200:
        return json.dumps({"status" : "success"})
    return json.dumps({"status" : "fail"}) # Return fail when corona-api.com is not available

def getDataTypePeak(country, dataType, method):
    if (country):
        try:
            countryCode = pycountry.countries.search_fuzzy(country)[0].alpha_2
        except: # Country not found
            return  json.dumps({})

        countryData = requests.get('http://corona-api.com/countries/' + countryCode)
        countryDataTimeline =  json.loads(countryData.text)['data']['timeline']
    else: # Return all countries new cases peak
        country = "All"
        countryData = requests.get('https://corona-api.com/timeline')
        countryDataTimeline =  json.loads(countryData.text)['data']

    return extractLast30DaysPeak(countryDataTimeline, dataType , country , method)
     
def extractLast30DaysPeak(dataTimeline, dataType , country , method):
    maxCasesType = 0
    last30Days = dataTimeline[:30]
    for record in last30Days:
        if maxCasesType < record[dataType]:
            maxCasesType = record[dataType]
            date =record["date"]
    return json.dumps({"country" : country , "method" : method , "date" : date , "value" :maxCasesType})
