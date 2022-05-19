from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from orm.db import get_cache as get_cache_db, set_cache as set_cache_db

app = FastAPI()


class SetCache(BaseModel):
    key: str
    value: str


class GetCache(BaseModel):
    key: str


@app.get("/")
async def get_cache_endpoint(body: GetCache):
    value, message = get_cache_db(body.key)
    if not value:
        return HTTPException(status_code=404, detail=message)

    return {'key': body.key, 'value': value, 'detail': message, 'status_code': 200}


@app.post("/")
async def set_cache_endpoint(body: SetCache):
    is_set, message = set_cache_db(body.key, body.value)
    return {'detail': message, 'status_code': 200 if is_set else 500}
