from fastapi import FastAPI
from pydantic import BaseModel
from .detected import detected_color


class Item(BaseModel):
    url:str


app = FastAPI()


@app.post("/detect_color/")
async def background_color(item: Item):
    obj = detected_color.BackgroundColorDetector(item.url)
    obj.detect()
    return obj.detect()