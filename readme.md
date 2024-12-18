Polinomic
Polinomic is a country information management system built with Django as the main framework, Celery for task management, Redis as a message broker, PostgreSQL for database management, and restcountries.com for fetching country information.

Table of Contents

Installation
Creating the Database
Running the Project
Docker Setup
API Endpoints
Scheduled Tasks


Installation
Clone the repository and navigate to the project folder:

git clone https://github.com/matibraun/countries.git
cd countries


Creating the Database
Set up a PostgreSQL database instance with the following parameters:

Host: 0.0.0.0
Port: 5432
Database Name: polinomic
Username: postgres
Password: postgres


Running the Project
Start the application using Docker:

docker-compose up --build

This command will build the necessary containers and start Django, PostgreSQL, Redis, and Celery workers all at once. Migrations will be automatically applied inside the Docker container.

To stop the application, use the following command:

docker-compose down


API Endpoints
The following endpoints can be tested using Postman or a browser:

Fetch and save country data to the database:
POST http://localhost:8000/country/countries/

List all country information:
GET http://localhost:8000/country/countries/

Retrieve specific country information:
GET http://localhost:8000/country/countries/<id>/


Scheduled Tasks
The application is configured to fetch country information and save it to the database automatically every hour.

