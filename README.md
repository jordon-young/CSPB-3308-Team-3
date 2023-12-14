# CSPB 3308 Team 3 

Team repository for our CSPB 3308 project.

| Team Member | Github Username |
| :---: | :---: |
| **William Barber** | wjbarberjr | 
| **Eric Hernandez** | EWHernandez |
| **William Hinkley** | WiHi1131 |  
| **Dylan Smith** | dylan33smith |
| **Jordon Young** | jordon-young |
        
Weekly meetings Thursdays 5:30 MST via Discord.

## Project: Exercise Tracker App

#### Vision Statement: What would you tell potential customers?

- Track your fitness and have fun while doing it. 

#### Motivation: Why are you working on this project?

- To promote a positive relationship with exercise and create a tool that is fun and keep users motivated.

#### Risks to Project Completion

- Time constraints on building the functionalities we want to incorporate
- poorly defined goals and what they entail
- lack of back end development experience

#### Development Method

- Scrum
    - Agile development
    - Weekly sprints
    - Rotate scrum masters every two weeks
- Project Management Software: [Todoist](https://todoist.com/)
    - Track task status in kanban-style view
    - Use task description, assignee, priority, and due dates
    - Comment on ticket and push notifications to team for blockers
- Discord for General Communication and Meetings

### How to Run

1. Use VS Code
2. Download the [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) extension
3. In the toolbar at the bottom of VS Code, click "Go Live"
4. View that the server opened in browser and the html displays

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
