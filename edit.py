from fastapi import APIRouter
from starlette.responses import Response
from server.data import doc as list_doc
from server.connect import *
from server.model import *
import base64

router = APIRouter()
doc = list_doc

@router.put("/edit", status_code=201)
async def edit_doc(doc : item):
    noreg = doc.noreg
    img1 = doc.img1
    img2 = doc.img2
    img3 = doc.img3
    img4 = doc.img4
    img5 = doc.img5
    img6 = doc.img6
    img7 = doc.img7
    img8 = doc.img8
    jenis_doc = doc.jns_doc
    ket = doc.ket
    
    with open(img1, "rb") as img_file:
        b64_img1 = base64.b64encode(img_file.read())
    with open(img2, "rb") as img_file:
        b64_img2 = base64.b64encode(img_file.read())
    with open(img3, "rb") as img_file:
        b64_img3 = base64.b64encode(img_file.read())
    with open(img4, "rb") as img_file:
        b64_img4 = base64.b64encode(img_file.read())
    with open(img5, "rb") as img_file:
        b64_img5 = base64.b64encode(img_file.read())
    with open(img6, "rb") as img_file:
        b64_img6 = base64.b64encode(img_file.read())
    with open(img7, "rb") as img_file:
        b64_img7 = base64.b64encode(img_file.read())
    with open(img8, "rb") as img_file:
        b64_img8 = base64.b64encode(img_file.read())
    
    try:
        cursor.execute ("UPDATE dokumen SET img1=?,img2=?,img3=?,img4=?,img5=?,img6=?,img7=?,img8=?,jns_doc=?,ket=? WHERE noreg=?", b64_img1, b64_img2, b64_img3, b64_img4, b64_img5, b64_img6, b64_img7, b64_img8, jenis_doc, ket, noreg)
        cursor.commit()
    except Exception as e:
        print(e)
    
    return doc