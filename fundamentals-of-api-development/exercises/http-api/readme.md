# HTTP API Exercise

## Setup

### Make Sure You've Done The Initial Setup

Our [initial setup doc](../../../computer-setup/readme.md) has everything you need.

### Fork and Clone the Course Git Repo

Skip this step if you've already done it.

- Fork this repo on GitHub: https://www.github.com/abbreviatedman/api-class
- Clone it to your local machine. `git clone [url from the GitHub repo page, SSH or HTTPS per your setup]`

### Navigate To The Course Repo Directory

If you've just cloned it:

- `cd api-class`

If you can't find it, clone it again from the previous set of steps.

### Navigate To The Exercise

- `cd api-class/fundamentals-of-api-development/exercises/http-api`

### Create And Activate Our Python Environment

- Create the environment. `conda env create -f environment.yml`
- Activate it. `conda activate api-class-flask-env`

### Open The Directory In Your Local Editor

If using VS Code, simply type `code .` on the command line.

## The Flask Server


### Running The Server

To run the server: `flask --debug run`

The `--debug` flag is optional but highly recommended during development—it will re-start the server when changes are made.

To run the server on a different port (if the default port 5000 is already in use): `flask --debug run --port [new port number]`

For example: `flask --debug run --port 5001`

### Hitting Up The Server

For GET requests, you can simply use your browser and hit up our endpoints. For example:

`http://127.0.0.1:5000/quotes`

For other HTTP verbs (such as POST), we recommend Postman, as it's the industry-standard tool. You can download it from app stores, command line repositories, or directly from [Postman's website](https://www.postman.com/downloads)

## Writing A Simple Route

With Flask, you declare which Python functions will be called from which endpoints. You do that with a Python decorator from Flask.

### Setup

Make sure this is near the top of your file:

```python
from flask import Flask, request

app = Flask(__name__)
```

You can skip importing `request` if only handling GET requests.

### A Simple Route

If you wanted the data "Hello, World!" to be returned when the user hit the endpoint `/hey`, you would write the following Python:

```python
@app.get("/hey")
def say_hi:
    return "Hello, World!"
```

The `@app.get` Python decorator is used by Flask to identify which endpoint (given as an argument to `@app.get`) will cause the function immediately following it to execute. Its return value is then sent back by the Flask server as a response to the client.

## Now Let's Write More Complex Routes!

### Exercise Layout

This exercise uses the same data and data files as the previous exercise.

### Specifications

See if you can create the following routes:

- `GET /characters` - returns all characters.
- `GET /quotes` - returns all quotes.
- `GET /characters/{id}` - returns the character with the matching `id` field. For example, `GET /characters/3`
- `GET /quotes/{id}` - returns the quote with the matching `id` field.
- `POST /characters` - adds a new character to the JSON file, returning the created character
- `POST /quotes` - adds a new character to the JSON file, returning the created character

### Tips

#### Returning Values

#### Loops

Both the Characters and Quotes files contain lists. The easiest way to 
#### IDs

For getting a particular id, you can use a decorator like the following:

```python
@app.get("/characters/<string:id>")
def some_function_name(id):
```

Flask will pass in the part of the route after `/characters/` to the matching parameter in your function.

So a request to `GET /characters/4` will result in `"4"` passed in as the value for `id` in your function.
 
#### POST Bodies

The POST routes are tricky, but the data sent in the body of the request will be accessible on the imported `request` object. If you call `request.get_json()`, you will get the JSON that was sent in the request, converted to Python for you.

