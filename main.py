import sqlite3

class TVShowDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def add_show(self):
        title = input("Enter the title of the TV show: ")
        genre_id = int(input("Enter the genre ID of the TV show: "))
        rating = float(input("Enter the rating of the TV show: "))
        self.cursor.execute("INSERT INTO shows (title, genre_id, rating) VALUES (?, ?, ?)", (title, genre_id, rating))
        self.conn.commit()
        print("TV show added successfully!")

    def view_shows(self):
        self.cursor.execute("SELECT * FROM shows")
        rows = self.cursor.fetchall()
        if rows:
            print("ID\tTitle\tGenre ID\tRating")
            for row in rows:
                print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")
        else:
            print("No shows found in the database.")

    def update_show(self):
        show_id = int(input("Enter the ID of the show you want to update: "))
        self.cursor.execute("SELECT * FROM shows WHERE id = ?", (show_id,))
        row = self.cursor.fetchone()
        if row:
            title = input("Enter the new title of the TV show (leave blank to keep current): ")
            genre_id = input("Enter the new genre ID of the TV show (leave blank to keep current): ")
            rating = input("Enter the new rating of the TV show (leave blank to keep current): ")
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
            update_query = update_query.rstrip(",")
            update_query += " WHERE id = ?"
            params.append(show_id)
            self.cursor.execute(update_query, tuple(params))
            self.conn.commit()
            print("TV show updated successfully!")
        else:
            print("TV show with ID", show_id, "not found in the database.")

    def delete_show(self):
        show_id = int(input("Enter the ID of the show you want to delete: "))
        self.cursor.execute("SELECT * FROM shows WHERE id = ?", (show_id,))
        row = self.cursor.fetchone()
        if row:
            self.cursor.execute("DELETE FROM shows WHERE id = ?", (show_id,))
            self.conn.commit()
            print("TV show deleted successfully!")
        else:
            print("TV show with ID", show_id, "not found in the database.")

    def close_connection(self):
        self.conn.close()


if __name__ == "__main__":
    db = TVShowDatabase('tv_shows.db')
    while True:
        command = int(input("Enter 1 for add, 2 view, 3 for update, 4 for delete, 0 for exit: "))
        if command == 1:
            db.add_show()
        elif command == 2:
            db.view_shows()
        elif command == 3:
            db.update_show()
        elif command == 4:
            db.delete_show()
        elif command == 0:
            db.close_connection()
            break
        else:
            print("Invalid input. Please try again.")
