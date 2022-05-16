# Polygence Coding Challenge

The coding challenge portion of the Polygence Engineering interview!

## Project overview

It is a simple application where you can track your spendings.

A spending has the followings properties:

    - when it happened (gives automatically the date and number when you added the spending)
    - how much did we spend ( 200 equals 2. So what you write it is with decimals)
    - in what currency (HUF or USD)
    - for what/description

This simple web app allows the users to:

       - Create a new spending
       - List all the spendings
       - List all the spendings ordered by amount, date
       - List all the spendings filtered by currency

## Building up the project

You have to open the project folder in terminal or interpreter (such as VS code).

####pip requirements:
After you have to run the following command: "pip install -r requirements.txt". You can do it globally or if you want to 
you can create a virtual environment for it ("mkdir venvfolder" -> in the folder: "python3 -m venv env" -> "source env/bin/activate" and
after all run the "pip install -r requirements.txt").

####node requirements:
To have the required dependencies for the node module you have to run "npm install"

####Set up database:
To have the empty database to work with you have to run "python3 manage.py migrate"
After you have a db.sqlite file where you can save the spendings and list them as well

####run the servers:
The have both servers running you just have to start it.
The Django will start by: "python3 manage.py runserver"
The React will start by: "npm start"

#All ready to use in localhost:3000





