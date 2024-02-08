from typing import Dict, List,Optional
from fastapi import APIRouter, Depends, HTTPException, File, UploadFile, Depends, FastAPI, Request, Form,status
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
@router.get('/Rate_type') 
def get_form(request:Request,db:Session = Depends(get_db)):
    try:
        if 'loginer_details' in request.session:
            token = request.session['loginer_details']
            try:
                payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
                loginer_id : int= payload.get("empid") 
                try:
                    if loginer_id:
                        emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                        if emp_data.Lock_screen == 'OFF':
                            return templates.TemplateResponse("rate_item.html",context={"request":request})
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
    except JWTError:
            return RedirectResponse('/HrmTool/login/login',status_code=302)
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"detail": "Internal Server Error"}) 
    
@router.get('/payroll-items') 
def get_form(request:Request,db:Session = Depends(get_db)):
    try:
        if 'loginer_details' in request.session:
            token = request.session['loginer_details']
            try:
                payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
                loginer_id : int= payload.get("empid") 
                try:
                    if loginer_id:
                        emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                        if emp_data.Lock_screen == 'OFF':
                            a = db.query(models.Payroll_Items_Addition).filter(models.Payroll_Items_Addition.status=='ACTIVE').all()
                            b = db.query(models.Payroll_Items_Overtime).filter(models.Payroll_Items_Overtime.status=='ACTIVE').all()
                            c = db.query(models.Payroll_Items_Deducation).filter(models.Payroll_Items_Deducation.status=='ACTIVE').all()
                            return templates.TemplateResponse("Admin/HR/Payroll/payroll-items.html",context={"request":request,'emp_data':emp_data,'a':a,'b':b,'c':c})
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
    except JWTError:
            return RedirectResponse('/HrmTool/login/login',status_code=302)
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"detail": "Internal Server Error"}) 
    

@router.post("/add_addition")
def add_addition(request: Request, db: Session = Depends(get_db),Name: str=Form(...), Category: str = Form(...),unit_calculation: str = Form(...) , unit_amount: str = Form(...), addition_assignee: str= Form(...), assignee: str=Form()):
    try:
        if 'loginer_details' in request.session:
            token = request.session['loginer_details']
            try:
                payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
                loginer_id : int= payload.get("empid") 
                try:
                    if loginer_id:
                        emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                        if emp_data.Lock_screen == 'OFF':
                            body = models.Payroll_Items_Addition(Name=Name,Category= Category,Unit_calculation=unit_calculation,Unit_Amount=unit_amount,Assignee_radio=addition_assignee,Assignee_drop=assignee,status="ACTIVE",created_by=" ")
                            db.add(body)
                            db.commit()
                            return RedirectResponse("/payroll-addition", status_code=303)
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
    except JWTError:
            return RedirectResponse('/HrmTool/login/login',status_code=302)
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"detail": "Internal Server Error"}) 

@router.get("/payroll-addition")
def add_addition(request: Request, db: Session = Depends(get_db)):
    try:
        if 'loginer_details' in request.session:
            token = request.session['loginer_details']
            try:
                payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
                loginer_id : int= payload.get("empid") 
                try:
                    if loginer_id:
                        emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                        if emp_data.Lock_screen == 'OFF':
                            # a = db.query(models.Payroll_Items_Addition).filter(models.Payroll_Items_Addition.status=='ACTIVE').all()
                            a = db.query(models.Payroll_Items_Addition).filter(models.Payroll_Items_Addition.status=='ACTIVE').all()
                            b = db.query(models.Payroll_Items_Overtime).filter(models.Payroll_Items_Overtime.status=='ACTIVE').all()
                            c = db.query(models.Payroll_Items_Deducation).filter(models.Payroll_Items_Deducation.status=='ACTIVE').all()
                            return templates.TemplateResponse("payroll-items.html",context={"request":request,'a':a,'b':b,'c':c})
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
    except JWTError:
            return RedirectResponse('/HrmTool/login/login',status_code=302)
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"detail": "Internal Server Error"}) 

