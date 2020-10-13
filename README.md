# theScore "the Rush" Interview Challenge
At theScore, we are always looking for intelligent, resourceful, full-stack developers to join our growing team. To help us evaluate new talent, we have created this take-home interview question. This question should take you no more than a few hours.

**All candidates must complete this before the possibility of an in-person interview. During the in-person interview, your submitted project will be used as the base for further extensions.**

### Why a take-home challenge?
In-person coding interviews can be stressful and can hide some people's full potential. A take-home gives you a chance work in a less stressful environment and showcase your talent.

We want you to be at your best and most comfortable.

### A bit about our tech stack
As outlined in our job description, you will come across technologies which include a server-side web framework (like Elixir/Phoenix, Ruby on Rails or a modern Javascript framework) and a front-end Javascript framework (like ReactJS)

### Challenge Background
We have sets of records representing football players' rushing statistics. All records have the following attributes:
* `Player` (Player's name)
* `Team` (Player's team abbreviation)
* `Pos` (Player's postion)
* `Att/G` (Rushing Attempts Per Game Average)
* `Att` (Rushing Attempts)
* `Yds` (Total Rushing Yards)
* `Avg` (Rushing Average Yards Per Attempt)
* `Yds/G` (Rushing Yards Per Game)
* `TD` (Total Rushing Touchdowns)
* `Lng` (Longest Rush -- a `T` represents a touchdown occurred)
* `1st` (Rushing First Downs)
* `1st%` (Rushing First Down Percentage)
* `20+` (Rushing 20+ Yards Each)
* `40+` (Rushing 40+ Yards Each)
* `FUM` (Rushing Fumbles)

In this repo is a sample data file [`rushing.json`](/rushing.json).

##### Challenge Requirements
1. Create a web app. This must be able to do the following steps
    1. Create a webpage which displays a table with the contents of [`rushing.json`](/rushing.json)
    2. The user should be able to sort the players by _Total Rushing Yards_, _Longest Rush_ and _Total Rushing Touchdowns_
    3. The user should be able to filter by the player's name
    4. The user should be able to download the sorted data as a CSV, as well as a filtered subset
    
2. The system should be able to potentially support larger sets of data on the order of 10k records.

3. Update the section `Installation and running this solution` in the README file explaining how to run your code

### Submitting a solution
1. Download this repo
2. Complete the problem outlined in the `Requirements` section
3. In your personal public GitHub repo, create a new public repo with this implementation
4. Provide this link to your contact at theScore

We will evaluate you on your ability to solve the problem defined in the requirements section as well as your choice of frameworks, and general coding style.

### Help
If you have any questions regarding requirements, do not hesitate to email your contact at theScore for clarification.

### Installation and running this solution
This web application uses [Python 3](https://www.python.org/downloads/) for the backend service and [VueJS v2](https://vuejs.org/v2/guide/installation.html) as the frontend framework.

#### Prerequisites
- The web application uses [Docker](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/install/) to containerize and run the images as individual services.

#### Set up
1. Ensure you are in the root directory of the project.
2. Build both backend and frontend applications into containers using the provided  bash script - `sh build_docker_images.sh`
3. Start both applications through Docker Compose - `docker-compose up` or `docker-compose up -d` to run it in detached mode.
4. Navigate to your [localhost on port 8080](http://localhost:8080/) to view the dashboard.

### Miscellaneous

#### Assumptions
- The backend Python service currently only hosts a GET request endpoint which returns the JSON data from the `rushing.json` file within the request payload. In an actual production environment, I would assume that the route would instead be pulling the data from a database server. However, for the sake of simplicity for this assignment, I did not set up a database and load the JSON data into a table.
- I have admittedly made some changes to the original data set. These changes involved updating some of the "Yds" values from string to integer types. I believe this situation occured when the "Yds" value met or exceeded `1000`, which then added a comma (`1,000`) and converted it into a string. I updated those values >1000 by removing the comma and converting it back into an int. I have made the assumption that in a production level environment, the data should have been validated and sanitized before being stored into the database.


#### Notes
- The current logic for the frontend is to call the API endpoint and load the entire dataset into memory. This has been tested to work well at the current scope of 326 players as well as a scaled up 10K players. However, if we were expecting to deal with a larger dataset, say in the hundreds of thousands in the future, I would update the logic of the API call to return the data in chunks and set up serverside pagination for the data so the frontend does not have to load huge amounts of data into memory.
- Though I used Gunicorn to replace Flask's built in HTTP server and installed Node's `http-server` package and are a step better than a development setup, neither has been completely optimized for production level usage.




