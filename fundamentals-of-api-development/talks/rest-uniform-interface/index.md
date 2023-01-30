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

The next aspect of the language is what's called an HTTP verb.

The HTTP verb a part of each network request an app makes to an API. The most common ones are:

`GET` - "send me back resource(s)"
`POST` - "create a new item in this resource collection"
`DELETE` - "remove this resource from the collection"
`PATCH` - "update this resource in the collection"

---

## Putting Them Together

`GET /characters` - "send me all the characters"
`GET /quotes` - "send me all the quotes"

---

## Targeting One Item

We can extend the noun (url) slightly to target a specific item.

The typical way to do that is to identify _which_ item we want to interact with by adding it to the end of  the URL.

`GET /quotes/8` - "give me the quote with the `id` 8"
`DELETE /character/Quentin` - "delete the character with the name Quentin".

## Adding New Information

Typically, a `POST` or `PATCH` request needs more information—what's the new resource to add, or what needs to change in the updated item?

This info can't easily be put into an HTTP verb or a URL, so it's typical to add it as part of a request.

`POST /quotes` with `{"line": "Magicians are cool, huh"}` in the "request body" - "add this quote to the quotes collection."
`PATCH /characters/3` with `{"name": "Colin"}` in the "request body" - "Change the attribute name to be 'Colin' in the character with the `id` of 3."
