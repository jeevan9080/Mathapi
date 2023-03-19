from fastapi import FastAPI,Path

app=FastAPI()

inventory = {
        1:{
            "name":"Milk",
            "price":3.99,
            "brand":"Regular"
        }

}

@app.get("/get-item/{item_id}")
def get_item(item_id:int=Path(None,description="The ID of the item")):
    return inventory[item_id]

@app.get("/get-by-name")
def get_item(name:str=None):
    for item_id in inventory:
        if inventory[item_id]["name"]==name:
            return inventory[item_id]
    return{"Data":"Not Found"}