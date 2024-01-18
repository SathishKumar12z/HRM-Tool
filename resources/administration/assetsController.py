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


#                                 *********** A S S E S T S ***********

@router.get('/assets') 
def get_form(request:Request,db:Session = Depends(get_db)):
    if 'loginer_details' in request.session:
        token = request.session['loginer_details']
        try:
            payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
            loginer_id : int= payload.get("empid") 
            try:
                if loginer_id:
                    emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                    if emp_data.Lock_screen == 'OFF':
                        asset_data = db.query(models.Asset).filter(models.Asset.status=='ACTIVE').all()
                        return templates.TemplateResponse("Admin/Administration/Assets/assets.html",context={"request":request,'emp_data':emp_data,'asset_data':asset_data})
                    else:
                        return RedirectResponse('/HrmTool/Lock/lockscreen',status_code=302)
                else:
                    return RedirectResponse('/HrmTool/login/login',status_code=302)
            except:
                return RedirectResponse('/Error',status_code=302)
        except JWTError:
            return RedirectResponse('/HrmTool/login/login',status_code=302)
    else:
        return RedirectResponse('/HrmTool/login/login',status_code=303)

@router.post("/add_asset")
def create_data(request: Request, db: Session = Depends(get_db),Asset_Name:str=Form(...),Asset_Id: str = Form(...),Purchase_Date: str = Form(...),Purchase_From: str = Form(...),Manufacturer: str = Form(...),Model: str = Form(...),Serial_Number: str= Form(...),Supplier: str= Form(...),Condition:str=Form(...),Warranty:str=Form(...),Value:str=Form(...),Asset_User_id:str=Form(...),Current_status:str=Form(...)):
    if 'loginer_details' in request.session:
        token = request.session['loginer_details']
        try:
            payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
            loginer_id : int= payload.get("empid") 
            try:
                if loginer_id:
                    emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                    if emp_data.Lock_screen == 'OFF':
                        current_datetime = datetime.now()
                        body = models.Asset(Asset_Name=Asset_Name,Asset_Id=Asset_Id,Purchase_Date=Purchase_Date,Purchase_From=Purchase_From,Manufacturer=Manufacturer,Model=Model,Serial_Number=Serial_Number,Supplier=Supplier,Condition=Condition,Warranty=Warranty,Value=Value,Asset_User_id=Asset_User_id,Current_status=Current_status,status='active',created_by='',created_at=current_datetime, updated_at=current_datetime)
                        db.add(body)
                        db.commit()
                        return RedirectResponse("/HrmTool/Administration/assets", status_code=303)
                    else:
                        return RedirectResponse('/HrmTool/Lock/lockscreen',status_code=302)
                else:
                    return RedirectResponse('/HrmTool/login/login',status_code=302)
            except:
                return RedirectResponse('/Error',status_code=302)
        except JWTError:
            return RedirectResponse('/HrmTool/login/login',status_code=302)
    else:
        return RedirectResponse('/HrmTool/login/login',status_code=303)

@router.get("/taking_dlt_id_deduction/{ids}")
def taking_dlt_id_overtime(request: Request,ids:int,db: Session = Depends(get_db)):
    if 'loginer_details' in request.session:
        token = request.session['loginer_details']
        try:
            payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
            loginer_id : int= payload.get("empid") 
            try:
                if loginer_id:
                    emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                    if emp_data.Lock_screen == 'OFF':
                        a = db.query(models.Asset).filter(models.Asset.status=='ACTIVE').all()
                        db.query(models.Asset).filter(models.Asset.id == ids).update({"status":"INACTIVE"})
                        db.commit()
                        return templates.TemplateResponse("Assets.html",context={"request":request,'a':a})      
                    else:
                        return RedirectResponse('/HrmTool/Lock/lockscreen',status_code=302)
                else:
                    return RedirectResponse('/HrmTool/login/login',status_code=302)
            except:
                return RedirectResponse('/Error',status_code=302)
        except JWTError:
            return RedirectResponse('/HrmTool/login/login',status_code=302)
    else:
        return RedirectResponse('/HrmTool/login/login',status_code=303)
    
@router.get("/taking_edit_id/{ids}")       
def taking_edit_id(ids:int,request:Request,db: Session = Depends(get_db)):
    if 'loginer_details' in request.session:
        token = request.session['loginer_details']
        try:
            payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
            loginer_id : int= payload.get("empid") 
            try:
                if loginer_id:
                    emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                    if emp_data.Lock_screen == 'OFF':
                        single_data = db.query(models.Asset).filter(models.Asset.id==ids).filter(models.Asset.status=='ACTIVE').first()
                        return single_data
                    else:
                        return RedirectResponse('/HrmTool/Lock/lockscreen',status_code=302)
                else:
                    return RedirectResponse('/HrmTool/login/login',status_code=302)
            except:
                return RedirectResponse('/Error',status_code=302)
        except JWTError:
            return RedirectResponse('/HrmTool/login/login',status_code=302)
    else:
        return RedirectResponse('/HrmTool/login/login',status_code=303)

@router.post('/edit_asset')
def create_data(request: Request, db: Session = Depends(get_db),edit_id:str=Form(...),edit_asset_name: str= Form(...),edit_assetid: str =Form(...),edit_pdate:str = Form(...),edit_pfrom: str = Form(...),edit_man: str = Form(...),edit_sup: str = Form(...),edit_con: str = Form(...),edit_model: str = Form(...),edit_snum: str = Form(...),edit_war: str = Form(...),edit_stat: str = Form(...),edit_val: str = Form(...),edit_assuser: str = Form(...)):
    if 'loginer_details' in request.session:
        token = request.session['loginer_details']
        try:
            payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
            loginer_id : int= payload.get("empid") 
            try:
                if loginer_id:
                    emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                    if emp_data.Lock_screen == 'OFF':
                        db.query(models.Asset).filter(models.Asset.id==edit_id).update({"Asset_Name":edit_asset_name,"Asset_Id":edit_assetid,"Purchase_Date":edit_pdate,"Purchase_From":edit_pfrom,"Manufacturer":edit_man,"Supplier":edit_sup,"Condition":edit_con,"Model":edit_model,"Serial_Number":edit_snum,"Warranty":edit_war,"Value":edit_val,"Asset_User_id":edit_assuser,"Current_status":edit_stat})
                        db.commit()
                        return RedirectResponse("/HrmTool/Administration/assets", status_code=303) 
                    else:
                        return RedirectResponse('/HrmTool/Lock/lockscreen',status_code=302)
                else:
                    return RedirectResponse('/HrmTool/login/login',status_code=302)
            except:
                return RedirectResponse('/Error',status_code=302)
        except JWTError:
            return RedirectResponse('/HrmTool/login/login',status_code=302)
    else:
        return RedirectResponse('/HrmTool/login/login',status_code=303)