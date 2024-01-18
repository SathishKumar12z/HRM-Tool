from typing import Dict, List,Optional
from fastapi import APIRouter, Depends, HTTPException, File, UploadFile, Depends, FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse,RedirectResponse
from fastapi.encoders import jsonable_encoder
import shutil,uuid,base64
from configs.base_config import BaseConfig
from jose import jwt, JWTError
from datetime import datetime 
from models import get_db, models
from sqlalchemy.orm import Session
from sqlalchemy import text
from resources.Oauth import create_access_token

router = APIRouter()




templates = Jinja2Templates(directory="templates")

current_datetime = datetime.today()

@router.get("/login")
async def Product_page(request: Request,db: Session = Depends(get_db)):
    
    return templates.TemplateResponse('Admin/Pages/Authentication/index.html', context={'request': request})


@router.post("/login/check_login")
async def Product_page(request: Request,db: Session = Depends(get_db),loginer_email:str=Form(...),loginer_password:str=Form(...)):

    mail_check = db.query(models.Employee).filter(models.Employee.Email == loginer_email ).filter(models.Employee.status == "ACTIVE").first() 
    if mail_check:
        # if mail_check.verify_password(loginer_password):
        pass_check = db.query(models.Employee).filter(models.Employee.Password == loginer_password ).filter(models.Employee.status == "ACTIVE").first() 
        if pass_check:
            emp_data = db.query(models.Employee).filter(models.Employee.Email==loginer_email,models.Employee.Password==loginer_password).filter(models.Employee.status=='ACTIVE').first()

            access_token = create_access_token(data={"empid": emp_data.id,"department":emp_data.Department_id})
            request.session['loginer_details'] = access_token
            return '/HrmTool/Admin/dashboard'
        else:
            return '2'
    else:
        return '1'

    
@router.get('/logout')
def user_logout(request: Request, db: Session = Depends(get_db)):

    if "loginer_details" in request.session:

        del request.session["loginer_details"]
        return RedirectResponse('/HrmTool/login/login',status_code=302)    
    else:
        return RedirectResponse('/HrmTool/login/login',status_code=302)
    