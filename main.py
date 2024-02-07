import sqlite3


conn = sqlite3.connect('tv_shows.db')
cursor = conn.cursor()

def add_show():
    # Prompt the user for input
    title = input("Enter the title of the TV show: ")
    genre_id = int(input("Enter the genre ID of the TV show: "))
    rating = float(input("Enter the rating of the TV show: "))

    # Execute SQL statement to insert the new show into the database
    cursor.execute("INSERT INTO shows (title, genre_id, rating) VALUES (?, ?, ?)", (title, genre_id, rating))
    conn.commit()
    print("TV show added successfully!")


def view_shows():
    # Execute SQL query to select all rows from the shows table
    cursor.execute("SELECT * FROM shows")
    
    # Fetch all rows and print them
    rows = cursor.fetchall()
    if rows:
        print("ID\tTitle\tGenre ID\tRating")
        for row in rows:
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")
    else:
        print("No shows found in the database.")


def update_show():
    # Prompt the user for the ID of the show they want to update
    show_id = int(input("Enter the ID of the show you want to update: "))
    
    # Check if the show exists in the database
    cursor.execute("SELECT * FROM shows WHERE id = ?", (show_id,))
    row = cursor.fetchone()
    if row:
        # Prompt the user for the new values of the show attributes
        title = input("Enter the new title of the TV show (leave blank to keep current): ")
        genre_id = input("Enter the new genre ID of the TV show (leave blank to keep current): ")
        rating = input("Enter the new rating of the TV show (leave blank to keep current): ")

        # Update the show with the new values
        update_query = "UPDATE shows SET"
        params = []
        if title:
            update_query += " title = ?,"
            params.append(title)
        if genre_id:
            update_query += " genre_id = ?,"
            params.append(genre_id)
        if rating:
            update_query += " rating = ?,"
            params.append(rating)
        # Remove the last comma
        update_query = update_query.rstrip(",")
        update_query += " WHERE id = ?"
        params.append(show_id)
        
        # Execute the update query
        cursor.execute(update_query, tuple(params))
        conn.commit()
        print("TV show updated successfully!")
    else:
        print("TV show with ID", show_id, "not found in the database.")


def delete_show():
    # Prompt the user for the ID of the show they want to delete
    show_id = int(input("Enter the ID of the show you want to delete: "))
    
    # Check if the show exists in the database
    cursor.execute("SELECT * FROM shows WHERE id = ?", (show_id,))
    row = cursor.fetchone()
    if row:
        # Execute the delete query
        cursor.execute("DELETE FROM shows WHERE id = ?", (show_id,))
        conn.commit()
        print("TV show deleted successfully!")
    else:
        print("TV show with ID", show_id, "not found in the database.")





command = int(input("Enter 1 for add, 2 view, 3 for update, 4 for delete, 0 for exit: "))
while(command != 0):
    if command > 4 or command < 0:
        print("Invalid input Please try again")
        command = int(input("Enter 1 for add, 2 view, 3 for update, 4 for delete, 0 for exit: "))
    elif command == 1:
        add_show()
    elif command == 2:
        view_shows()
    elif command == 3:
        update_show()
    else:
        delete_show()
    
    command = int(input("Enter 1 for add, 2 view, 3 for update, 4 for delete, 0 for exit: "))

conn.close()

print("all done!")