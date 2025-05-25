# FRDB - Flask Relational Database Project

## INTRO

Simple API using python flask

FRDB is a Flask-based web application that provides a platform for user registration, authentication, and social interactions such as creating tweets, liking tweets, commenting, and following other users. The project uses SQLAlchemy for database management and Flask-Login for user session handling.

## Features

- User registration and login
- Create, like, and comment on tweets
- Follow and unfollow users
- View followers and followings
- RESTful API endpoints for all operations
- SQLite database for local storage
- Faker integration for generating test data

## Project Structure

```
.env
.gitignore
app.py
config.py
handler.py
models.py
requirements.txt
routes.py
docs/
instance/
test/
```

### Key Files and Directories

- **`app.py`**: The main entry point of the application. Initializes the Flask app, database, and routes.
- **`config.py`**: Contains configuration settings for the application, including the database URI and secret key.
- **`handler.py`**: Contains functions to handle various API operations such as user registration, login, and tweet management.
- **`models.py`**: Defines the database models for users, tweets, comments, likes, and followers.
- **`routes.py`**: Defines the API endpoints and their corresponding handlers.
- **`requirements.txt`**: Lists the Python dependencies required for the project.
- **`test/`**: Contains scripts for testing and generating data, including `run.py` for automated user and tweet creation.
- **`docs/`**: Documentation files, including API endpoint details.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sonalvijit/FRDB.git
   cd FRDB
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the environment variables:
   - Create a `.env` file in the root directory.
   - Add the following content:
     ```
     PORT=4300
     ```

5. Run the application:
   ```bash
   python app.py
   ```

## Usage

### API Endpoints

Refer to the [API Documentation](docs/api/endpoints.md) for details on available endpoints, request formats, and responses.

### Testing

The `test/run.py` script can be used to generate test data and simulate user interactions:
```bash
python run.py
```

## Technologies Used

- **Backend**: Flask, Flask-SQLAlchemy, Flask-Login
- **Database**: SQLite
- **Testing and Data Generation**: Faker
- **Authentication**: Flask-Login
- **Other Libraries**: Werkzeug, dotenv

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push them to your fork.
4. Submit a pull request.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Faker](https://faker.readthedocs.io/)
