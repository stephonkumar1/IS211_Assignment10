#Stephon Kumar

import sqlite3  # Import SQLite library for database operations

# Data to load into the database
person_data = [
    (1, 'James', 'Smith', 41),  # Person ID, First Name, Last Name, Age
    (2, 'Diana', 'Greene', 23),
    (3, 'Sara', 'White', 27),
    (4, 'William', 'Gibson', 23)
]

pet_data = [
    (1, 'Rusty', 'Dalmation', 4, 1),  # Pet ID, Name, Breed, Age, Dead Status (1 = Dead, 0 = Alive)
    (2, 'Bella', 'Alaskan Malamute', 3, 0),
    (3, 'Max', 'Cocker Spaniel', 1, 0),
    (4, 'Rocky', 'Beagle', 7, 0),
    (5, 'Rufus', 'Cocker Spaniel', 1, 0),
    (6, 'Spot', 'Bloodhound', 2, 1)
]

person_pet_data = [
    (1, 1),  # Person ID, Pet ID relationship
    (1, 2),
    (2, 3),
    (2, 4),
    (3, 5),
    (4, 6)
]

if __name__ == "__main__":
    print("Running load_pets.py")  # Notify script is running
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('pets.db')  # Open connection to pets.db
        cursor = conn.cursor()  # Create a cursor object for executing SQL queries

        # Insert data into the 'person' table
        cursor.executemany("INSERT INTO person (id, first_name, last_name, age) VALUES (?, ?, ?, ?)", person_data)
        print("Inserted data into 'person' table.")  # Confirm data insertion

        # Insert data into the 'pet' table
        cursor.executemany("INSERT INTO pet (id, name, breed, age, dead) VALUES (?, ?, ?, ?, ?)", pet_data)
        print("Inserted data into 'pet' table.")  # Confirm data insertion

        # Insert data into the 'person_pet' table
        cursor.executemany("INSERT INTO person_pet (person_id, pet_id) VALUES (?, ?)", person_pet_data)
        print("Inserted data into 'person_pet' table.")  # Confirm data insertion

        # Commit changes and close the connection
        conn.commit()  # Save changes to the database
        print("Data loaded successfully!")  # Notify success
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")  # Print any database error
    finally:
        conn.close()  # Close the database connection
