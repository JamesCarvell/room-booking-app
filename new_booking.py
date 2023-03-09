# Reads json data file, takes user input in terminal for a new booking, updates json and writes over whole file.
import json


def create_new_booking(database, new_booking):
    with open(database, "r+") as db:
        data = json.load(db)
        data.update(new_booking)
        json.dump(data, db, indent=2)