@router.post("/edit_addition")
def create_data(request: Request, db: Session = Depends(get_db),edit_id:str= Form(...),  edit_name: str = Form(...), edit_category: str = Form(...), edit_unit_calculation: str = Form(...), edit_unit_Amount: str = Form(...), edit_addition_assignee: str=Form(...), edit_drop: str=Form(...)):
    try:
        if 'loginer_details' in request.session:
            token = request.session['loginer_details']
            try:
                payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
                loginer_id : int= payload.get("empid") 
                try:
                    if loginer_id:
                        emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                        if emp_data.Lock_screen == 'OFF':
                            a = db.query(models.Payroll_Items_Addition).filter(models.Payroll_Items_Addition.status=='ACTIVE').all()
                            b = db.query(models.Payroll_Items_Overtime).filter(models.Payroll_Items_Overtime.status=='ACTIVE').all()
                            c = db.query(models.Payroll_Items_Deducation).filter(models.Payroll_Items_Deducation.status=='ACTIVE').all()
                            db.query(models.Payroll_Items_Addition).filter(models.Payroll_Items_Addition.id==edit_id).update({"Name": edit_name, "Category": edit_category, "Unit_calculation": edit_unit_calculation, "Unit_Amount": edit_unit_Amount, "Assignee_radio": edit_addition_assignee, "Assignee_drop": edit_drop})
                            db.commit()
                            return templates.TemplateResponse("payroll-items.html",{"request":request,'b':b,'a':a,'c':c})
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
    except JWTError:
            return RedirectResponse('/HrmTool/login/login',status_code=302)
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"detail": "Internal Server Error"}) 
    
@router.post("/edit_overtime")
def edit(request: Request, db: Session = Depends(get_db),edit_id_ovr:str= Form(...),  edit_ovr_name: str = Form(...), edit_ovr_rate_id: str = Form(...), edit_ovr_rate: str = Form(...)):
    try:
        if 'loginer_details' in request.session:
            token = request.session['loginer_details']
            try:
                payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
                loginer_id : int= payload.get("empid") 
                try:
                    if loginer_id:
                        emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                        if emp_data.Lock_screen == 'OFF':
                            a = db.query(models.Payroll_Items_Addition).filter(models.Payroll_Items_Addition.status=='ACTIVE').all()
                            b = db.query(models.Payroll_Items_Overtime).filter(models.Payroll_Items_Overtime.status=='ACTIVE').all()
                            c = db.query(models.Payroll_Items_Deducation).filter(models.Payroll_Items_Deducation.status=='ACTIVE').all()
                            db.query(models.Payroll_Items_Overtime).filter(models.Payroll_Items_Overtime.id==edit_id_ovr).update({"Name": edit_ovr_name, "Rate_type_id": edit_ovr_rate_id, "Rate": edit_ovr_rate})
                            db.commit()
                            return templates.TemplateResponse("payroll-items.html",{"request":request,'b':b,'a':a,'c':c})
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
    except JWTError:
            return RedirectResponse('/HrmTool/login/login',status_code=302)
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"detail": "Internal Server Error"}) 
    
@router.post("/edit_deduction")
def edit(request: Request, db: Session = Depends(get_db),edit_id_deduction:str= Form(...),  edit_deduction_name: str = Form(...), edit_unit_calculation_deduction: str = Form(...), edit_deduction_unit_Amount: str = Form(...), edit_deduction_assignee: str = Form(), edit_deduction_dropdwn: str = Form()):
    try:
        if 'loginer_details' in request.session:
            token = request.session['loginer_details']
            try:
                payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
                loginer_id : int= payload.get("empid") 
                try:
                    if loginer_id:
                        emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                        if emp_data.Lock_screen == 'OFF':
                            a = db.query(models.Payroll_Items_Addition).filter(models.Payroll_Items_Addition.status=='ACTIVE').all()
                            b = db.query(models.Payroll_Items_Overtime).filter(models.Payroll_Items_Overtime.status=='ACTIVE').all()
                            c = db.query(models.Payroll_Items_Deducation).filter(models.Payroll_Items_Deducation.status=='ACTIVE').all()
                            db.query(models.Payroll_Items_Deducation).filter(models.Payroll_Items_Deducation.id==edit_id_deduction).update({"Name": edit_deduction_name, "Unit_calculation": edit_unit_calculation_deduction, "Unit_Amount": edit_deduction_unit_Amount, "Assignee_radio": edit_deduction_assignee, "Assignee_drop": edit_deduction_dropdwn})
                            db.commit()
                            return templates.TemplateResponse("payroll-items.html",{"request":request,'b':b,'a':a,'c':c})
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
    except JWTError:
            return RedirectResponse('/HrmTool/login/login',status_code=302)
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"detail": "Internal Server Error"}) 
    

@router.get("/taking_edit_id_addition/{ids}")       
def taking_edit_id_addition(ids:int,request:Request,db: Session = Depends(get_db)):
    try:
        if 'loginer_details' in request.session:
            token = request.session['loginer_details']
            try:
                payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
                loginer_id : int= payload.get("empid") 
                try:
                    if loginer_id:
                        emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                        if emp_data.Lock_screen == 'OFF':
                            single_data = db.query(models.Payroll_Items_Addition).filter(models.Payroll_Items_Addition.id==ids).filter(models.Payroll_Items_Addition.status=='ACTIVE').first()
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
    except JWTError:
            return RedirectResponse('/HrmTool/login/login',status_code=302)
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"detail": "Internal Server Error"}) 
    

