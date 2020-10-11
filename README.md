# Corona-API

This project include python service that scrapes data from external API and response with JSON format.
The service will run on localhost:8080

# installation:

first download to jenkins the following plugin:
Docker
  
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

# running the program:

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
