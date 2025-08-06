# REST API with FastAPI <!-- omit in toc -->

This repo contains notes and projects of the course [Mastering REST APIs with FastAPI](https://www.coursera.org/learn/packt-mastering-rest-apis-with-fastapi-1xeea/home) on [Coursera](https://www.coursera.org).

- [Module 1: Introduction](#module-1-introduction)
  - [What is an API?](#what-is-an-api)
  - [What is a web API?](#what-is-a-web-api)
  - [What is in a request?](#what-is-in-a-request)
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

- There're 4 pieces of data in a request:
  - **Method**: can be one of many different values like `GET`, `POST`, `PUT`, etc.
    - These values are essentially preset. These methods have meaning to most servers and clients.
    - So, usually servers will repond in a predictable way to each method.
    - For example,
      - `GET` method tends to be used to retrieve information.
      - `POST` method tends to be used to create information.
      - `PATCH` method tends to be used to modify an existing bit of information.
    - Some methods have certain restrictions.
    - For example, most requests can have a body, some data included in the request, but some methods don't support a body being sent. For instance, we couldn't use the `GET` method to send information to the server because it can't have a body in most cases.
  - **Endpoint:** is where the request is sent.
    - For example, given an API url: `api.com/post?sorting=new`.
      - `api.com`: is a host.
      - `/post`: is an endpoint.
      - `?sorting=new`: `sorting=new` is the `sorting` query string argument with a value of `new`.
        - It's a way to send extra data to the server.
  - **Body:** usually is JSON data, used to when the client wants to send an extra information to the server.
  - **Header:** is also information in key-value pairs, but the keys tend to have specific meaning. For example, `Content-Type`. Headers are specific key value pairs that mean something.

## Module 2: Working with FastAPI

## Module 3: Introduction to pytest

## Reference

1. [Mastering REST APIs with FastAPI](https://www.coursera.org/learn/packt-mastering-rest-apis-with-fastapi-1xeea/)
2. [Mastering REST APIs with FastAPI, by Packt Publishing](https://github.com/vuanhtuan1012/Mastering-REST-APIs-with-FastAPI)
