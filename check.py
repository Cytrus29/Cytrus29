import pandas as pd
from server.data import doc as list_doc
from starlette.responses import Response
from server.connect import *
from server.model import *
from fastapi import APIRouter

router = APIRouter()
doc = list_doc

@router.get("/check/{noreg}", status_code=200)
async def check_doc_by_noreg(noreg: int, response: Response):
        sql = "SELECT * FROM dokumen WHERE noreg=?"
        result = pd.read_sql (sql, conn, params=[noreg])
        return result