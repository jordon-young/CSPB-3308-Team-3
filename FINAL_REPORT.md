# Team 3 Fitness Tracker Final Report

Project Title: Team 3 Fitness Tracker Application

| Team Member | Github Username |
| :---: | :---: |
| **William Barber** | wjbarberjr | 
| **Eric Hernandez** | EWHernandez |
| **William Hinkley** | WiHi1131 |  
| **Dylan Smith** | dylan33smith |
| **Jordon Young** | jordon-young |

Make sure that your repository has the following files committed to remote repository:
- [X] REAMDE.md
- [X] WEEKLY_STATUS.md
- [X] PAGE_TESTING.md
- [X] SQL_TESTING.md
- [X] FINAL_REPORT.md
- [X] Project presentation files from Presentation Milestone
- [X] Video of demo
- [X] Source code
- [X] Test cases
- [X] Source documentation, and auto-doc files
- [X] Link to Public Deployment Site (Heroku or similar)

Project tracker link (Instructor can access): https://www.figma.com/file/Sp4L2uwhVrR8WGC1pQ5vDp/Project-Planning?type=whiteboard&node-id=0%3A1&t=NzAzoc6VsZtHbWeZ-1

Link to 5 minute video: https://youtu.be/YS46r0HW-S0

Version control repository link (make sure the instructor(s) have access): https://github.com/jordon-young/CSPB-3308-Team-3/tree/main


List your public hosting site and make sure that it is available: 
Page: https://team-3-sb0f.onrender.com/  

Include a Final Status Report: This is included in our README.md file but it is also pasted below.

# Fitness App Way Current/Future State

### Login Page

Current - Currently the login page compares the user name and password to existing users in the database and only allows a user to the about page if their credentials match the credentials in the database

Future features
1. Would like to implement hashing for passwords for security reasons.
2. Currently we pass user ID in the open via a url, would like to use hashing for that as well.
3. Add more aesthetic features consistent with the brand.

### Create Account

Current - The current create account page takes information from a user and adds them to the database so they can log in. The only input validation exists on username and email. 

Future features
1. Apply more input validation to ensure users are not able to bypass important information.
2. Create better error handling to help developers and users understand what is happening.
3. Add more aesthetic features consistent with the brand.

### Forgot Password

Current - The forgot password page takes a users email and validates against any valid email in the database. If it matches a message is sent to user and they are redirected to login page.

Future features
1. Send a password reset link to the users active  email, allowing them to actively change their password.
2. Implement security questions and have them stored in the database.

### About Page

Current - The about page serves as a landing page after the user logs in. Currently there is nothing to stop the user from accessing the page directly without logging in. 

Future features
1. Implement security features to redirect the user to the login page if a valid user ID is not passed with the URL.
2. Add more aesthetic features consistent with the brand.

### Exercise Input Page

Current/Issues - Where the page currently stands it has created fields and supports the correct data types. As a standalone page it had full working database function, but because of poor planning and communication I did not have my page set up to communicate with other team memebers page. The hope the exercise_input page would take the data input, store it into the database, and when routed to the exercise_log page, the data would be shown there from my page. I did not account for that in getting it to work on my own so the overall functionality suffered a bit. There is javascript written to populate the 'workouts' table, but the output routing is defined wrong.

Future features
1. The exercise input page can store groups of individual exercises into an entire workout session.
2. More detail and a couple of more data fields in the exercise input form
   - Button selectors for exercise type (cardio, weight training).
   - Drop down integer fields that define the sets of an individual weight training exercise.
3. Improved CSS that organizes the input form to create a simple but detailed experience for the user.

### Exercise Output Page

#### Current State

Upon visiting the URL for the exercise output, a fetch request is made to the database API to select all exercises. The JSON returned from the request is loaded in an iframe.

#### Known Issues

The API for adding workouts is functional, but the connection from the input page does not work, so the only way to add new entries is by manually using the API, as in this example:

`/db/workouts/create_workout?date=2023-12-31&name=Jogging&duration=30&type=Cardio&notes=Morning+run`

#### Future Features

Our original intention was to have a much more complicated input interface and relational database for managing different workout types and exercises. The output page would have needed to list all workouts, and the user could choose to expand sections to see more information about that workout, depending on the type.

In the case of a strength training workout, expanding the workout entry would show the exercises performed during that workout, and expanding a particular exercise would show information about the sets completed. The expand / collapse functionality was going to be used as a learning opportunity, not as a practical solution–each expand action would be an API request.


### Food Tracking Page

Current/Issues - The food tracking page currently has input fields for the date, calories, fats, proteins and carbs. It then has two functionalities that can be used with those inputs, the first is to load them into the food tracking table in our database, and the second is that it includes a table that can take multiple of those inputs and list each entry as well as the total macros across all of the entries. The idea for this was that if a meal had multiple items in it, you could implement the nutritional info for each of them and then you would only have to add the meal to the tracking table rather than each part of the meal. There are buttons for both of the above functions as well as a reset button that can reset the table showing the total inputs.

Future features
1. The food history table isn't currently connected to the users table. This means that when you upload nutrional values to the table, there is no tag to retrieve an individual users data. The idea of the table is that it can be used to track a users nutritional history, so in order to do that, the food_history table has to have a reference to the users table so that each users history can be differentiated.
   - This will allow tracking of a users nutritional history which can then be analyzed to give users nutritional advice.
2. Once the previous feature is added, I want to add something to the food tracking html that will pull a users history from the database and then display it to them in a table or perhaps different graphs or plots.
3. Another feature that we planned to add was connecting the food tracking page to the food lookup page so that users didn't have to find and input the nutritional values of food on their own but could instead use the nutritional values already present in our database.


### Food Lookup and Add Food 

#### What Was Completed: 

- Food Lookup:
     - A page for a user to search the foods table for existing items, receive auto-populated, clickable suggestions matching what they type into the search bar, and nutritional information (as would be found on a food nutritional label) on-click of a food item found within the database, and a message displaying that a food item could not be found by name within the database if such a match with the database could not be found matching the user's input string. A link to the add food page is available if a user wants to add a food item to the database, and links to the other pages of the project are also included on the page. 
- Add Food:
     - A page for a user to add food items to the backend database, with an input field for each item in the foods table (name of the item (REQUIRED), and all nutritional values as found on a nutritional label, which are all optional). A submit button is included, and error messages pop up on screen if inserting a food item does not work. Pre-filtering error messages display if a user inputs an invalid value for the name field (such as one containing numbers or special characters), and technical, SQL-related error messages are displayed for entering other invalid values (such as a duplicate name, which violates the UNIQUE constraint on the name field in the foods table). A link to return the user back to food_lookup is included on the bottom of the page.

#### In-progress implementation: 

- Detecting errors in input was not completely finished, as evidenced by the technical flash messages appearing to the user upon some invalid inputs - these could have been matched to more user-friendly error messages for those unfamiliar with SQL. 

#### Future plans: 

- More input validation and security measures should be implemented to prevent SQL injection attacks. Better-looking frontend features and design should be completed for a better, cleaner look. Integrating these pages more closely with the user/login features could help give rise to other pages/features such as pages for administrators to query the database, delete the database, or delete problematic items, as well as having a user be able to see what they have added to the database, or being able to log specific food items eaten (would require integration with the food/calorie tracker as well). Documentation and testing of these pages should be improved. 

#### Known problems

- No known issues besides the technical flash messages being displayed on screen for the user, which should be altered to more user-friendly messages. Exhaustive unit-testing was not conducted, so unknown errors or issues remain a concern. 
