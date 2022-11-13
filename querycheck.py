from typing import Optional

from fastapi import FastAPI, Query, Path, Body
app = FastAPI()

#
# @app.get("/items/")
# async def read_items(q: Optional[str] = Query(None, max_length=10)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results
#
#
#
# @app.get("/items/alias/")
# async def read_items(q: Optional[str] = Query(None, alias="item-query", title="标题", description="描述")):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results




from pydantic import BaseModel, Field



# class Item(BaseModel):
#     name: str
#     description: Optional[str] = Field(
#         None, title="The description of the item", max_length=300
#     )
#     price: float = Field(..., gt=0, description="The price must be greater than zero")
#     tax: Optional[float] = None
#
#
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item = Body(..., embed=True)):
#     results = {"item_id": item_id, "item": item}
#     return results


# @app.get("/items/path-and-query/{item_id}")
# async def read_items(
#     *,
#     item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),
#     q: str,
#     size: float = Query(..., gt=0, lt=10.5)
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

# from fastapi import Cookie
#
#
# @app.get("/items/")
# async def read_items(ads_id: Optional[str] = Cookie(None)):
#     return {"ads_id": ads_id}

# from fastapi import Header
#
#
# @app.get("/items/")
# async def read_items(
#     strange_header: Optional[str] = Header(None, convert_underscores=False)
# ):
#     return {"strange_header": strange_header}


#
# from pydantic import EmailStr
#
# app = FastAPI()
#
#
# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#     full_name: Optional[str] = None
#
#
#
# class UserOut(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: Optional[str] = None
#
#
# # Don't do this in production!
# @app.post("/user/userIn", response_model=UserIn)
# async def create_user(user: UserOut):
#     return user
#
#
# @app.post("/user/userOut", response_model=UserOut)
# async def create_user(user: UserIn):
#     return user


from typing import List


app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True,
            #response_model_include={"name", "description"}
            response_model_exclude={"name", "description"}
        )
async def read_item(item_id: str):
    return items[item_id]
