# import dependencies
from flask import Flask

#We're now ready to create a new Flask app instance. 
# "Instance" is a general term in programming to refer to a singular version of something. 
# Add the following to your code to create a new Flask instance called app

app = Flask(__name__)

#This __name__ variable denotes the name of the current function. 
# You can use the __name__ variable to determine 
# if your code is being run from the command line or if it has been imported into another piece of code. 
# Variables with underscores before and after them are called magic methods in Python

# CREATE FLASK ROUTES
#----------------------
    # First, we need to define the starting point, also known as the root. 
    # To do this, we'll use the function @app.route('/'). Add this to your code now.

    # Whenever you make a route in Flask, you put the code you want in that specific route below, for instance
    #create a function named helloworld

@app.route('/')

def hello_world():
    return 'Hello World'

#The process of running a Flask app is a bit different from how we've run Python files.
#  To run the app, we're first going to need to use the command line to navigate to the folder where we've saved our code.
#  You should save this code in the same folder you've used in the rest of this module.
#Once you've ensured that your code is saved in the proper directory, 
# then run the following command if you are on a Mac. 
# This command sets the FLASK_APP environment variable to the name of our Flask file, app.py

#(export FLASK_APP=app.py)
#(flask run)
#above code in git bash in the path were the file is saved.

#When you run this command, you'll notice a line that says "Running on" followed by an address. 
# This should be your localhost address and a port number.



