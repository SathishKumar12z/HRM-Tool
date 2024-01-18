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
from sqlalchemy import text

router = APIRouter()

templates = Jinja2Templates(directory="templates")

current_datetime = datetime.today()

@router.get("/lockscreen")
async def Product_page(request: Request,db: Session = Depends(get_db)):
    if 'loginer_details' in request.session:
        token = request.session['loginer_details']
        try:
            payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
            loginer_id : int= payload.get("empid") 
            try:
                if loginer_id:
                    emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                    return templates.TemplateResponse('Admin/Pages/Authentication/lock-screen.html',context={'request':request,'emp_data':emp_data})
                else:
                    return RedirectResponse('/HrmTool/login/login',status_code=302)
            except:
                return RedirectResponse('/HrmTool/login/login',status_code=302)
        except JWTError:
            return RedirectResponse('/HrmTool/login/login',status_code=302)
    else:
        return RedirectResponse('/HrmTool/login/login',status_code=303)

@router.post("/lockscreen")
async def Product_page(request: Request,db: Session = Depends(get_db),lock_password:str=Form(...)):
    if 'loginer_details' in request.session:
        token = request.session['loginer_details']
        try:
            payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
            loginer_id : int= payload.get("empid") 
            try:
                emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                if emp_data.Password == lock_password:
                    db.query(models.Employee).filter(models.Employee.id==loginer_id).update({'Lock_screen':'OFF'})
                    db.commit()
                    return 'ok'
                else:
                    return 'error'
            except:
                return templates.TemplateResponse('Admin/Pages/Authentication/index.html', context={'request': request,'error':'Invalid Loginer'})
        except JWTError:
            return RedirectResponse('/HrmTool/login/login',status_code=302)
    else:
        return RedirectResponse('/HrmTool/login/login',status_code=303)

@router.get("/lockscreen_id/{empId}")
async def Product_page(empId:int,request: Request,db: Session = Depends(get_db)):
    if 'loginer_details' in request.session:
        token = request.session['loginer_details']
        try:
            payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
            loginer_id : int= payload.get("empid") 
            try:
                if loginer_id:
                    db.query(models.Employee).filter(models.Employee.id==empId).update({'Lock_screen':'ON'})
                    db.commit()
                    return '/HrmTool/Lock/lockscreen'
                else:
                    return RedirectResponse('/HrmTool/login/login',status_code=302)
            except:
                return RedirectResponse('/HrmTool/login/login',status_code=302)
        except JWTError:
            return RedirectResponse('/HrmTool/login/login',status_code=302)
    else:
        return RedirectResponse('/HrmTool/login/login',status_code=303)
