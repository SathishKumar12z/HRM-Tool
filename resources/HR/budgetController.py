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

@router.get('/budget') 
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
                        budget_data = db.query(models.Budget).all()
                        return templates.TemplateResponse("budget.html",context={"request":request,"budget_data":budget_data})
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
    
@router.post("/submit_budget")
def submit_budget(request: Request, db: Session = Depends(get_db),
                    budget_title: str = Form(...),
                 budget_type: str = Form(...),
                 budget_start_date: str = Form(...),
                 budget_end_date: str = Form(...),
                 revenue_title: list = Form(...),
                 revenue_amount: list = Form(...),
                 total_revenve: str = Form(...),
                 expenses_title: list = Form(...),
                 expenses_amount: list = Form(...),
                 total_expense: str = Form(...),
                 total_profit: str = Form(...),
                 tax_amount: str = Form(...),
                 budget_amount: str = Form(...)):
    if 'loginer_details' in request.session:
        token = request.session['loginer_details']
        try:
            payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
            loginer_id : int= payload.get("empid") 
            try:
                if loginer_id:
                    emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                    if emp_data.Lock_screen == 'OFF':
                        body = models.Budget(
                            Budget_Title = budget_title,
                            Budget_Type = budget_type,
                            Start_Date = budget_start_date,
                            End_Date = budget_end_date,
                            Revenue_Title = revenue_title,
                            Revenue_Amount = revenue_amount,
                            Overall_Revenues = total_revenve,
                            Expenses_Title = expenses_title,
                            Expenses_Amount = expenses_amount,
                            Overall_Expense = total_expense,
                            Expected_Profit = total_profit,
                            Tax = tax_amount,
                            Budget_Amount = budget_amount,
                        )

                        db.add(body)
                        db.commit()
                        # return RedirectResponse("/get_form", status_code=303)
                        return RedirectResponse("budget", status_code=303)
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
    
@router.get('/submit_budget') 
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
                        return templates.TemplateResponse("budget.html",context={"request":request})
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
    
@router.get("/taking_edit_modal/{ids}")       
def taking_edit_modal(ids:int,request:Request,db: Session = Depends(get_db)):
    if 'loginer_details' in request.session:
        token = request.session['loginer_details']
        try:
            payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
            loginer_id : int= payload.get("empid") 
            try:
                if loginer_id:
                    emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                    if emp_data.Lock_screen == 'OFF':
                        single_data = db.query(models.Budget).filter(models.Budget.id==ids).first()
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
    
@router.post('/budget_edit')
def create_data(request: Request, db: Session = Depends(get_db),  edit_id: str= Form(...),edit_budget_title: str =Form(...), edit_budget_type: str = Form(...),edit_budget_start_date: str = Form(...) , edit_budget_end_date: str = Form(...), edit_revenue_title: str = Form(...), edit_revenue_amount: str = Form(...),edit_total_revenve: str=Form(...),edit_expenses_title: str=Form(...),edit_expenses_amount: str=Form(...),edit_total_expense: str=Form(...),edit_total_profit: str=Form(...),edit_tax_amount: str=Form(...),edit_budget_amount: str=Form(...)):
    if 'loginer_details' in request.session:
        token = request.session['loginer_details']
        try:
            payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
            loginer_id : int= payload.get("empid") 
            try:
                if loginer_id:
                    emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                    if emp_data.Lock_screen == 'OFF':
                        db.query(models.Budget).filter(models.Budget.id==edit_id).update({"Budget_Title": edit_budget_title, "Budget_Type": edit_budget_type, "Start_Date": edit_budget_start_date, "End_Date": edit_budget_end_date, "Revenue_Title": edit_revenue_title, "Revenue_Amount": edit_revenue_amount,"Overall_Revenues":edit_total_revenve,"Overall_Revenues":edit_total_revenve ,"Expenses_Title":edit_expenses_title ,"Expenses_Amount":edit_expenses_amount ,"Overall_Expense":edit_total_expense,"Expected_Profit":edit_total_profit ,"Tax":edit_tax_amount ,"Budget_Amount":edit_budget_amount  })
                        db.commit()
                        return RedirectResponse("/budget", status_code=303)    
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
    
@router.get("/delete_budget/{ids}")
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
                        db.query(models.Budget).filter(models.Budget.id== ids).delete()
                        db.commit()
                        return templates.TemplateResponse("budget.html",context={"request":request})
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