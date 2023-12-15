# Team 3 Fitness/App Tracker Final Report

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
Force Rebuild: https://api.render.com/deploy/srv-clp7v89oh6hc73buj3n0?key=5Zu3lRKyBwA

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
