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


@router.get('/goaltype')
def signin(request:Request,db:Session=Depends(get_db)):
    if 'loginer_details' in request.session:
        token = request.session['loginer_details']
        try:
            payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
            loginer_id : int= payload.get("empid") 
            try:
                if loginer_id:
                    emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                    if emp_data.Lock_screen == 'OFF':    
                        goal_type = db.query(models.Goal_Type).filter(models.Goal_Type.status=='ACTIVE').all()
                        return templates.TemplateResponse("Admin/Performance/Goals/goal-type.html",context={"request":request,'emp_data':emp_data,'goal_type':goal_type})	
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


@router.post('/goal_type')
def Goal_Type(request:Request,db:Session=Depends(get_db),name:str=Form(...),description:str=Form(...)):
    if 'loginer_details' in request.session:
        token = request.session['loginer_details']
        try:
            payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
            loginer_id : int= payload.get("empid") 
            try:
                if loginer_id:
                    emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                    if emp_data.Lock_screen == 'OFF':
                        max_id = db.query(func.max(models.Goal_Type.id)).scalar()
                        # Increment the ID by 1
                        new_id = max_id + 1 if max_id else 1

                        # Create a new Leave_Type record with the incremented ID
                        body = models.Goal_Type(id=new_id, Name=name, Description=description,
                                                Current_status="ACTIVE", status="ACTIVE", created_by="Admin")
                        db.add(body)
                        db.commit()
                        return RedirectResponse('/HrmTool/Performance/goaltype',status_code=303)
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


@router.get('/get_single_id/{main_id}')
def signin(main_id:int,request:Request,db:Session=Depends(get_db)):
    if 'loginer_details' in request.session:
        token = request.session['loginer_details']
        try:
            payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
            loginer_id : int= payload.get("empid") 
            try:
                if loginer_id:
                    emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                    if emp_data.Lock_screen == 'OFF':
                        goal_type = db.query(models.Goal_Type).filter(models.Goal_Type.id==main_id).filter(models.Goal_Type.status=='ACTIVE').first()
                    
                        return goal_type
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

@router.post('/edit')
def Goal_Type(request:Request,db:Session=Depends(get_db),edit_id:int=Form(...),edit_name:str=Form(...),edit_description:str=Form(...)):
    if 'loginer_details' in request.session:
        token = request.session['loginer_details']
        try:
            payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
            loginer_id : int= payload.get("empid") 
            try:
                if loginer_id:
                    emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                    if emp_data.Lock_screen == 'OFF':
                        db.query(models.Goal_Type).filter(models.Goal_Type.id==edit_id).update({"Name":edit_name,"Description":edit_description})
                        db.commit()
                        return RedirectResponse('/HrmTool/Performance/goaltype',status_code=303)
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



@router.get('/get_single/{delete_id}')
def signin(delete_id:int,request:Request,db:Session=Depends(get_db)):
    if 'loginer_details' in request.session:
        token = request.session['loginer_details']
        try:
            payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
            loginer_id : int= payload.get("empid") 
            try:
                if loginer_id:
                    emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                    if emp_data.Lock_screen == 'OFF':    
                        goal_type = db.query(models.Leave_Type).filter(models.Leave_Type.id==delete_id).filter(models.Leave_Type.status=='ACTIVE').first()
                        return goal_type
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
      
@router.post('/delete_goaltype')
def Goal_Type(request: Request, db: Session = Depends(get_db), delete_id: int = Form(...)):
    if 'loginer_details' in request.session:
        token = request.session['loginer_details']
        try:
            payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
            loginer_id : int= payload.get("empid") 
            try:
                if loginer_id:
                    emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                    if emp_data.Lock_screen == 'OFF':
                        # Delete the specified Leave_Type record
                        goal_type = db.query(models.Goal_Type).filter(models.Goal_Type.id == delete_id).first()
                        if goal_type:
                            db.delete(goal_type)
                            db.commit()
                            remaining_leave_types = db.query(models.Goal_Type).order_by(models.Goal_Type.id).all()
                            # Update the IDs of the remaining records
                            for i, goal_type in enumerate(remaining_leave_types, start=1):
                                db.execute(update(models.Goal_Type).where(models.Goal_Type.id == goal_type.id).values(id=i))
                            db.commit()
                            # Redirect to the home page with the updated list
                            return RedirectResponse('/HrmTool/Performance/goaltype', status_code=303)
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
