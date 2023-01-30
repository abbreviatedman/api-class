import json

from flask import Flask, request

app = Flask(__name__)

def get_data_from_json(filename):
    """A helper function for reading from a JSON file.

    Takes a file path as its lone argument.

    Returns the JSON converted to a Python list or dictionary.
    """
    with open(filename) as file:
        return json.load(file)


def post_data_to_json(filename, data):
    """A helper function for writing to a JSON file.

    Takes a file path as its first argument.

    Takes a value to be added to the JSON file as its second argument

    Does not return a value. (Besides the Python default value `None`.)

    NOTE: this will overwrite the data in the file. Be sure to include the old
    data in your argument to this function.  (A backup copy of both files has
    been provided. Copy one over should you need it. Do not write to the
    backups.)
    """
    with open(filename, "w") as file:
        json.dump(data, file, indent=2)

@app.get("/characters")
def get_characters():
    return get_data_from_json("characters.json")

@app.get("/characters/<string:id>")
def get_character(id):
    characters = get_data_from_json("characters.json")
    for index, character in enumerate(characters):
        if character["id"] == int(id):
            return character

    return 404

@app.post("/characters")
def add_character():
    request_data = request.get_json()
    characters = get_data_from_json("characters.json")
    characters.append(request_data)
    post_data_to_json("characters.json", characters)

    return request_data, 201

