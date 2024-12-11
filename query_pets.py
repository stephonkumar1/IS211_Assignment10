#Stephon Kumar

import sqlite3  # Import SQLite library for database operations

def fetch_person(cursor, person_id):
    """Fetch and return person details by ID."""
    # Execute SQL query to get person details
    cursor.execute("SELECT first_name, last_name, age FROM person WHERE id = ?", (person_id,))
    return cursor.fetchone()  # Return the result of the query

def fetch_person_pets(cursor, person_id):
    """Fetch and return all pets associated with a person."""
    # Execute SQL query to get pet details for a person
    cursor.execute("""
        SELECT pet.name, pet.breed, pet.age, pet.dead
        FROM pet
        JOIN person_pet ON pet.id = person_pet.pet_id
        WHERE person_pet.person_id = ?
    """, (person_id,))
    return cursor.fetchall()  # Return all matching results

if __name__ == "__main__":
    print("Running query_pets.py")  # Notify script is running

    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('pets.db')  # Open connection to pets.db
        cursor = conn.cursor()  # Create a cursor object for executing SQL queries

        while True:
            # Prompt the user for a person's ID
            person_id = input("Enter a person's ID (-1 to exit): ")  # Get user input
            if person_id == '-1':  # Check if user wants to exit
                print("Exiting the program.")
                break  # Exit the loop

            try:
                person_id = int(person_id)  # Convert input to integer
            except ValueError:
                print("Invalid input. Please enter a valid integer ID.")  # Handle invalid input
                continue  # Restart the loop

            # Fetch person details
            person = fetch_person(cursor, person_id)  # Call function to get person details
            if person:
                first_name, last_name, age = person  # Unpack person details
                print(f"{first_name} {last_name}, {age} years old")  # Print person details

                # Fetch and display pets
                pets = fetch_person_pets(cursor, person_id)  # Call function to get pets
                if pets:
                    for pet in pets:  # Loop through each pet
                        pet_name, breed, pet_age, is_dead = pet  # Unpack pet details
                        status = "was" if is_dead else "is"  # Determine alive/dead status
                        print(f"  {first_name} owned {pet_name}, a {breed}, that {status} {pet_age} years old.")
                else:
                    print(f"  {first_name} has no pets.")  # If no pets found
            else:
                print(f"No person found with ID {person_id}.")  # If no person found
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")  # Print any database error
    finally:
        conn.close()  # Close the database connection
