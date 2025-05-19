from fastapi import FastAPI

app = FastAPI(title="University")


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/status")
async def read_status():
    return {"status": 200,"message": "OK"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#    return {"item_id": item_id, "q": q}
