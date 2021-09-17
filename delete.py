from fastapi import APIRouter
from server.data import doc as list_doc
from starlette.responses import Response
from server.connect import *
from server.model import *

router = APIRouter()
doc = list_doc

@router.delete("/delete/{noreg}", status_code=201)
async def delete_doc(noreg : int):
    try:
        cursor.execute("DELETE FROM dokumen WHERE noreg=?" ,noreg) 
        cursor.commit()
    except Exception as e:
        print(e)
    
    return "Dokumen Anda Telah Dihapus"