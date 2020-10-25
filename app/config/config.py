from starlette.config import Config


config = Config('.env')


DB_HOST: str = config('DB_HOST')
DB_PORT: int = config('DB_PORT', cast=int)