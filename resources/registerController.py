from typing import Dict, List,Optional
from fastapi import APIRouter, Depends, HTTPException, File, UploadFile, Depends, FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse,RedirectResponse
from fastapi.encoders import jsonable_encoder
# from models.schemas import masterSchemas
import base64
import shutil,uuid
from configs.base_config import BaseConfig
from jose import jwt, JWTError
# from django.contrib import messages
from datetime import datetime 
from models import get_db, models
from sqlalchemy.orm import Session
from sqlalchemy import text,func,update

router = APIRouter()

templates = Jinja2Templates(directory="templates")

current_datetime = datetime.today()

@router.get("/reg")
def register(request:Request,db:Session = Depends(get_db)):
    # if 'loginer_details' in request.session:
    #     token = request.session['loginer_details']
    #     try:
    #         payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
    #         loginer_id : int= payload.get("empid") 
    #         try:
    #             if loginer_id:
    #                 emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
    #                 if emp_data.Lock_screen == 'OFF':  
                        return templates.TemplateResponse("Admin/Pages/Authentication/register.html",context={"request":request,"method":"Post Method"})
    #                 else:
    #                     return RedirectResponse('/HrmTool/Lock/lockscreen',status_code=302)
    #             else:
    #                 return RedirectResponse('/HrmTool/login/login',status_code=302)
    #         except:
    #             return RedirectResponse('/HrmTool/login/login',status_code=302)
    #     except JWTError:
    #         return RedirectResponse('/HrmTool/login/login',status_code=302)
    # else:
    #     return RedirectResponse('/HrmTool/login/login',status_code=303)
    
#create Data
@router.post("/register")
def create_data(request:Request,db:Session=Depends(get_db),Email:str=Form(...),Password:str=Form(...)):
    # if 'loginer_details' in request.session:
    #     token = request.session['loginer_details']
    #     try:
    #         payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
    #         loginer_id : int= payload.get("empid") 
    #         try:
    #             if loginer_id:
    #                 emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
    #                 if emp_data.Lock_screen == 'OFF':    
                        body=models.Register(Email=Email,Password=Password,status="ACTIVE",created_by='user')
                        db.add(body)
                        db.commit()
    #                 else:
    #                     return RedirectResponse('/HrmTool/Lock/lockscreen',status_code=302)
    #             else:
    #                 return RedirectResponse('/HrmTool/login/login',status_code=302)
    #         except:
    #             return RedirectResponse('/HrmTool/login/login',status_code=302)
    #     except JWTError:
    #         return RedirectResponse('/HrmTool/login/login',status_code=302)
    # else:
    #     return RedirectResponse('/HrmTool/login/login',status_code=303)   