# Assignment

1. To Run this project

    - download the zip file extract it
    - cd in extracted folder
    - make a virtual environment
    
        - python -m venv venv
    
    - activate venv
    
        - source venv/bin/activate
    
    - install dependencies
    
        - python -r install requirements.txt

    - migrate database
        
        - python manage.py makemigartions
        
        - python manage.py migrate

    - change data base credentials in settings.py in the folder Assignment
     

### Folder structure 

    - Assignment (Project) - (Admin of project)

            -User 
                - user
                - post

            -Product 

                - product


### run

create a superuser to make login for the first time:

    - python manage.py createsuperuser 

after making superuser you can run the project

    - python manage.py runserver
    
redirect to:
    - localhost:8000/admin
    
