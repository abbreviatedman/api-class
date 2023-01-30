<!-- splash-page -->

# API Architectures

## What Differentiates REST

---

## Questions We'll Ask

And answer!

- **What** Are The Different API Architectures?
- **How** Do They Differ?
- **Why** Do People Choose REST?

---

<!-- splash-page -->

# Major API Architectures

---

- REST (the most common)
- SOAP
- RPC

---

## RPC

Remote Procedure Call

- Created in 1998.
- Is built around calling functions on a server.

Pros:

- High performance.
- Easy to change.

---

## RPS Is Used:

- When speed and low bandwidth are the #1 priorities
- When being user-friendly to multiple clients is not.

---

## SOAP

- Started by Microsoft in 1999.
- Focused on sending highly standardized XML data (NOT functions).

Pros:

- Server is more decoupled from clients. They can grow separately.
- Highly secure and handles errors gracefully.

---

## SOAP Is Used:

SOAP is often used in areas where:

- security is of the utmost concern
- speed of transaction and future-proof portable design less important

A great example of this is finance.

---

## REST

- Started in 2000 from a research paper.
- Can be used to send any data (json now most popular)

Pros:

- Better performance than SOAP (XML is heavy on the bandwidth)
- Decoupling and simple standards allow for easily adding new clients.

--- 

## REST Is Used:

Pretty much everywhere else!

Its future-proof modularity and simple, user-friendly architecture makes it perfect for most public APIs.

---

## We've Already Made A REST API!

Our command line API meets most of the requirements for REST.

REST APIs do NOT have to:

- be connected to a database (but usually are)
- be accessed over HTTP (but again usually are)
- be tied to JSON (and many aren't)

---

## Architectural Constraints

What makes a REST API?

1. Client-Server Relationship
2. Uniform Interface
3. Statelessness
4. Caching
5. Layered System
6. Code On Demand (optional)

Let's go into some detail on each.

---

## Client-Server Relationship

This just means that a separate app handles the API. It is not bundled into the overall app.

Most APIs do this, not just REST.

---

## Uniform Interface

REST is built around verbs and nouns. This makes it:

- Easy to reason about. Taking actions on resources (verb and noun) is how humans think anyway.
- Easy to go from one API to another. The grammar is very portable.

As a result, if you've used a REST API before, you are 80% of the way to understanding how to use the next one.

---

## Statelessness

REST insists that the API program itself has no state of its own.

- The client manages its own state.
- The database state is separate as well (though accessible and changeable).

This means that no call to the API changes the API itself in any way.

---

## Caching

REST's statelessness means that more network calls happen than in SOAP or RPC.

Caching requests helps to minimize this.

Note that not _every_ REST API implements caching (though they should!).

We still (usually) call them RESTful, even if they don't.

---

## Layered System

Every layer only talks to its neighbor.

The simplest example of this is that the client can _not_ access the database except through the API.

Every layer is an intermediary, providing modularity, separation of concerns, and loose coupling.

--- 

## Code On Demand

This optional architectural restraint encourages REST APIs to send links as data.

This restraint is outside our scope for this course, and most REST APIs don't provide it at all.

But Code on Demand is fascinating to read up on.

---

## What's Next

We're going to dive into making our API work  over HTTP using the Python library Flask.

<!-- ending-splash-page -->

# Let's Get Coding!
