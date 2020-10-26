## Quickstart

You must have `poetry` installed to bootstrap the environment.

Clone this repo and setup the environment:

```
git clone https://github.com/jeckscolari/poke-shakespeare.git
cd poke-shakespeare
poetry install
poetry shell
```

Optionally, you can run `redis` to provide the application with caching capabilities. For example using `docker`:

```
docker run --name poke-redis -p 6379:6379 -d redis
```

Create an `.env` file to tell the application where `redis` is. You can clone `.env.example` if `redis` is running on `localhost:6379`:

```
cp .env.example .env
```

Run the application:

```
uvicorn app.main:app --reload
```

You'll find the application running on http://localhost:8000.

The endpoint `/pokemon` is documented under `/docs` or `/redoc`.

## Deploy with docker-compose

If you have `docker` and `docker-compose` you can deploy both the app and the cache with:

```
docker-compose up -d --build
```

The application will still be available on [localhost:8000](http://localhost:8000).

## Run tests

The tests are defined under the `tests` folder.

You can run the tests using the `pytest` command:

```
$ pytest
================================================================================ test session starts ================================================================================
platform linux -- Python 3.7.7, pytest-6.1.1, py-1.9.0, pluggy-0.13.1
rootdir: /home/jeck/Projects/poke-shakespeare, configfile: pyproject.toml, testpaths: tests
plugins: asyncio-0.14.0
collected 2 items

tests/test_routes/test_pokemon.py ..                                                                                                                                          [100%]

================================================================================= 2 passed in 0.28s =================================================================================
```
