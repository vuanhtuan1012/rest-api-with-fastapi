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
  - [What is FastAPI?](#what-is-fastapi)
  - [Aysnc functions](#aysnc-functions)
  - [WSGI vs. ASGI](#wsgi-vs-asgi)
  - [Thread vs. Coroutine](#thread-vs-coroutine)
  - [Deadlock](#deadlock)
  - [Race condition](#race-condition)
  - [Linter](#linter)
  - [Formatter](#formatter)
  - [Pydantic](#pydantic)
  - [Request Model](#request-model)
  - [Response Model](#response-model)
  - [API Routers](#api-routers)
  - [Project structure](#project-structure)
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
- Sometimes, backends are made up of multiple servers, *for example,* one for retrieving information, another for user authentication and registration.
- The client shouldn't care about how the backend is organized.

### Conclusion
- The API is the interface between the client and server. It isn't the actual processing and the work that goes in behind the scenes.
- The API is just the request, the responses, and the way the information is passed from one place to another.
- REST API defines how the interface should behave, not how the implementation or the architecture of the backend system.

## Module 2: Working with FastAPI

### What is FastAPI?
- FastAPI is a library that simplifies making APIs.
- FastAPI is a modern and async first library, which means that especially for web application development and APIs.
- It's very covinient and very fast performing option.

### Aysnc functions
- An `async` function means that the function can run more or less at the same time as other function.
- If **functions** that we're trying to run at the same time, **do heavy computation,** then they **can't run** at the same time.
- But, if **functions are just waiting** for the client to send some data or they're waiting for the database to respond to requests, or things like that, those functions **can run in parallel** more or less. That is where we get a speed benifit when we're using FastAPI and `async` functions.
- `async def` allows FastAPI to perform non-blocking I/O. When an endpoint `await`s **an asynchronous operation,** such as a database query or an external API call, the event loop **can suspend** that coroutine and **process other** incoming requests. *For example:*

  ```python
  from fastapi import FastAPI

  app = FastAPI()


  @app.get("/posts")
  async def get_posts():
      """
      Returns a list of posts
      """
      posts = await db.fetch_all(...)
      return posts
  ```

### WSGI vs. ASGI
- The main difference between WSGI (**W**eb **S**erver **G**ateway **I**nterface) and ASGI (**A**synchronous **S**erver **G**ateway **I**nterface) lies in their support for asynchronous code and modern comunication protocols.
- **WSGI** (**W**eb **S**erver **G**ateway **I**nterface):
  - Designed for **synchronous** Python application.
  - Each request is handled in a separate thread or process.
  - Blocks while handling I/O (e.g, reading from a DB or file).
- **ASGI** (**A**synchronous **S**erver **G**ateway **I**nterface):
  - Designed for **asynchronous** Python application.
  - Uses `asyncio` coroutines, allowing non-blocking I/O.
  - Can handle many more concurent requests efficiently.

| Features               | WSGI                             | ASGI                               |
|------------------------|----------------------------------|------------------------------------|
| **Sync / Async**       | Synchronous only                 | Asynchronous + Synchronous         |
| **Background task**    | Complex / Limited                | Simple & built-in                  |
| **Concurrency model**  | Thread-based                     | Coroutine-based (`asyncio`)        |
| **Protocol support**   | HTTP 1.1 only                    | HTTP 1.1, HTTP/2, WebSockets       |
| **Use cases**          | Classic web apps (Flask, Django) | Real-time app (FastAPI, Starlette) |
| **WebSockets support** | Not supported                    | Supported                          |

### Thread vs. Coroutine
- A **thread** is a real OS-level construct. Python uses threads via the `threading` module.
- Concurrency via threads is **preemptive**: the OS switches between threads as it sees fit.
- A **couroutine** is Python language feature for writing asynchronous code.
- We define one using `async def` and run it using `await`.
- Concurrency (using couritine) is **cooperative**: the coroutine yields control explicitly via `await`.

| Features              | Thread                       | Coroutine                                   |
|-----------------------|------------------------------|---------------------------------------------|
| **Definition**        | OS-managed unit of execution | Python-managed lightweight `async` function |
| **Managed by**        | Operating System             | Python runtime (`asyncio`)                  |
| **Context switching** | Done by OS (heavy)           | Done by Python (lightweight)                |
| **Overhead**          | High (memory and CPU)        | Low                                         |
| **Blocking behavior** | Can block entire thread      | Non-blocking with `await`                   |
| **Use case**          | Legacy I/O apps              | High I/O concurrency (web apps, scrapping)  |
| **Drawbacks**         | GIL, context switch cost     | Must avoid blocking code (`time.sleep`)     |
| **Complexity**        | Deadlocks, race conditions   | Harder debugging, async-first mindset       |

### Deadlock
- A deadlock happens when two (or more) tasks are waiting for each other forever.
- *For example*, task 1 has `lock_a`, but waits for `lock_b`, task 2 has `lock_b`, but waits for `lock_a`.
- When deadlock happens, **nobody can move**.

### Race condition
- A race condition happens when two tasks access and modify shared data at the same time, and the result depends on the timing of their execution.
- *For example*, two threads read a global variable before writing back. It leads to the updates overlap and overwrite each other.
- When a race condition happens, the result is wrong or unstable.

| Features         | Deadlock                           | Race condition                     |
|------------------|------------------------------------|------------------------------------|
| **What happens** | Everything stops                   | Things run, but produce wrong data |
| **Cause**        | Circular wait for resources        | Concurrent access to shared data   |
| **Symptom**      | Program hangs                      | Wrong / Unstable output            |
| **Fix**          | Avoid circular locks, use timeouts | Use locks or atomic operations     |

### Linter
- A linter is a **code quality checker**.
- **Linter** analyzes the code to detect issues and bad practices such as:
  - style violations (PEP8 rules, naming conventions, unused imports).
  - possible bugs (undefined variables, unreachable code).
  - best practices warnings (bad complexity, security concerns)
- Linter **doesn't change** code, only reports issues.
- Popular tools: [flake8](https://flake8.pycqa.org/en/latest/), [pylint](https://pypi.org/project/pylint/), [ruff](https://pypi.org/project/ruff/) (fast, Rust-based).

### Formatter
- A formatter is a **code beautifier**.
- **Formatter** automatically **rewrites** the code so it follows a consistent style, without changing its behavior.
- Formatter focuses on whitespace, indentation, line breaks.
- Popular tool: [black](https://pypi.org/project/black/), [yapf](https://pypi.org/project/yapf/), [ruff](https://pypi.org/project/ruff/).

### Pydantic
- [Pydantic](https://docs.pydantic.dev/latest/) is a Python library for **data validation** and **settings management** using Python type hints.
- It ensures that _"data looks exactly how we expected it to"_ without writting manual checks.
- What Pydantic does:
  - **Validate data**: Make sure values are of the right type.
  - **Parse data**: Convert compatible inputs automatically (e.g, `"123"` -> `123`).
  - **Serialize data**: Output data as clean Python dicts or JSON.
  - **Settings management**: Load configuration from environment variables or files.
- Key features:
  - **Type safety**: Uses Python type hints for validation.
  - **Automatic parsing**: Strings, lists, and other formats get converted when possible.
  - **Clear error messages**: If data is invalid, it raises a detailed `ValidationError`.
  - **Optional default**: Use default values for missing data.
  - **Setting models**: Easily load config from `.env` or OS environment variables.

### Request Model
- A **request model** in FastAPI is just a **Pydantic model** that is used to describe and validate the shape of incoming data (usually JSON in the request body). *For example,*

  ```python
  from pydantic import BaseModel


  class PostIn(BaseModel):
    """
    Represents the incoming post data sent to the API.
    Used for validating and storing fields provided by the client.
    """

    body: str
  ```
- **How to use it?** Defining a Pydantic model and **use** it as **type hint** of a function parameter in a FastAPI route.

  ```python
  from fastapi import APIRouter

  from social_media_api.models.post import Post, PostIn

  router = APIRouter(prefix="/posts", tags=["Posts"])


  @router.post("", response_model=Post, status_code=201)
  async def create_post(post: PostIn):
      """
      TODO: Creates a post
      """
  ```
- **What it does?** When a defined Pydantic model is used as type hint of a function parameter in a FastAPI route, it:
  - **parses** the incoming request body into that model.
  - **validates** types and required fields.
    - If the data is **invalid,** FastAPI returns a `422 Unprocessable Entity` with a detailed error message.
    - **If valid,** a fully typed Python object is available to work inside the function.
  - If an **extra field** is included incoming data, it can be ignored or raise an error depending on Pydantic version and model configuration.
    - Pydantic v1 will raise a validation error.
    - Pydantic v2.11 will silently drop extra fields.
    - The behavior can be changed via model configuration.
- **Why use request models?**
  - Automatic **type conversion**: strings to ints, dates, etc.
  - Automatic **error handling**.
  - Built-in **API docs** with request schema in `/docs`.
  - **Security**: ensures clients can't send unexpected or malicious fields.

### Response Model
- The `respone_model` parameter in FastAPI's route decorators (`@app.get`, `@app.post`, etc.) tells FastAPI **take whatever I return** from this function, **validate** and **filter** it through this Pydantic model, and **use** that as the **response schema** in the API docs. *For example:*

  ```python
  # models/post.py
  class Post(PostIn):
    """
    Represents the post data returned to the client.
    Used for formating and sending post information in API responses.
    """

    id: int


  # routers/posts.py
  @router.post("", response_model=Post, status_code=201)
  async def create_post(post: PostIn):
      """
      TODO: Creates a post
      """
  ```
- **What it does?**
  - **Validation**: Ensures that the endpoint returns data matching the model. If the return data is missing fields, has wrong types, or has extra fields, FastAPI will handle it (filter or error depending on config).
  - **Serialization**: Converts Pydantic models, datetimes, enums, etc. into JSON-friendly types.
  - **Documentation**: The OpenAPI schema (Swagger UI at `/docs`) will automatically show the model as the shape of the response.
- **Why it's important?**
  - Keeps API **responses consistent.**
  - **Prevents leaking** sensitive fields from the database.
  - **Generates accurate API docs** without extra work.
  - **Validates outgoing data,** just like request models validate **incoming** data.

### API Routers
- `APIRouter` in FastAPI is a way to organize routes into separate, reusable groups instead of putting everything directly in an application instance.
- ​An `APIrouter` is basically a FastAPI app, but **instead** of running on its own, ​it **can be included** into an existing app.
- Why use `APIRouter`?
  - **Modular organization**: Keep related endpoints together (e.g, `posts.py`, `comments.py`).
  - **Reusable**: Routers can be imported and included in multiple apps or microservices.
  - **Versioning** & **prefixes**: Easily group endpoints under `/api/v1`, `/auth`, etc.
  - **Shared settings**: Apply tags, dependencies, or responses to a whole group.

- *For example,*
  - `routers/posts.py`

    ```python
    from fastapi import APIRouter

    from social_media_api.models.post import Post, PostIn

    router = APIRouter(prefix="/posts", tags=["Posts"])


    @router.post("", response_model=Post, status_code=201)
    async def create_post(post: PostIn):
        """
        TODO: Creates a post
        """


    @router.get("", response_model=list[Post])
    async def get_all_posts():
        """
        TODO: Returns a list of posts
        """
    ```
  - `main.py`
    ```python
    from fastapi import FastAPI

    from social_media_api.routers.posts import router as post_router

    app = FastAPI()
    app.include_router(post_router)

    ```

### Project structure
- For a small or medium-sized FastAPI project, this is a recommended structure:

  ```text
  project/
  │
  ├── social_media_api/
  │   ├── __init__.py
  │   ├── main.py
  │   │
  │   ├── routers/   # HTTP layer (request/response)
  │   │   ├── __init__.py
  │   │   └── comments.py
  │   │   └── posts.py
  │   │
  │   ├── models/   # SQLAlchemy ORM models
  │   │   ├── __init__.py
  │   │   └── comment.py
  │   │   └── post.py
  │   │
  │   ├── schemas/   # Pydantic request/response models
  │   │   ├── __init__.py
  │   │   └── comment.py
  │   │   └── post.py
  │   │
  │   ├── database.py
  │   └── config.py
  │
  ├── tests/
  ├── Dockerfile
  ├── requirements.txt
  └── pyproject.toml   # optional but recommended
  ```
- Use **plural names** for `routers` because each router manages a collection of resources.
- Use **singular names** for `models`, `schemas` because the filename represents one model class.
- Separate `models` and `schemas`.
  - `models` contains SQLAlchemy ORM models.
  - `schemas` contains Pydantic request/response models.

## Module 3: Introduction to pytest

## Reference

1. [Mastering REST APIs with FastAPI](https://www.coursera.org/learn/packt-mastering-rest-apis-with-fastapi-1xeea/)
2. [Mastering REST APIs with FastAPI, by Packt Publishing](https://github.com/vuanhtuan1012/Mastering-REST-APIs-with-FastAPI)
3. ChatGPT
