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

Create an `.env` file to tell the application where redis is. Clone `.env.example` if redis is running on `localhost:6379`.

```
cp .env.example .env
```

Run the application:

```
uvicorn app.main:app --reload
```

You'll find the application running on http://localhost:8000.
