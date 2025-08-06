# REST API with FastAPI <!-- omit in toc -->

This repo contains notes and projects of the course [Mastering REST APIs with FastAPI](https://www.coursera.org/learn/packt-mastering-rest-apis-with-fastapi-1xeea/home) on [Coursera](https://www.coursera.org).

- [Module 1: Introduction](#module-1-introduction)
  - [What is an API?](#what-is-an-api)
  - [What is a web API?](#what-is-a-web-api)
  - [What is in a request?](#what-is-in-a-request)
  - [What is REST?](#what-is-rest)
  - [What is a resource?](#what-is-a-resource)
  - [What does stateless mean?](#what-does-stateless-mean)
  - [What does cacheable mean?](#what-does-cacheable-mean)
  - [What does hypermedia-driven mean?](#what-does-hypermedia-driven-mean)
  - [What does multiple servers mean?](#what-does-multiple-servers-mean)
  - [Conclusion](#conclusion)
- [Module 2: Working with FastAPI](#module-2-working-with-fastapi)
- [Module 3: Introduction to pytest](#module-3-introduction-to-pytest)
- [Reference](#reference)


## Module 1: Introduction

### What is an API?

- An API is an **A**pplication **P**rogramming **I**nterface.
  - **Application:** is just code that runs and does somethings.
  - **Programming:** provides instructions to perform a task.
  - **Interface:** defines how things are allowed to interact with each other.
- So, *an API defines how two programes interact with each other.*
- *For example,* the database layer written in `db.py`, which contains functions and methods for database interaction, acts as an interface. The application, written in `app.py`, imports this module to communicate with the database.

### What is a web API?

- A web API defines *how two programes communicate by sending data over the Internet*.
- It's just like the code files but instead of one file asking another to do something, we've got one programe (*client*) asking another program (*server*) to do something. Instead of messages passing happening within a process between two Python files, we've got messages passing happening between two programes.
- Two programes communicate by sending requests.

![API communication](images/api_communication.svg)

### What is in a request?

There're 4 pieces of data in a request:
- **Method**: can be one of many different values like `GET`, `POST`, `PUT`, etc.
  - These values are essentially preset. These methods have meaning to most servers and clients.
  - So, usually servers will repond in a predictable way to each method.
  - *For example*,
    - `GET` method tends to be used to retrieve information.
    - `POST` method tends to be used to create information.
    - `PATCH` method tends to be used to modify an existing bit of information.
  - Some methods have certain restrictions.
  - *For example*, most requests can have a body, some data included in the request, but some methods don't support a body being sent. For instance, we couldn't use the `GET` method to send information to the server because it can't have a body in most cases.
- **Endpoint:** is where the request is sent.
  - *For example*, given an API url `api.com/post?sorting=new`.
    - `api.com`: is a host.
    - `/post`: is an endpoint.
    - `?sorting=new`: `sorting=new` is the `sorting` query string argument with a value of `new`.
      - It's a way to send extra data to the server.
- **Body:** usually is JSON data, used to when the client wants to send an extra information to the server.
- **Header:** is also information in key-value pairs, but the keys tend to have specific meaning.
  - *For example*, `Content-Type`, `Content-Length`, `Date`, etc.
  - Headers are specific key value pairs that mean something.

### What is REST?

REST is a set of architectural constraints.
- Use the concept of **client** and **server**.
- Use the concept of **resource**.
- Be **stateless**.
- Be **cacheable**.
- Have a uniform, hypermedia-driven interface.
- If backend use **multiple servers**, they're invisible to the client.

### What is a resource?

- Resources are *things* that the API deals in, such as: posts, comments, likes, users, etc.
- When the client makes a request, it's a request about a particular resource.
- When the server responds to a request, it does so with a resource representation.

### What does stateless mean?

- The server doesn't keep any information about the clients.
- In every request, the client has to send all the relevant information for the server to understand what's going on.
- The server doesn't remember anything about the client.
- Being stateless makes the server much simpler, much more straightforward to code, and also perform much faster.

### What does cacheable mean?

- If one client makes a request for information, it should be possible for the backend to save that response.
- So, if another client makes a request for the same information, it doesn't have to be recalculated.
- A cache is normally another layer in front of the API that remembers requests and the response that was sent back to that request.

### What does hypermedia-driven mean?

- If a resource is related to another resource, there should be an actual link in the response which allows the client to find the related resources.
- Most APIs don't implement it. It's an optional.

### What does multiple servers mean?

- Sometimes, backends are made up of multiple servers, for example, one for retrieving information, another for user authentication and registration.
- The client shouldn't care about how the backend is organized.

### Conclusion

- The API is the interface between the client and server. It isn't the actual processing and the work that goes in behind the scenes.
- The API is just the request, the responses, and the way the information is passed from one place to another.
- REST API defines how the interface should behave, not how the implementation or the architecture of the backend system.

## Module 2: Working with FastAPI

## Module 3: Introduction to pytest

## Reference

1. [Mastering REST APIs with FastAPI](https://www.coursera.org/learn/packt-mastering-rest-apis-with-fastapi-1xeea/)
2. [Mastering REST APIs with FastAPI, by Packt Publishing](https://github.com/vuanhtuan1012/Mastering-REST-APIs-with-FastAPI)
