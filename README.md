# DealFlow ( Django-REST-FRAMEWORK )

Built a set of REST API's with Django-Rest-Framework that : -
* Allows a client to fetch (GET REQUEST) all available freelancers on Dealflow
* Allows to add (POST REQUEST) freelancers on DealFlow
* Allows search by first name, last name, email, phone number and/or followers (DJANGO-FILTER) on the platform  
* Supports pagination (DJANGO-PAGINATION) 
* Stores these freelancers data in a Database (MONGO-DB)
* Hosted on AWS Instance. Check the link here :
  ```
  http://3.15.5.27:8000/freelancers/
  ```

## Setting-up Virtual envvironment :
* Install virtualenv :
```
pip install virtualenv
```
* Create a Virtual Environment :
```
virtualenv .env
```
* Activate the Virtual Environment :
```
.\.env\Scripts\activate
```

## Installing Dependecies and Libraries :
* Install the required libraries :
```
pip install django, djangorestframework, django-filter, djongo, pymongo==3.12.3
```

## Running the Project :
* Make Migrations :
```
python manage.py makemigrations
```
* Migrate
```
python manage.py migrate
```
* Running the Server
```
python manage.py runserver
```

# API ENDPOINTS
* To fetch (GET REQUEST) all the freelancers and to add (POST) any new freelancer :
```
localhost:8000/freelancers
```
* To Search with filter :
```
localhost:8000/freelancers/?<filter_name1>=<filter_value1>&<filter_name2>=<filter_value2> and so on.... to apply more filters
```
Above filter_name can be one of these {first_name, last_name, email, phone_number, followers} and filter_values can be anything

# PAGINATION
* Pagination has been applied to show only 2 results per page
* Link for further pages and moving to previous pages is shown with the Results itself

# DATABASE STORING
* Mongo-DB Database connection using djongo python library has been made, with Database name as FreeLancers

# SCREENSHOTS
* Get Request
  ![GET REQUEST](https://github.com/J-VIKAS/DealFlow/blob/main/ScreenShots/GetRequest.PNG)  
* Pagination
  ![PAGINATION](https://github.com/J-VIKAS/DealFlow/blob/main/ScreenShots/Pagination.PNG)  
* Filtering
  ![FILTERING](https://github.com/J-VIKAS/DealFlow/blob/main/ScreenShots/Filtering.PNG)  
* MongoDB
  ![MONGO-DB](https://github.com/J-VIKAS/DealFlow/blob/main/ScreenShots/MongoDB.PNG)  
* Posting
  ![POSTING](https://github.com/J-VIKAS/DealFlow/blob/main/ScreenShots/Posting.PNG)  
  ![POSTING-RESULT](https://github.com/J-VIKAS/DealFlow/blob/main/ScreenShots/PostingResult.PNG)

### Hoping you'll like the project, feel free ask for any queries  
