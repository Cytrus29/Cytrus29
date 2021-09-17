from fastapi import FastAPI
from server.connect import *
from server import add, check, edit, delete, search

app = FastAPI()

app.include_router(check.router)
app.include_router(search.router)
app.include_router(add.router)
app.include_router(edit.router)
app.include_router(delete.router)
'''
app = FastAPI()
doc = list_doc

conn = pyodbc.connect('DRIVER={MySQL ODBC 5.3 ANSI Driver};User ID=8;Password=;Server=127.0.0.1;Database=document;Port=3306;String Types=Unicode')
cursor = conn.cursor()

class item(BaseModel):
    noreg:Optional[str] = None
    img1:Optional[str] = None
    img2:Optional[str] = None
    img3:Optional[str] = None
    img4:Optional[str] = None
    img5:Optional[str] = None
    img6:Optional[str] = None
    img7:Optional[str] = None
    img8:Optional[str] = None
    jns_doc:Optional[str] = None
    ket:Optional[str] = None
    
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

@app.get("/check/{noreg}", status_code=200)
async def search_doc_by_noreg(noreg: int, response: Response):
        sql = "SELECT * FROM dokumen WHERE noreg=?"
        result = pd.read_sql (sql, conn, params=[noreg])
        return result
    
@app.get("/search/{noreg}", status_code=201)
async def search_doc_by_noreg(noreg : int,  response: Response):
        
    try :
        cursor.execute ("SELECT * FROM dokumen WHERE noreg=?", noreg)
        ret = mssql_result2dict(cursor)
        conn.commit()
    except pyodbc.Error as e:
        print('SQL Query Failed : {e}')
        ret = {"message": "system error"}
    return ret
     
@app.post("/doc")
async def create_doc(doc : item):
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
        cursor.execute("INSERT INTO dokumen VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", noreg, b64_img1, b64_img2, b64_img3, b64_img4, b64_img5, b64_img6, b64_img7, b64_img8, jenis_doc, ket)
        cursor.commit()
    except Exception as e:
        print(e)
    
    return doc
    
@app.post("/edit", status_code=201)
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

@app.delete("/delete", status_code=201)
async def delete_doc(noreg : int):
    try:
        cursor.execute("DELETE FROM dokumen WHERE noreg=?" ,noreg) 
        cursor.commit()
    except Exception as e:
        print(e)
    
    return "Dokumen Anda Telah Dihapus"
'''