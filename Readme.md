# StarNavi Test Task (by Vitalii Melnychuk)

This project is a simple social network API built using FastAPI and SQLAlchemy

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
8. [Acknowledgments](#acknowledgments)

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
4. Build the Docker images:
```env
docker-compose build
```
## Running the Application

To run the application, execute the following command:

```env
docker-compose up
```
The API will be available at `http://localhost:8000`.

## Running the Tests

To run the tests, execute the following command:

```env
docker-compose --profile=test up --build
```
## API Documentation

Once the application is running, you can access the interactive API documentation at `http://localhost:8000/docs`.

## Telegram Bot

The Telegram bot interacts with the API and allows users to perform various actions. To run the bot, you'll need to have the `TELEGRAM_API_KEY` in your `.env` file.

After running the application, bot will start working automatically

### Bot Usage

1. Start a conversation with the bot in Telegram.
2. Use the bot's commands to interact with the API.


## Acknowledgments
* Thank the StarNavi company for this chance. It was fun to create this project
