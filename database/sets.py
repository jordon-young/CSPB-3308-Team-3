# Sets Functionality

import sqlite3

# Creates the sets table
def create_sets(db, db_filename):
    connection = db.connect(db_filename)
    cursor = connection.cursor()

    cursor.execute(
    """
    CREATE TABLE sets IF NOT EXISTS (
        id INT PRIMARY KEY,
        exercise_group_id INT,
        rep INT,
        weight FLOAT,
        order INT,
        FOREIGN KEY (exercise_group_id) REFERENCES exercise_groups(id)
    );
    """
    )

    connection.commit()
    connection.close()

    

# Creates a set
# Needs parameter for creating category
def create_set(db, db_filename):
    pass

# Populate sets table with dummy data
def populate_sets(db, db_filename):
    pass

# Drop sets table
def drop_sets(db, db_filename):
    pass