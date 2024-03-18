# Todo Application

This project implements a Todo application using FastAPI, Neon Database, and SQLModel ORM.

## Features

- Create new todo items
- Read existing todo items
- Update todo items
- Delete todo items

## Technologies Used

- FastAPI
- PostgreSQL
- SQLModel ORM
- Poetry (for Python virtual environment)

## Setup Instructions

1. Clone the repository.
2. Install Poetry (if not already installed): `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -`
3. Navigate to the project directory.
4. Install the required dependencies using Poetry: `poetry install`.
5. Set up a PostgreSQL database and update the database connection URL in the `.env` file.
6. Run the application using Poetry: `poetry run uvicorn main:app --reload`.

## API Documentation

The API documentation can be found at `http://localhost:8000/docs` after running the application.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