@router.get("/taking_edit_id_overtime/{ids}")       
def taking_edit_id_overtime(ids:int,request:Request,db: Session = Depends(get_db)):
    try:
        if 'loginer_details' in request.session:
            token = request.session['loginer_details']
            try:
                payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
                loginer_id : int= payload.get("empid") 
                try:
                    if loginer_id:
                        emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                        if emp_data.Lock_screen == 'OFF':
                            single_data = db.query(models.Payroll_Items_Overtime).filter(models.Payroll_Items_Overtime.id==ids).filter(models.Payroll_Items_Overtime.status=='ACTIVE').first()
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
    except JWTError:
            return RedirectResponse('/HrmTool/login/login',status_code=302)
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"detail": "Internal Server Error"}) 
    
@router.get("/taking_edit_id_deduction/{ids}")       
def taking_edit_id_deduction(ids:int,request:Request,db: Session = Depends(get_db)):
    try:
        if 'loginer_details' in request.session:
            token = request.session['loginer_details']
            try:
                payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
                loginer_id : int= payload.get("empid") 
                try:
                    if loginer_id:
                        emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                        if emp_data.Lock_screen == 'OFF':
                            single_data = db.query(models.Payroll_Items_Deducation).filter(models.Payroll_Items_Deducation.id==ids).filter(models.Payroll_Items_Deducation.status=='ACTIVE').first()
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
    except JWTError:
            return RedirectResponse('/HrmTool/login/login',status_code=302)
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"detail": "Internal Server Error"}) 
    

@router.get("/taking_dlt_id_addition/{ids}")
def taking_dlt_id_addition(request: Request,ids:int,db: Session = Depends(get_db)):
    try:
        if 'loginer_details' in request.session:
            token = request.session['loginer_details']
            try:
                payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
                loginer_id : int= payload.get("empid") 
                try:
                    if loginer_id:
                        emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                        if emp_data.Lock_screen == 'OFF':
                            a = db.query(models.Payroll_Items_Addition).filter(models.Payroll_Items_Addition.status=='ACTIVE').all()
                            b = db.query(models.Payroll_Items_Overtime).filter(models.Payroll_Items_Overtime.status=='ACTIVE').all()
                            c = db.query(models.Payroll_Items_Deducation).filter(models.Payroll_Items_Deducation.status=='ACTIVE').all()
                            db.query(models.Payroll_Items_Addition).filter(models.Payroll_Items_Addition.id == ids).delete()
                            db.commit()
                            return templates.TemplateResponse("payroll-items.html",context={"request":request,'c':c,'a':a,'b':b})
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
    except JWTError:
            return RedirectResponse('/HrmTool/login/login',status_code=302)
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"detail": "Internal Server Error"}) 
    
@router.get("/taking_dlt_id_overtime/{ids}")
def taking_dlt_id_overtime(request: Request,ids:int,db: Session = Depends(get_db)):
    try:
        if 'loginer_details' in request.session:
            token = request.session['loginer_details']
            try:
                payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
                loginer_id : int= payload.get("empid") 
                try:
                    if loginer_id:
                        emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                        if emp_data.Lock_screen == 'OFF':
                            a = db.query(models.Payroll_Items_Addition).filter(models.Payroll_Items_Addition.status=='ACTIVE').all()
                            b = db.query(models.Payroll_Items_Overtime).filter(models.Payroll_Items_Overtime.status=='ACTIVE').all()
                            c = db.query(models.Payroll_Items_Deducation).filter(models.Payroll_Items_Deducation.status=='ACTIVE').all()
                            db.query(models.Payroll_Items_Overtime).filter(models.Payroll_Items_Overtime.id == ids).delete()
                            db.commit()
                            return templates.TemplateResponse("payroll-items.html",context={"request":request,'c':c,'a':a,'b':b})
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
    except JWTError:
            return RedirectResponse('/HrmTool/login/login',status_code=302)
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"detail": "Internal Server Error"}) 
    
@router.get("/taking_dlt_id_deduction/{ids}")
def taking_dlt_id_overtime(request: Request,ids:int,db: Session = Depends(get_db)):
    try:
        if 'loginer_details' in request.session:
            token = request.session['loginer_details']
            try:
                payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
                loginer_id : int= payload.get("empid") 
                try:
                    if loginer_id:
                        emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                        if emp_data.Lock_screen == 'OFF':
                            a = db.query(models.Payroll_Items_Addition).filter(models.Payroll_Items_Addition.status=='ACTIVE').all()
                            b = db.query(models.Payroll_Items_Overtime).filter(models.Payroll_Items_Overtime.status=='ACTIVE').all()
                            c = db.query(models.Payroll_Items_Deducation).filter(models.Payroll_Items_Deducation.status=='ACTIVE').all()
                            db.query(models.Payroll_Items_Deducation).filter(models.Payroll_Items_Deducation.id == ids).update({"status":"INACTIVE"})
                            db.commit()
                            return templates.TemplateResponse("payroll-items.html",context={"request":request,'c':c,'a':a,'b':b})
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
    except JWTError:
            return RedirectResponse('/HrmTool/login/login',status_code=302)
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"detail": "Internal Server Error"}) 


