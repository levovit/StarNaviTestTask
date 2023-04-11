# StarNavi Test Task (by Vitalii Melnychuk)

This project is a simple social network API built using FastAPI and SQLAlchemy based on this test task:
https://drive.google.com/file/d/1lRoKVkBTtQDdNB1Zwaa0tyJS0wkR7iT1/view

Key features:

- User authentication and registration
- Post creation and retrieval
- Liking and unliking posts
- User activity analytics
- Post analytics
- Integration with a Telegram bot

The API is designed to be easy to set up and use, making it an ideal starting point for developers who want to learn more about building web applications with FastAPI and SQLAlchemy.


## Table of Contents

1. [Getting Started](#getting-started)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Running the Application](#running-the-application)
5. [Running the Tests](#running-the-tests)
6. [API Documentation](#api-documentation)
7. [Telegram Bot](#telegram-bot)
8. [Technologies Used](#technologies-used)
9. [Acknowledgments](#acknowledgments)

## Getting Started

These instructions will guide you through the process of setting up the project on your local machine for development and testing purposes.

### Prerequisites

Before you can run the project, you need to have the following software installed on your machine:

- Docker
- Docker Compose
- Python 3.11

### Installation

1. Clone the repository:
```bash
git clone https://github.com/levovit/StarNaviTestTask.git
```
2. Change the current working directory to the project's root:
```bash
cd StarNaviTestTask
```
3. Create a `.env` file in the project's root directory and add your environment variables:
```bash
touch .env
```
Example of `.env` file content:
```env
DB_USER=myuser
DB_PASSWORD=mypassword
DB_NAME=mydb
DB_PORT=5432

SECRET_KEY=mysecretkey

TELEGRAM_API_KEY=<Telegram Bot Token>
NUMBER_OF_USERS=3
MAX_LIKE_PER_USER=8
MAX_POSTS_PER_USER=6
```
## Running the Application

To run the application, execute the following command:

```env
docker-compose up --build --scale test=0
```
The API will be available at `http://localhost:8000`.

## Running the Tests

To run app with tests, execute the following command:

```env
docker-compose up --build
```
Tests will be executed automatically before the main container starts.
## API Documentation

Once the application is running, you can access the interactive API documentation at `http://localhost:8000/docs`.

## Telegram Bot

The Telegram bot interacts with the API and allows users to perform various actions. To run the bot, you'll need to have the `TELEGRAM_API_KEY` in your `.env` file.

After running the application, bot will start working automatically

### Bot Usage

1. Start a conversation with the bot in Telegram.
2. Use the bot's commands to interact with the API.
3. Use /start command to reset keyboard

### Ready bot
If you don't want to create telegram bot you can test mine: 
[@starnavi_levovit_bot](https://t.me/starnavi_levovit_bot)

## Technologies Used

This project utilizes the following technologies:

- **Python**: Main programming language used for writing the application logic.
- **FastAPI**: Modern, high-performance web framework for building API, used for building the web application.
- **Docker**: Containerization platform used to build, package, and distribute the application.
- **Docker Compose**: Tool for defining and running multi-container Docker applications, used to manage the services and their dependencies.
- **Uvicorn**: ASGI server used to serve the FastAPI application.
- **SQLAlchemy**: Object-relational mapping (ORM) library used for database operations within the Flask application.
- **PostgreSQL**: Relational database management system used for storing the application data.
- **SQLite**: Lightweight database engine used for testing.
- **Alembic**: Database migration tool used to manage schema changes for the SQLAlchemy ORM.
- **pytest**: Testing framework used for writing and running tests for the application.
- **PyTelegramBotAPI**: Python library used to interact with the Telegram Bot API and manage the Telegram bot functionality.
- **Git**: Version control system used for tracking changes in the project's source code.
- **NGINX**: Web server and reverse proxy server for serving the static files and forwarding requests to the FastAPI application.
- **Google Cloud**: Cloud computing platform used for deploying and hosting the application.
- **Flake8**: A Python linting tool that checks for PEP 8 compliance and other code quality issues.
- **Black**: A Python code formatter that automatically formats code to a consistent style.


## Acknowledgments
* Special thanks to StarNavi company for this opportunity. It was a pleasure to create this project
