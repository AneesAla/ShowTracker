# TV Shows Database Application

This project is a simple database application for managing TV shows. It allows users to perform CRUD (Create, Read, Update, Delete) operations on TV shows stored in a SQLite database. The application is implemented in Python and utilizes the SQLite3 library for database connectivity.

## Tools and Technologies Used

- Database Management System: SQLite
- Programming Language: Python
- Library for Database Connection: SQLite3 (included with Python)
- Text Editor: Visual Studio Code (or any preferred editor)
- Terminal or Command Prompt for executing commands

## Database Schema

The database consists of two tables:

1. **shows**: Stores information about TV shows.
   - Columns: id (Primary Key), title, genre_id (Foreign Key referencing genres), rating

2. **genres**: Stores information about TV show genres.
   - Columns: id (Primary Key), name

## CRUD Operations

The application supports the following CRUD operations:

1. **Add a Show**: Allows users to add a new TV show to the database.
2. **View Shows**: Allows users to view all TV shows stored in the database.
3. **Update a Show**: Allows users to update information about an existing TV show.
4. **Delete a Show**: Allows users to remove a TV show from the database.

## Getting Started

To set up and use the application, follow these steps:

1. Clone or download the project repository.
2. Ensure you have Python and SQLite installed on your system.
3. Open a terminal or command prompt and navigate to the project directory.
4. Create the SQLite database file (`tv_shows.db`) by running the command `sqlite3 tv_shows.db`.
5. Execute the SQL commands provided in the project documentation to create the database tables.
6. Run the Python script (`tv_shows_app.py`) to interact with the database and perform CRUD operations.

## Next Steps

After completing this project, you may consider the following next steps:

- Adding more features to the application, such as search functionality or user authentication.
- Learning about web frameworks (e.g., Flask or Django) to turn the project into a web application.
- Exploring advanced database concepts and techniques to enhance the functionality and performance of the application.

Feel free to contribute to the project by adding new features, fixing bugs, or improving documentation.

