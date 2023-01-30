<!-- splash-page -->

# API Architectures

## What Differentiates REST

---

## The Language Of REST

Let's talk about what most identifies and differentiates REST when you're first discovering it. One of its main architectural constraints:

**Uniform Interfaces**

---

## REST Grammar

The structure of a REST url is what gives a REST API a short learning curve.

Most REST urls closely follow this pattern:

`www.[domain-name].com/[plural-noun]`

- `www.swapi.tech/api/planets`
- `https://api.humorapi.com/memes`
- `http://www.thebookapi.com/authors`

---

## This Is Like A Filename

Called a "resource", each of these plural nouns is a collection of one type of thing. Planets, memes, authors, transactions, etc.

But how does the API know what we want to _do_ with that collection of data?

---
## Nouns and Verbs

The next piece of the puzzle is what's called an HTTP Verb.

It's a part of each network request an app makes to an API. The most common ones are:

`GET` - "send me back resource(s)"
`POST` - "create a new item in this resource collection"
`DELETE` - "remove this resource from the collection"
`PATCH` - "update this resource in the collection"

---

## Putting Them Together

`GET /characters` - send me all the characters
`POST /quotes "Magicians are cool, huh"` - add this quote to the quotes collection.
