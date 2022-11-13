from fastapi import FastAPI

app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}


# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
#     return {"user_id": user_id}

# @app.get("/users/me")
# async def read_user_me():
#     return {"user_id": "the current user"}
#
#
# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
#     return {"user_id": user_id}
#
#
# from enum import Enum
# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"
#
#
# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name == ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}
#
#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}
#
#     return {"model_name": model_name, "message": "Have some residuals"}
#
#
# @app.get("/files/{file_path:path}")
# async def read_file(file_path: str):
#     return {"file_path": file_path}
#
#
# @app.get("/files/test/{file_path}")
# async def read_file(file_path: str):
#     return {"file_path": file_path}

#
#
# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
#
#
# from typing import Optional
#
#
# @app.get("/items")
# async def read_item(skip: int, limit: int, remark: Optional[int]):
#     return fake_items_db[skip : skip + limit]
#
#
#
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item
#
#
# @app.get("/users/{user_id}/items/{item_id}")
# async def read_user_item(
#     user_id: int, item_id: str, q: Optional[str] = None, short: bool = False
# ):
#     item = {"item_id": item_id, "owner_id": user_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item


from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item