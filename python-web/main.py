import random

from fastapi import FastAPI

app = FastAPI()

random_value = random.randint(1, 100)


@app.get("/")
def read_root():
    return {"msg": f"Hello World {random_value} new version"}
