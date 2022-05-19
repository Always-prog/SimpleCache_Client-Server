# SimpleCache_Client-Server
Works on FastAPI.
I started learning FastAPI and SqlAlchemy,
because of this I created this simple cache client-server.


## Use cache client for simple caching 
### Configure server.

1. Create database (mysql or postgresql), and put next enviroment variables:<br>
`DB_USER` - username of database user <br>
`DB_PASSWORD` - password <br>
`DB_NAME` - database name <br>
`DB_HOST` - database host <br>
`DB_TYPE` - database type (postgresql, mysql)<br>
2. Go to CacheServer and run FastAPI app. For localhost it ` uvicorn main:app --reload`
3. Test it by `CacheServer/test_main.http` file.
4. Done

```python
from client import CacheClient


cache_client = CacheClient('https://your-domain.com:4352')
cache_client.set_cache('testing_key', 'testing value')
print(cache_client.get_cache('testing_key')) # --> "testing value"
```

Also, you can use the server directly.
Just see `<running server url>/docs` to see swagger, http://localhost:800/docs.


