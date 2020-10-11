# Corona-API

This project include python service that allowed you to send request and recive answer in json format.
The service will run on localhost:8080


## Get Status
Returns a value of success / fail to contact the backend API.
### Request
    curl localhost:8080/status

### Response

    {“status”: “success”}

## Get new cases peak
Returns the date (and value) of the highest peak of new
Covid-19 cases in the last 30 days for a required country.   
### Request

    curl localhost:8080/newCasesPeak?country=israel

### Response

     {“country”:”israel”,“method”:“newCasesPeak”,”date”:“9/12/20”,“value”:4158}
     
## Get new death peak
Returns the date (and value) of the highest peak of recovered
Covid-19 cases in the last 30 days for the required country.
### Request

    curl localhost:8080/deathsPeak?country=israel

### Response

    {“country”:”israel”,“method”:“deathsPeak”,”date”:“9/12/20”,“value”:110}
    
## Get new recoverd peak
Returns the date (and value) of the highest peak of death Covid-19
cases in the last 30 days for a required country.
### Request

`new recoverd peak`

     curl localhost:8080/recoveredPeak?country=israel

### Response

     {“country”:”israel”,“method”:“recoveredPeak”,”date”:“9/12/20”,“value”:11000}
    

# How to run Jenkinsfile pipeline:

# installation:

First check that git installed in your computer.

Now go to Manage Jenkins -> Global Tool Configuration ->Git ->Git installation.
Verify that git is define.

Second download and install Docker.

Third, download to jenkins the following plugin:
Docker pipeline.
Docker.
  
# pipeline settings:

Choose "This project is parameterized".
After that choose "Multi-Line string paramter"
And name the paramter : "country"

Should look like this:

![Screenshot_2020-10-11 ee Config  Jenkins](https://user-images.githubusercontent.com/48445002/95673258-e8c3af00-0b5b-11eb-8105-4e7d00e3dc1f.png)


Starting the pipeline with git with the follwoing setting(notice to change the brance to"main"):

Git url: https://github.com/eladsolomon/Corona-API

![Screenshot_2020-10-11 gg Config  Jenkins (1)](https://user-images.githubusercontent.com/48445002/95673201-8d91bc80-0b5b-11eb-8057-e3329f091712.png)

That's it, you are ready to go!

# Running the pipeline:

While starting the job by clicking build, you will ask to enter parameters:

![Screenshot_2020-10-11 Jenkins](https://user-images.githubusercontent.com/48445002/95673368-9d5dd080-0b5c-11eb-9f4d-e155e97b19c0.png)

Enter each country you will like seperate by comma
Example:

![Screenshot_2020-10-11 Jenkins(1)](https://user-images.githubusercontent.com/48445002/95673384-c716f780-0b5c-11eb-8c40-904ff4dc9413.png)

Click build and you will get 3 answer for each country:
- new cases peak
- new recoverd peak
- new death peak

![Screenshot_2020-10-11 ThiwWillWork #79 Console  Jenkins](https://user-images.githubusercontent.com/48445002/95673413-19f0af00-0b5d-11eb-926e-68eef86b0d47.png)

If no country enter , stats of all the countries included will show.



By Elad Solomon
