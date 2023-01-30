# The Magicians Local API Exercise

# Your task: create a command-line app to serve as an API to the data in `characters.json` and `quotes.json` (partial data from the TV show The Magicians).

# Please read the following specifications and note the helper functions given
# to you already.  Your job should boil down to the logic required to follow
# the specifications, with a minimum of Python-specific gotchas.

# Don't worry about error handling, input validation, or any of those
# (genuinely vital) tasks. This will never be a production app!
#
# (If it is, blame your instructor for the technical debt accrued.)


# NOTE: handling POST requests is a bonus specification. Handle GET first!

# Specifications
#
# This program will print to the console the resource or resources requested by
# the user, according to the command-line arguments the user gives.
#
# The user will request data in the following command-line format:
# python main.py action data [index]
#
# `action` can be one of the following strings:
# "GET" || "POST"
#
# `data` can be one of the following strings:
# "characters" || "quotes"
#
# `index` is an OPTIONAL argument for GET requests. Its presence indicates that
# the user wants a single element from the list, the element at the index
# `index`.
#
# NOTE: like all command-line arguments, this will come in as a string as well.
# You MAY need to convert it to an integer.
#
# EXAMPLE:
# If the user enters `python main.py GET quotes 1`, the following quote should be printed to the console:
# {'episode': 'Unauthorized Magic', 'explicit': False, 'id': 1, 'lines': [{'speaker': 'Quentin', 'line': 'And, honestly, they probably take anyone conscious for philosophy.'}, {'speaker': 'Julia', 'line': 'For philosophy, "conscious" is a detriment.'}]}

# BONUS Specifications:
#
# 1. Instead of looking up a single resource (quote or character) by index,
# print the resource with the matching `id` property.
#
# 2a. Implement logic for handling a POST request. This will have a different
# command-line format:
# python main.py POST quotes new_quote
#
# `new_quote` will be a python dictionary, wrapped in double quotes, as in the
# following example:
# python main.py POST quotes "{'episode': 'Fundamentals of API Development', 'explicit': false, 'lines': [{'speaker': 'Colin', 'line': 'Example quote!'}]}"
#
# A POST request should have two results: the new quote should be printed to the
# console, and the JSON file for the request (quotes.json or characters.json)
# should be modified.
#
# 2b. Add an `id` field to the new resource. Make sure it does not already
# belong to an existing resource.

# BUILT IN CODE. Don't touch the below!

# Import required libraries.
import sys
import json


# The arguments from the command line.
arguments = sys.argv[1::]

# `arguments` should now be a list of command-line arguments.   If the user
# enters `python main.py the command line is cool.` on the command line,
# `arguments` will be a list of four items, like so:
#
# ["the", command", "line", "is", "cool."]


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


# YOUR CODE GOES BELOW

# TIPS:
#
# You can use more advanced architecture, but if/elif/else chains are totally
# fine for an exercise.
#
# Don't forget case sensitivity!
#
# If you're unused to Python, some quick internet research should uncover how
# to append strings, convert strings to numbers, add to a list (what Python
# calls arrays), etc.
