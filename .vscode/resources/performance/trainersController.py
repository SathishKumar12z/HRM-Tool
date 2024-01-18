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

#cGet The Template
@router.get('/add_trainers') 
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
                        trainers_data = db.query(models.Trainers).filter(models.Trainers.status=='ACTIVE').all()
                        return templates.TemplateResponse("Admin/Performance/Trainings/trainers.html",context={"request":request,'emp_data':emp_data,'trainers_data':trainers_data})
                    else:
                        return RedirectResponse('/HrmTool/Lock/lockscreen',status_code=302)
                else:
                    return RedirectResponse('/HrmTool/login/login',status_code=302)
            except:
                return RedirectResponse('/HrmTool/login/login',status_code=302)
        except JWTError:
            return RedirectResponse('/HrmTool/login/login',status_code=302)
    else:
        return RedirectResponse('/HrmTool/login/login',status_code=303)
    
@router.post('/add_trainers')
def create_data(request: Request, db: Session = Depends(get_db),fname: str =Form(...), lname: str = Form(...),rol: str = Form(...) , mail: str = Form(...), ph: str = Form(...),des: str = Form(...),client_photo:UploadFile=File(...)):
    if 'loginer_details' in request.session:
        token = request.session['loginer_details']
        try:
            payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
            loginer_id : int= payload.get("empid") 
            try:
                if loginer_id:
                    emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                    if emp_data.Lock_screen == 'OFF':

                        file_location = f"./templates/assets/uploaded_files/{client_photo.filename}"
                        with open(file_location, 'wb+') as file_object:
                            shutil.copyfileobj(client_photo.file,file_object)
                        
                        data_check = db.query(models.Trainers).filter(models.Trainers.Email==mail).all()
                        if not data_check:
                            body = models.Trainers(First_Name=fname,Last_Name =lname,Role_id=rol,Email=mail,Phone =ph,Current_status=" Pending",Description=des,Photo=client_photo.filename,status="ACTIVE",created_by="admin")
                            db.add(body)
                            db.commit()
                            return 'ok'
                        else :
                            return 'error'
                    else:
                        return RedirectResponse('/HrmTool/Lock/lockscreen',status_code=302)
                else:
                    return RedirectResponse('/HrmTool/login/login',status_code=302)
            except:
                return RedirectResponse('/HrmTool/login/login',status_code=302)
        except JWTError:
            return RedirectResponse('/HrmTool/login/login',status_code=302)
    else:
        return RedirectResponse('/HrmTool/login/login',status_code=303)
# edit
@router.get("/eidt_trainers/{ids}")       
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
                        single_data = db.query(models.Trainers).filter(models.Trainers.id==ids).filter(models.Trainers.status=='ACTIVE').first()
                        return single_data
                    else:
                        return RedirectResponse('/HrmTool/Lock/lockscreen',status_code=302)
                else:
                    return RedirectResponse('/HrmTool/login/login',status_code=302)
            except:
                return RedirectResponse('/HrmTool/login/login',status_code=302)
        except JWTError:
            return RedirectResponse('/HrmTool/login/login',status_code=302)
    else:
        return RedirectResponse('/HrmTool/login/login',status_code=303)

@router.post('/trainers_update')
def create_data(request: Request, db: Session = Depends(get_db),  edit_id: str= Form(...),edit_fname: str =Form(...), edit_lname: str = Form(...),edit_rol: str = Form(...) , edit_mail: str = Form(...), edit_ph: str = Form(...), edit_des: str = Form(...)):
    if 'loginer_details' in request.session:
        token = request.session['loginer_details']
        try:
            payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
            loginer_id : int= payload.get("empid") 
            try:
                if loginer_id:
                    emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                    if emp_data.Lock_screen == 'OFF':
                        db.query(models.Trainers).filter(models.Trainers.id==edit_id).update({"First_Name": edit_fname, "Last_Name": edit_lname, "Role_id": edit_rol, "Email": edit_mail, "Phone": edit_ph,"Description": edit_des})
                        db.commit()
                        return RedirectResponse("/HrmTool/Performance/add_trainers", status_code=303)
                    else:
                        return RedirectResponse('/HrmTool/Lock/lockscreen',status_code=302)
                else:
                    return RedirectResponse('/HrmTool/login/login',status_code=302)
            except:
                return RedirectResponse('/HrmTool/login/login',status_code=302)
        except JWTError:
            return RedirectResponse('/HrmTool/login/login',status_code=302)
    else:
        return RedirectResponse('/HrmTool/login/login',status_code=303)
# # delete
@router.get("/delete_trainers/{ids}")
def taking_dlt_id(request: Request,ids:int,db: Session = Depends(get_db)):
    if 'loginer_details' in request.session:
        token = request.session['loginer_details']
        try:
            payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
            loginer_id : int= payload.get("empid") 
            try:
                if loginer_id:
                    emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                    if emp_data.Lock_screen == 'OFF':
                        a = db.query(models.Trainers).filter(models.Trainers.status=='ACTIVE').all()
                        db.query(models.Trainers).filter(models.Trainers.id == ids).update({"status":"INACTIVE","Current_status":"Inactive"})
                        db.commit()
                        return templates.TemplateResponse("trainers.html",context={"request":request})
                    else:
                        return RedirectResponse('/HrmTool/Lock/lockscreen',status_code=302)
                else:
                    return RedirectResponse('/HrmTool/login/login',status_code=302)
            except:
                return RedirectResponse('/HrmTool/login/login',status_code=302)
        except JWTError:
            return RedirectResponse('/HrmTool/login/login',status_code=302)
    else:
        return RedirectResponse('/HrmTool/login/login',status_code=303)
    
@router.get("/current_trainer/{data}/{ids}")
async def taking_dlt_id(ids:int,data:str,request: Request,db: Session = Depends(get_db)):
    print(data,ids )
    if 'loginer_details' in request.session:
        token = request.session['loginer_details']
        try:
            payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
            loginer_id : int= payload.get("empid") 
            try:
                if loginer_id:
                    emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                    if emp_data.Lock_screen == 'OFF':
                        print('here')
                        db.query(models.Trainers).filter(models.Trainers.id==ids).update({'Current_status':data})
                        db.commit()
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