@router.post("/add_overtime")
def add_addition(request: Request, db: Session = Depends(get_db),name: str=Form(...), rate_type: str = Form(...),rate: str = Form(...)):
    try:
        if 'loginer_details' in request.session:
            token = request.session['loginer_details']
            try:
                payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
                loginer_id : int= payload.get("empid") 
                try:
                    if loginer_id:
                        emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                        if emp_data.Lock_screen == 'OFF':
                            body = models.Payroll_Items_Overtime(Name=name,Rate_type_id= rate_type,Rate=rate,status="ACTIVE",created_by=" ")
                            db.add(body)
                            db.commit()
                            return RedirectResponse("/payroll-overtime", status_code=303)
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
    except JWTError:
            return RedirectResponse('/HrmTool/login/login',status_code=302)
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"detail": "Internal Server Error"}) 
    
@router.get("/payroll-overtime")
def add_addition(request: Request, db: Session = Depends(get_db)):
    try:
        if 'loginer_details' in request.session:
            token = request.session['loginer_details']
            try:
                payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
                loginer_id : int= payload.get("empid") 
                try:
                    if loginer_id:
                        emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                        if emp_data.Lock_screen == 'OFF':
                            # a = db.query(models.Payroll_Items_Addition).filter(models.Payroll_Items_Addition.status=='ACTIVE').all()
                            a = db.query(models.Payroll_Items_Addition).filter(models.Payroll_Items_Addition.status=='ACTIVE').all()
                            b = db.query(models.Payroll_Items_Overtime).filter(models.Payroll_Items_Overtime.status=='ACTIVE').all()
                            c = db.query(models.Payroll_Items_Deducation).filter(models.Payroll_Items_Deducation.status=='ACTIVE').all()
                            return templates.TemplateResponse("payroll-items.html",context={"request":request,'b':b,'a':a,'c':c})
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
    except JWTError:
            return RedirectResponse('/HrmTool/login/login',status_code=302)
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"detail": "Internal Server Error"}) 

@router.post("/add_deduction")
def add_addition(request: Request, db: Session = Depends(get_db),name: str=Form(...), unit_calculation_deduction: str = Form(...), unit_amount_deduction: str = Form(...), deduction_assignee: str=Form(...), deduction_radio:str=Form(...)):
    try:
        if 'loginer_details' in request.session:
            token = request.session['loginer_details']
            try:
                payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
                loginer_id : int= payload.get("empid") 
                try:
                    if loginer_id:
                        emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                        if emp_data.Lock_screen == 'OFF':
                            body = models.Payroll_Items_Deducation(Name=name,Unit_calculation= unit_calculation_deduction, Unit_Amount=unit_amount_deduction, Assignee_radio= deduction_assignee, Assignee_drop=deduction_radio, status="ACTIVE",created_by=" ")
                            db.add(body)
                            db.commit()
                            return RedirectResponse("/payroll-deduction", status_code=303)
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
    except JWTError:
            return RedirectResponse('/HrmTool/login/login',status_code=302)
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"detail": "Internal Server Error"}) 
    
@router.get("/payroll-deduction")
def add_addition(request: Request, db: Session = Depends(get_db)):
    try:
        if 'loginer_details' in request.session:
            token = request.session['loginer_details']
            try:
                payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
                loginer_id : int= payload.get("empid") 
                try:
                    if loginer_id:
                        emp_data = db.query(models.Employee).filter(models.Employee.id==loginer_id).filter(models.Employee.status=='ACTIVE').first()
                        if emp_data.Lock_screen == 'OFF':
                            #  a = db.query(models.Payroll_Items_Addition).filter(models.Payroll_Items_Addition.status=='ACTIVE').all()
                            a = db.query(models.Payroll_Items_Addition).filter(models.Payroll_Items_Addition.status=='ACTIVE').all()
                            b = db.query(models.Payroll_Items_Overtime).filter(models.Payroll_Items_Overtime.status=='ACTIVE').all()
                            c = db.query(models.Payroll_Items_Deducation).filter(models.Payroll_Items_Deducation.status=='ACTIVE').all()
                            return templates.TemplateResponse("payroll-items.html",context={"request":request,'c':c,'a':a,'b':b})
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
    except JWTError:
            return RedirectResponse('/HrmTool/login/login',status_code=302)
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"detail": "Internal Server Error"}) 

