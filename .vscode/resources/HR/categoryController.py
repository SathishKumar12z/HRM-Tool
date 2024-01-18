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

#                                                       ***** B U D G E T  *****

#cGet The Template
@router.get('/category') 
def get_form(request:Request,db:Session=Depends(get_db)):
    if 'loginer_details' in request.session:
        token = request.session['loginer_details']
        try:
            payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
            loginer_id : int= payload.get("empid") 
            try:
                if loginer_id:
                    emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                    if emp_data.Lock_screen == 'OFF':
                        new_user = db.query(models.Categories).filter(models.Categories.status=='ACTIVE').all()
                        sub_cate = db.query(models.Sub_Category).filter(models.Sub_Category.current_status=='Active').filter(models.Sub_Category.status=='ACTIVE').all()
                        return templates.TemplateResponse("Admin/HR/Accounting/categories.html",context={"request":request,'emp_data':emp_data,"new_id":new_user,'sub_cate':sub_cate})
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

@router.post('/category')
def create_data(request: Request, db: Session = Depends(get_db),Name: str =Form(...)):
    if 'loginer_details' in request.session:
        token = request.session['loginer_details']
        try:
            payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
            loginer_id : int= payload.get("empid") 
            try:
                if loginer_id:
                    emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                    if emp_data.Lock_screen == 'OFF':
                        body = models.Categories(Name=Name,SubCategory_id='Add Sub Category',status='ACTIVE',created_by=loginer_id)
                        db.add(body)
                        db.commit()
                        return RedirectResponse("/HrmTool/HR/category", status_code=303)
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
    
@router.get("/catedit/{ids}")      
def catedit(ids:int,request:Request,db: Session = Depends(get_db)):
    if 'loginer_details' in request.session:
        token = request.session['loginer_details']
        try:
            payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
            loginer_id : int= payload.get("empid") 
            try:
                if loginer_id:
                    emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                    if emp_data.Lock_screen == 'OFF':
                        single_data = db.query(models.Categories).filter(models.Categories.id==ids).filter(models.Categories.status=='ACTIVE').first()
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
    
@router.post('/category_update')
def create_data(request: Request, db: Session = Depends(get_db),  edit_id: str= Form(...),edit_Name: str =Form(...)):
    if 'loginer_details' in request.session:
        token = request.session['loginer_details']
        try:
            payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
            loginer_id : int= payload.get("empid") 
            try:
                if loginer_id:
                    emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                    if emp_data.Lock_screen == 'OFF':
                        db.query(models.Categories).filter(models.Categories.id==edit_id).update({"Name": edit_Name})
                        db.commit()
                        return RedirectResponse("/HrmTool/HR/category", status_code=303)
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
    
@router.get('/subcat/{cat_id}') 
def get_form(request:Request,cat_id:int,db:Session=Depends(get_db)):
    if 'loginer_details' in request.session:
        token = request.session['loginer_details']
        try:
            payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
            loginer_id : int= payload.get("empid") 
            try:
                if loginer_id:
                    emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                    if emp_data.Lock_screen == 'OFF':
                        cat_data = db.query(models.Categories).filter(models.Categories.id==cat_id).filter(models.Categories.status=='ACTIVE').first()
                        new_user = db.query(models.Sub_Category).filter(models.Sub_Category.Category_id==cat_id).filter(models.Sub_Category.status=='ACTIVE').all()
                        return templates.TemplateResponse("Admin/HR/Accounting/sub-category.html",context={"request":request,'emp_data':emp_data,"new_id":new_user,'cat_name':cat_data})
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

@router.post('/subcategory')
def create_data(request: Request, db: Session = Depends(get_db),Name: int =Form(...),SubCategory_id: str= Form(...),cur_state:str=Form(...)):
    if 'loginer_details' in request.session:
        token = request.session['loginer_details']
        try:
            payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
            loginer_id : int= payload.get("empid") 
            try:
                if loginer_id:
                    emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                    if emp_data.Lock_screen == 'OFF':

                        data_check = db.query(models.Sub_Category).filter(models.Sub_Category.Name == SubCategory_id.lower(),models.Sub_Category.Name == SubCategory_id.upper()).filter(models.Sub_Category.status=='ACTIVE').all()
                        if not data_check:
                            body = models.Sub_Category(Category_id=Name,Name=SubCategory_id,current_status=cur_state,status='ACTIVE',created_by=loginer_id)
                            db.add(body)
                            db.commit()

                            if cur_state=='Active':
                                db.query(models.Sub_Category).filter(models.Sub_Category.Category_id == Name,models.Sub_Category.id != body.id ).update({'current_status':'Inactive'})
                                db.commit()
                            return 'ok'
                        else:
                            return 'error'
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
    
@router.get("/subcatedit/{ids}")      
def subcatedit(ids:int,request:Request,db: Session = Depends(get_db)):
    if 'loginer_details' in request.session:
        token = request.session['loginer_details']
        try:
            payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
            loginer_id : int= payload.get("empid") 
            try:
                if loginer_id:
                    emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                    if emp_data.Lock_screen == 'OFF':
                        single_data = db.query(models.Sub_Category).filter(models.Sub_Category.id==ids).filter(models.Sub_Category.status=='ACTIVE').first()
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
    
@router.post('/subcategory_update')
def create_data(request: Request, db: Session = Depends(get_db),  edit_id: str= Form(...),edit_SubCategory_id: str =Form(...)):
    if 'loginer_details' in request.session:
        token = request.session['loginer_details']
        try:
            payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
            loginer_id : int= payload.get("empid") 
            try:
                if loginer_id:
                    emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                    if emp_data.Lock_screen == 'OFF':
                        db.query(models.Sub_Category).filter(models.Sub_Category.id==edit_id).update({"SubCategory_id": edit_SubCategory_id})
                        db.commit()
                        return RedirectResponse("/subcat", status_code=303)
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
    
@router.get("/delsubcat/{ids}")
def delete_subcategory(request: Request,ids:int,db: Session = Depends(get_db)):
    if 'loginer_details' in request.session:
        token = request.session['loginer_details']
        try:
            payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
            loginer_id : int= payload.get("empid") 
            try:
                if loginer_id:
                    emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                    if emp_data.Lock_screen == 'OFF':
                        a = db.query(models.Sub_Category).filter(models.Sub_Category.status=='ACTIVE').all()
                        db.query(models.Sub_Category).filter(models.Sub_Category.id == ids).update({"status":"INACTIVE"})
                        db.commit()
                        return templates.TemplateResponse("sub-category.html",context={"request":request,'a':a})
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
 
@router.get("/status_change/{data}/{id_value}")
def delete_subcategory(request: Request,data:str,id_value:int,db: Session = Depends(get_db)):
    if 'loginer_details' in request.session:
        token = request.session['loginer_details']
        try:
            payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
            loginer_id : int= payload.get("empid") 
            try:
                if loginer_id:
                    emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                    if emp_data.Lock_screen == 'OFF':
                        a = db.query(models.Sub_Category).filter(models.Sub_Category.status=='ACTIVE').all()
                        db.query(models.Sub_Category).filter(models.Sub_Category.id == id_value).update({"current_status":f"{data}"})
                        db.commit()
                        if data ==' Active':
                            db.query(models.Sub_Category).filter(models.Sub_Category.id !=id_value).update({"current_status":"Inactive"})
                            db.commit()
                        return templates.TemplateResponse("sub-category.html",context={"request":request,'a':a})
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
