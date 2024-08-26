# Simple PostgreSQL UI with Tkinter

This project is a simple graphical user interface (GUI) for interacting with a PostgreSQL database using Tkinter in Python.

## Features

- Connect to a PostgreSQL database
- Insert, update, and delete records
- Simple and intuitive interface

## Requirements

- Python 3.6 or higher
- Tkinter (usually included with Python)
- psycopg2 (PostgreSQL adapter for Python)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/jeevan251203/GUI_For_PostgreSQL.git
    ```

2. Install the required Python packages:
    ```sh
    pip install psycopg2
    ```
3. Make sure to install and setup PostgreSQL before running

## Usage

1. Ensure your PostgreSQL server is running and accessible.
2. Update the database connection settings in `config.py`:
    ```python
    DB_HOST = 'localhost'
    DB_PORT = '5432'
    DB_NAME = 'your_database'
    DB_USER = 'your_username'
    DB_PASSWORD = 'your_password'
    ```

3. Run the application:
    ```sh
    python main.py
    ```

## License

This project is licensed under the MIT License.
