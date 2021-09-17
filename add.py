from fastapi import APIRouter
from server.data import doc as list_doc
from server.connect import *
from server.model import *
import base64
from image.base import *

router = APIRouter()
doc = list_doc

@router.post("/doc")
async def create_doc(doc : item):
        
    try:
        cursor.execute("INSERT INTO dokumen VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", noreg, b64_img1, b64_img2, b64_img3, b64_img4, b64_img5, b64_img6, b64_img7, b64_img8, jenis_doc, ket)
        cursor.commit()
    except Exception as e:
        print(e)
    
    return doc