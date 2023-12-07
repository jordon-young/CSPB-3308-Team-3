###############################################################################
##
## This starter code was taken from Lab  6 Flask application and modified
## for the team 3 application
##
## The **prefix.py** code is included to allow you to develop your code within
## the **csel.io** environment.  There is a required prefix to be used when
## pages access the **csel.io** virtual machine from your local machine browser.
## 
## The prefix code will have no effect when running Flask on your local machine
## as it looks to make sure you are running on **csel.io** virtual machine.
##
## Author: Dylan Smith - Sept 2022
## Contributor: Fall 2023 Team 3 Members
##
###############################################################################


###############################################################################
## Import "prefix" code into your Flask app to make your app usable when running
## Flask either in the csel.io virtual machine or running on your local machine.
## The module will create an app for you to use

from flask import Flask, render_template, url_for, request, jsonify, redirect
import indexDB 

# create app to use in this Flask application
app = Flask(__name__, static_folder='static')


###############################################################################

@app.route('/foodtracking')
def index():

    

    return render_template('/index.html')

@app.route('/histinput', methods=['POST'])
def histinput():

    # get input information
    date = request.form.get('dateinput')
    cals = request.form.get('calories')
    fat = request.form.get('fat')
    protein = request.form.get('protein')
    carbs = request.form.get('carbs')

    # will have to include user_id functionality when db is connected
    indexDB.add_to_history(date, cals, fat, protein, carbs)

    return redirect('/foodtracking', code=302)

###############################################################################
# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server using port 3308 instead of port 5000.
    app.run(host='0.0.0.0', port=3308)
