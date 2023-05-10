import io
from empty_detector import detect
import uvicorn
import numpy as np
from PIL import Image
from fastapi import FastAPI
from base64 import b64decode
from pydantic import BaseModel
import cv2

class Item(BaseModel):
    image: str

app = FastAPI()

im_empty = cv2.imread('photo_0.jpg')

@app.post("/detect/")
async def create_item(item: Item):
    img = np.array(Image.open(io.BytesIO(b64decode(item.image))))
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imwrite('te.jpg',img)
    result = detect(im_empty=im_empty , im_test=img)
    return result

if __name__ == '__main__':  
    uvicorn.run("server:app", host="0.0.0.0", port=8000, workers=1, reload=True)