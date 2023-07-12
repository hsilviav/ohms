# Online Health Monitoring System

This prototype uses Django (with SQLite3 database) and Python to collect health data from user input and/or a smartwatch simulator app. The data is then displayed to both the patient and the doctor assigned to the patient in question. The system highlights if the metric is out of the normal range.

## Docker Installation 

NOTE: Docker required to be pre-installed.
Use the official Docker website to [install](https://docs.docker.com/get-docker/) the package that best suits your environment.

## Running the container 

Use the following commands to build the docker image and run the container:

```bash
docker-compose build 
docker-compose up
```

The name of the image build is: ohms-web
The name of the container is: ohms

You should now be able to access the prototype at 
'localhost:8000'

## Running the server

In case the container is not running you follow these steps to access the project at 'localhost:8000'

1. Activate the virtual environment

In your terminal, navigate to the projects directory and type in the following command:

 ```bash
.\ohms_env\Scripts\activate
```

2. Run the development server

Use the next command in your terminal:

 ```bash
python manage.py runserver
```

Access 'localhost:8000' and you'll be able to see the landing page.

