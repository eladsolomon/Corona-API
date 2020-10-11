
import requests
import sys

if(len(sys.argv)>1):
    for country in sys.argv[1:]:
        responeCases = requests.get('http://localhost:8080/newCasesPeak?country=' + country)
        print(responeCases.text)

        responeDeaths = requests.get('http://localhost:8080/deathsPeak?country=' + country)
        print(responeDeaths.text)

        responeRecover = requests.get('http://localhost:8080/recoveredPeak?country=' + country)
        print(responeRecover.text)
else: #In case no country insert
        responeCases = requests.get('http://localhost:8080/newCasesPeak')
        print(responeCases.text)

        responeDeaths = requests.get('http://localhost:8080/deathsPeak')
        print(responeDeaths.text)

        responeRecover = requests.get('http://localhost:8080/recoveredPeak')
        print(responeRecover.text)
