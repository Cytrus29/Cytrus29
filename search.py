from fastapi import APIRouter
from starlette.routing import Router
from server.data import doc as list_doc
from server.connect import *
from server.model import *
from starlette.responses import Response

router = APIRouter()
doc = list_doc

def mssql_result2dict(cursor):
    try: 
        result = []
        columns = [column[0] for column in cursor.description]
        for row in  cursor.fetchall():
            result.append(dict(zip(columns,row)))

        print(result)

        if len(result) > 0:
            ret = result
        else:
            ret = {"message": "no results found"}
    except pyodbc.Error as e:
        print(e)
        ret = { "message": "Internal Database Query Error"}
    
    return ret

@router.get("/search/{noreg}", status_code=201)
async def search_doc_by_noreg(noreg : int,  response: Response):
        
    try :
        cursor.execute ("SELECT * FROM dokumen WHERE noreg=?", noreg)
        ret = mssql_result2dict(cursor)
        conn.commit()
    except pyodbc.Error as e:
        print('SQL Query Failed : {e}')
        ret = {"message": "system error"}
    return ret