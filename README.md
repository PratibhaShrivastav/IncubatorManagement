# IncubatorManagement

## A Codeutsava 3.0 Project :


This is an incubator management system

Steps to clone and run this program locally:

__In Terminal execute following commands:__

`git clone https://github.com/PratibhaShrivastav/IncubatorManagement.git`


`cd IncubatorManagement`


`virtualenv env`


`source env/bin/activate`


`pip install -r requirements.txt`

If you want to avail email feature :

1. Change your working directory to /IncubatorManagement

2. In settings.py change these :

`EMAIL_HOST_USER = 'email@gmail.com'`


`EMAIL_HOST_PASSWORD = 'YourPassword'`


`python manage.py runserver`


now Navigate to http://localhost:8000



__About project__ :
This is a simple management website for Incubators where startups can apply for incubation, mentors can apply for mentorship. There is an application process for startups where they will be notified about their acceptance/rejection via email, a separate room booking feature where users can book seats for themselves as well as suggest seats for other users, startups can request mentors for mentorship where mentors will be notified about all requests on their dashboard, a startup logs portal to takeup weekly/monthly progress reports and classify the progress rate through sentiment analysis, coffee token management and a local wallet for each user which shows the pending amount for each user and also notifies a user when the wallet balance goes low.
