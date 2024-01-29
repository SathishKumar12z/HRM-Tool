from sqlalchemy import Boolean, Column, ForeignKey,  String, DateTime, LargeBinary,func
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Time,Date,DateTime,BLOB, JSON,Float
from sqlalchemy.orm import relationship
from datetime import datetime
from models import engine
import bcrypt
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Employee(Base):
   
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True, index=True)

    First_Name = Column(String(255), nullable=False, index=True)
    Last_Name = Column(String(255), nullable=False, index=True)
    Username = Column(String(255), nullable=False, index=True)
    Email = Column(String(255), nullable=False, index=True)
    Password = Column(String(255), nullable=False, index=True)
    Employee_ID = Column(String(255), nullable=False, index=True)
    Joining_Date = Column(String(255), nullable=False, index=True)
    Phone = Column(String(255), nullable=False, index=True)
    Company_id = Column(String(255), nullable=False, index=True)
    Department_id = Column(String(255), nullable=False, index=True)
    Designation_id = Column(String(255), nullable=False, index=True)
    Current_status = Column(String(255), nullable=False, index=True)
    #------>... Profile 
    Birth_Date = Column(String(255), nullable=False, index=True)
    Gender = Column(String(255), nullable=False, index=True)
    Address = Column(String(255), nullable=False, index=True)
    State = Column(String(255), nullable=False, index=True)
    Country = Column(String(255), nullable=False, index=True)
    Pin_Code = Column(String(255), nullable=False, index=True)
    Reports_To = Column(String(255), nullable=False, index=True)
    Photo = Column(String(255), nullable=False, index=True)
    Lock_screen = Column(String(255), nullable=False, index=True)
    #------>... others 
    # role_permission = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    def hash_password(self, Password):
        self.Password = bcrypt.hashpw(Password.encode('utf-8'), bcrypt.gensalt(14))
     
    def verify_password(self, Password):
        if bcrypt.checkpw(Password,(self.Password).encode('utf-8')):
            return True
        else:
            return False

class Holiday_List(Base):
   
    __tablename__ = "holiday_list"

    id = Column(Integer, primary_key=True, index=True)

    Name = Column(String(255), nullable=False, index=True)
    Date = Column(String(255), nullable=False, index=True)
    Current_status = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())


class Department(Base):
   
    __tablename__ = "department"

    id = Column(Integer, primary_key=True, index=True)

    Name = Column(String(255), nullable=False, index=True)
    Current_status = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Designation(Base):
   
    __tablename__ = "designation"

    id = Column(Integer, primary_key=True, index=True)

    Name = Column(String(255), nullable=False, index=True)
    Department_id = Column(String(255), nullable=False, index=True)
    Current_status = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Timesheet(Base):
   
    __tablename__ = "timesheet"

    id = Column(Integer, primary_key=True, index=True)

    Employee_id = Column(String(255), nullable=False, index=True)
    Project_id = Column(String(255), nullable=False, index=True)
    Deadline  = Column(String(255), nullable=False, index=True)
    Total_Hours  = Column(String(255), nullable=False, index=True)
    Remaining_Hours  = Column(String(255), nullable=False, index=True)
    Date  = Column(String(255), nullable=False, index=True)
    Hours  = Column(String(255), nullable=False, index=True)
    Description  = Column(String(255), nullable=False, index=True)
    Current_status = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Client(Base):
   
    __tablename__ = "client"

    id = Column(Integer, primary_key=True, index=True)

    First_Name = Column(String(255), nullable=False, index=True)
    Last_Name = Column(String(255), nullable=False, index=True)
    Username  = Column(String(255), nullable=False, index=True)
    Email   = Column(String(255), nullable=False, index=True)
    Password  = Column(String(255), nullable=False, index=True)
    Client_ID  = Column(String(255), nullable=False, index=True)
    Phone  = Column(String(255), nullable=False, index=True)
    Company_Name  = Column(String(255), nullable=False, index=True)
    Photo  = Column(String(255), nullable=False, index=True)
    current_status  = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Project(Base):
   
    __tablename__ = "project"

    id = Column(Integer, primary_key=True, index=True)

    Project_Name = Column(String(255), nullable=False, index=True)
    Client_id = Column(String(255), nullable=False, index=True)
    Start_Date  = Column(String(255), nullable=False, index=True)
    End_Date   = Column(String(255), nullable=False, index=True)
    Rate  = Column(String(255), nullable=False, index=True)
    Priority  = Column(String(255), nullable=False, index=True)
    Phone  = Column(String(255), nullable=False, index=True)
    Project_Leader_id  = Column(String(255), nullable=False, index=True)
    Teams  = Column(String(255), nullable=False, index=True)
    Description  = Column(String(255), nullable=False, index=True)
    File  = Column(String(255), nullable=False, index=True)
    Current_status = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Project_Workers(Base):
   
    __tablename__ = "project_worker"

    id = Column(Integer, primary_key=True, index=True)

    Project_id = Column(String(255), nullable=False, index=True)
    Employee_id = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Task(Base):
   
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255), nullable=False, index=True)
    Current_status = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Tickets(Base):
   
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)

    Ticket_Subject = Column(String(255), nullable=False, index=True)
    Ticket_Id = Column(String(255), nullable=False, index=True)
    Employee_id = Column(String(255), nullable=False, index=True)
    Client_id = Column(String(255), nullable=False, index=True)
    Priority = Column(String(255), nullable=False, index=True)
    CC = Column(String(255), nullable=False, index=True)
    Assign_id = Column(String(255), nullable=False, index=True)
    Description = Column(String(255), nullable=False, index=True)
    Files = Column(String(255), nullable=False, index=True)
    Current_status = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Tickets_Followers(Base):
   
    __tablename__ = "tickets_followers"

    id = Column(Integer, primary_key=True, index=True)

    Ticket_id = Column(String(255), nullable=False, index=True)
    Employee_id = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Estimate(Base):
   
    __tablename__ = "estimate"

    id = Column(Integer, primary_key=True, index=True)

    Client_id = Column(String(255), nullable=False, index=True)
    Project_id = Column(String(255), nullable=False, index=True)
    Email = Column(String(255), nullable=False, index=True)
    Tax = Column(String(255), nullable=False, index=True)
    Biling_address = Column(String(255), nullable=False, index=True)
    Estimate_Date = Column(String(255), nullable=False, index=True)
    Expiry_Date = Column(String(255), nullable=False, index=True)
    Total = Column(String(255), nullable=False, index=True)
    Tax = Column(String(255), nullable=False, index=True)
    Discount  = Column(String(255), nullable=False, index=True)
    Grand_Total = Column(String(255), nullable=False, index=True)
    Information = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Estimate_Items(Base):
   
    __tablename__ = "estimate_items"

    id = Column(Integer, primary_key=True, index=True)

    Estimate_id = Column(String(255), nullable=False, index=True)
    Item = Column(String(255), nullable=False, index=True)
    Description = Column(String(255), nullable=False, index=True)
    Unit_Cost = Column(String(255), nullable=False, index=True)
    Qty = Column(String(255), nullable=False, index=True)
    Amount = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Invoice(Base):
   
    __tablename__ = "invoice"

    id = Column(Integer, primary_key=True, index=True)

    Client_id = Column(String(255), nullable=False, index=True)
    Project_id = Column(String(255), nullable=False, index=True)
    Email = Column(String(255), nullable=False, index=True)
    Tax = Column(String(255), nullable=False, index=True)
    Biling_address = Column(String(255), nullable=False, index=True)
    Estimate_Date = Column(String(255), nullable=False, index=True)
    Expiry_Date = Column(String(255), nullable=False, index=True)
    Total = Column(String(255), nullable=False, index=True)
    Tax = Column(String(255), nullable=False, index=True)
    Discount  = Column(String(255), nullable=False, index=True)
    Grand_Total = Column(String(255), nullable=False, index=True)
    Information = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Invoice_Items(Base):
   
    __tablename__ = "invoice_items"

    id = Column(Integer, primary_key=True, index=True)

    Invoice_id = Column(String(255), nullable=False, index=True)
    Item = Column(String(255), nullable=False, index=True)
    Description = Column(String(255), nullable=False, index=True)
    Unit_Cost = Column(String(255), nullable=False, index=True)
    Qty = Column(String(255), nullable=False, index=True)
    Amount = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Expenses(Base):
   
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)

    Client_id = Column(String(255), nullable=False, index=True)
    Project_id = Column(String(255), nullable=False, index=True)
    Email = Column(String(255), nullable=False, index=True)
    Tax = Column(String(255), nullable=False, index=True)
    Biling_address = Column(String(255), nullable=False, index=True)
    Estimate_Date = Column(String(255), nullable=False, index=True)
    Expiry_Date = Column(String(255), nullable=False, index=True)
    Total = Column(String(255), nullable=False, index=True)
    Tax = Column(String(255), nullable=False, index=True)
    Discount  = Column(String(255), nullable=False, index=True)
    Grand_Total = Column(String(255), nullable=False, index=True)
    Information = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Expenses_Items(Base):
   
    __tablename__ = "expenses_items"

    id = Column(Integer, primary_key=True, index=True)

    Expenses_id = Column(String(255), nullable=False, index=True)
    Item = Column(String(255), nullable=False, index=True)
    Description = Column(String(255), nullable=False, index=True)
    Unit_Cost = Column(String(255), nullable=False, index=True)
    Qty = Column(String(255), nullable=False, index=True)
    Amount = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())


class Payment(Base):
   
    __tablename__ = "payment"

    id = Column(Integer, primary_key=True, index=True)

    Client_id = Column(String(255), nullable=False, index=True)
    Project_id = Column(String(255), nullable=False, index=True)
    Email = Column(String(255), nullable=False, index=True)
    Tax = Column(String(255), nullable=False, index=True)
    Biling_address = Column(String(255), nullable=False, index=True)
    Estimate_Date = Column(String(255), nullable=False, index=True)
    Expiry_Date = Column(String(255), nullable=False, index=True)
    Total = Column(String(255), nullable=False, index=True)
    Tax = Column(String(255), nullable=False, index=True)
    Discount  = Column(String(255), nullable=False, index=True)
    Grand_Total = Column(String(255), nullable=False, index=True)
    Information = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Payment_Items(Base):
   
    __tablename__ = "payment_items"

    id = Column(Integer, primary_key=True, index=True)

    Payment_id = Column(String(255), nullable=False, index=True)
    Item = Column(String(255), nullable=False, index=True)
    Description = Column(String(255), nullable=False, index=True)
    Unit_Cost = Column(String(255), nullable=False, index=True)
    Qty = Column(String(255), nullable=False, index=True)
    Amount = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())


class Taxes(Base):
   
    __tablename__ = "taxes"

    id = Column(Integer, primary_key=True, index=True)

    Tax_Name = Column(String(255), nullable=False, index=True)
    Tax_Percentage = Column(String(255), nullable=False, index=True)
    Current_Status  = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Provident_Fund(Base):
   
    __tablename__ = "provident_fund"

    id = Column(Integer, primary_key=True, index=True)

    Employee_id = Column(String(255), nullable=False, index=True)
    Fund_Type_id = Column(String(255), nullable=False, index=True)
    Employee_Share  = Column(String(255), nullable=False, index=True)
    Organization_Share  = Column(String(255), nullable=False, index=True)
    Employee_Share  = Column(String(255), nullable=False, index=True)
    Employee_percentage  = Column(String(255), nullable=False, index=True)
    Organization_percentage  = Column(String(255), nullable=False, index=True)
    Description  = Column(String(255), nullable=False, index=True)
    current_status  = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Categories(Base):
   
    __tablename__ = "Categories"

    id = Column(Integer, primary_key=True, index=True)

    Name = Column(String(255), nullable=False, index=True)
    SubCategory_id = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Sub_Category(Base):
   
    __tablename__ = "sub_category"

    id = Column(Integer, primary_key=True, index=True)

    Category_id = Column(String(255), nullable=False, index=True)
    Name = Column(String(255), nullable=False, index=True)
    current_status = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Budget(Base):
   
    __tablename__ = "budget"

    id = Column(Integer, primary_key=True, index=True)

    Budget_Title = Column(String(255), nullable=False, index=True)
    Budget_Type = Column(String(255), nullable=False, index=True)
    Start_Date = Column(String(255), nullable=False, index=True)
    End_Date = Column(String(255), nullable=False, index=True)
    Revenue_Title = Column(String(255), nullable=False, index=True)
    Revenue_Amount = Column(String(255), nullable=False, index=True)
    Overall_Revenues = Column(String(255), nullable=False, index=True)
    Expenses_Title = Column(String(255), nullable=False, index=True)
    Expenses_Amount = Column(String(255), nullable=False, index=True)
    Overall_Expense = Column(String(255), nullable=False, index=True)
    Expected_Profit = Column(String(255), nullable=False, index=True)
    Tax  = Column(String(255), nullable=False, index=True)
    Budget_Amount = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Budget_Expenses(Base):
   
    __tablename__ = "budget_expenses"

    id = Column(Integer, primary_key=True, index=True)

    Amount  = Column(String(255), nullable=False, index=True)
    Currency = Column(String(255), nullable=False, index=True)
    Notes  = Column(String(255), nullable=False, index=True)
    Expense_Date = Column(String(255), nullable=False, index=True)
    Category_id = Column(String(255), nullable=False, index=True)
    Sub_Category_id = Column(String(255), nullable=False, index=True)
    File = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Budget_Revenues(Base):
   
    __tablename__ = "budget_revenues"

    id = Column(Integer, primary_key=True, index=True)

    Amount  = Column(String(255), nullable=False, index=True)
    Currency = Column(String(255), nullable=False, index=True)
    Notes  = Column(String(255), nullable=False, index=True)
    Revenue_Date = Column(String(255), nullable=False, index=True)
    Category_id = Column(String(255), nullable=False, index=True)
    Sub_Category_id = Column(String(255), nullable=False, index=True)
    File = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Employee_Salary(Base):
   
    __tablename__ = "employee_salary"

    id = Column(Integer, primary_key=True, index=True)

    Employee_id  = Column(String(255), nullable=False, index=True)
    Net_Salary = Column(String(255), nullable=False, index=True)
    Basic  = Column(String(255), nullable=False, index=True)
    TDS = Column(String(255), nullable=False, index=True)
    DA_40 = Column(String(255), nullable=False, index=True)
    ESI = Column(String(255), nullable=False, index=True)
    HRA_15 = Column(String(255), nullable=False, index=True)
    PF = Column(String(255), nullable=False, index=True)
    Conveyance = Column(String(255), nullable=False, index=True)
    Leave = Column(String(255), nullable=False, index=True)
    Allowance = Column(String(255), nullable=False, index=True)
    Prof_Tax = Column(String(255), nullable=False, index=True)
    Medical_Allowance = Column(String(255), nullable=False, index=True)
    Labour_Welfare = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Payroll_Items(Base):
   
    __tablename__ = "payroll_items"

    id = Column(Integer, primary_key=True, index=True)

    Name   = Column(String(255), nullable=False, index=True)
    Category  = Column(String(255), nullable=False, index=True)
    Unit_calculation  = Column(String(255), nullable=False, index=True)
    Unit_Amount = Column(String(255), nullable=False, index=True)
    Assignee = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Policies(Base):
   
    __tablename__ = "policies"

    id = Column(Integer, primary_key=True, index=True)

    Name   = Column(String(255), nullable=False, index=True)
    Description   = Column(String(255), nullable=False, index=True)
    Department  = Column(String(255), nullable=False, index=True)
    File = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Performance_Indicator(Base):
   
    __tablename__ = "performance_indicator"

    id = Column(Integer, primary_key=True, index=True)

    Designation_id   = Column(String(255), nullable=False, index=True)
    Customer_Experience   = Column(String(255), nullable=False, index=True)
    Marketing  = Column(String(255), nullable=False, index=True)
    Management = Column(String(255), nullable=False, index=True)
    Administration = Column(String(255), nullable=False, index=True)
    Presentation_Skill = Column(String(255), nullable=False, index=True)
    Quality_Of_Work = Column(String(255), nullable=False, index=True)
    Efficiency = Column(String(255), nullable=False, index=True)
    Integrity = Column(String(255), nullable=False, index=True)
    Professionalism = Column(String(255), nullable=False, index=True)
    Team_Work = Column(String(255), nullable=False, index=True)
    Critical_Thinking = Column(String(255), nullable=False, index=True)
    Conflict_Management = Column(String(255), nullable=False, index=True)
    Attendance = Column(String(255), nullable=False, index=True)
    Meet_Deadline = Column(String(255), nullable=False, index=True)
    Current_status = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Performance_Appraisal(Base):
   
    __tablename__ = "performance_appraisal"

    id = Column(Integer, primary_key=True, index=True)

    Employee_id   = Column(String(255), nullable=False, index=True)
    Date    = Column(String(255), nullable=False, index=True)
    Customer_Experience_Value  = Column(String(255), nullable=False, index=True)
    Marketing_Value = Column(String(255), nullable=False, index=True)
    Management_Value = Column(String(255), nullable=False, index=True)
    Administration_Value = Column(String(255), nullable=False, index=True)
    Presentation_Skill_Value = Column(String(255), nullable=False, index=True)
    Quality_Of_Work_Value = Column(String(255), nullable=False, index=True)
    Efficiency_Value = Column(String(255), nullable=False, index=True)
    Integrity_Value = Column(String(255), nullable=False, index=True)
    Professionalism_Value = Column(String(255), nullable=False, index=True)
    Team_Work_Value = Column(String(255), nullable=False, index=True)
    Critical_Thinking_Value = Column(String(255), nullable=False, index=True)
    Conflict_Management_Value = Column(String(255), nullable=False, index=True)
    Attendance_Value = Column(String(255), nullable=False, index=True)
    Meet_Deadline_Value = Column(String(255), nullable=False, index=True)
    Current_status = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Goal_Tracking(Base):
   
    __tablename__ = "goal_tracking"

    id = Column(Integer, primary_key=True, index=True)

    Goal_Type_id   = Column(String(255), nullable=False, index=True)
    Subject    = Column(String(255), nullable=False, index=True)
    Target_Achievement   = Column(String(255), nullable=False, index=True)
    Start_Date = Column(String(255), nullable=False, index=True)
    End_Date = Column(String(255), nullable=False, index=True)
    Description  = Column(String(255), nullable=False, index=True)
    Current_status = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Goal_Type(Base):
   
    __tablename__ = "goal_type"

    id = Column(Integer, primary_key=True, index=True)

    Name   = Column(String(255), nullable=False, index=True)
    Description     = Column(String(255), nullable=False, index=True)
    Current_status = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Training(Base):
   
    __tablename__ = "training"

    id = Column(Integer, primary_key=True, index=True)

    Training_Type_id   = Column(String(255), nullable=False, index=True)
    Trainer_id     = Column(String(255), nullable=False, index=True)
    Employees_id = Column(String(255), nullable=False, index=True)
    Training_Cost = Column(String(255), nullable=False, index=True)
    Start_Date = Column(String(255), nullable=False, index=True)
    End_Date = Column(String(255), nullable=False, index=True)
    Description  = Column(String(255), nullable=False, index=True)
    Current_status = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Trainers(Base):
   
    __tablename__ = "trainers"

    id = Column(Integer, primary_key=True, index=True)

    First_Name   = Column(String(255), nullable=False, index=True)
    Last_Name     = Column(String(255), nullable=False, index=True)
    Role_id = Column(String(255), nullable=False, index=True)
    Email  = Column(String(255), nullable=False, index=True)
    Phone = Column(String(255), nullable=False, index=True)
    Description  = Column(String(255), nullable=False, index=True)
    Photo  = Column(String(255), nullable=False, index=True)
    Current_status = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Training_Type(Base):
   
    __tablename__ = "training_type"

    id = Column(Integer, primary_key=True, index=True)

    Name    = Column(String(255), nullable=False, index=True)
    Description  = Column(String(255), nullable=False, index=True)
    Current_status = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Promotion(Base):
   
    __tablename__ = "promotion"

    id = Column(Integer, primary_key=True, index=True)

    Promotion_For    = Column(String(255), nullable=False, index=True)
    Promotion_From  = Column(String(255), nullable=False, index=True)
    Promotion_To = Column(String(255), nullable=False, index=True)
    Promotion_Date = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Resignation(Base):
   
    __tablename__ = "resignation"

    id = Column(Integer, primary_key=True, index=True)

    Employee_id    = Column(String(255), nullable=False, index=True)
    Notice_Date  = Column(String(255), nullable=False, index=True)
    Date  = Column(String(255), nullable=False, index=True)
    Reason  = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Termination(Base):
   
    __tablename__ = "termination"

    id = Column(Integer, primary_key=True, index=True)

    Employee_id    = Column(String(255), nullable=False, index=True)
    Termination_Type_id  = Column(String(255), nullable=False, index=True)
    Date  = Column(String(255), nullable=False, index=True)
    Reason  = Column(String(255), nullable=False, index=True)
    Notice_Date  = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Termination_Type(Base):
   
    __tablename__ = "termination_type"

    id = Column(Integer, primary_key=True, index=True)

    Name    = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Asset(Base):
   
    __tablename__ = "asset"

    id = Column(Integer, primary_key=True, index=True)

    Asset_Name = Column(String(255), nullable=False, index=True)
    Asset_Id = Column(String(255), nullable=False, index=True)
    Purchase_Date = Column(String(255), nullable=False, index=True)
    Purchase_From = Column(String(255), nullable=False, index=True)
    Manufacturer = Column(String(255), nullable=False, index=True)
    Model = Column(String(255), nullable=False, index=True)
    Serial_Number = Column(String(255), nullable=False, index=True)
    Supplier = Column(String(255), nullable=False, index=True)
    Condition = Column(String(255), nullable=False, index=True)
    Warranty = Column(String(255), nullable=False, index=True)
    Value = Column(String(255), nullable=False, index=True)
    Asset_User_id = Column(String(255), nullable=False, index=True)
    Current_status = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Users(Base):
   
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    First_Name = Column(String(255), nullable=False, index=True)
    Last_Name = Column(String(255), nullable=False, index=True)
    Username  = Column(String(255), nullable=False, index=True)
    Email  = Column(String(255), nullable=False, index=True)
    Password = Column(String(255), nullable=False, index=True)
    Phone = Column(String(255), nullable=False, index=True)
    Role_id = Column(String(255), nullable=False, index=True)
    Company = Column(String(255), nullable=False, index=True)
    Employee_ID = Column(String(255), nullable=False, index=True)
    Photo = Column(String(255), nullable=False, index=True)
    Value = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Company_Settings(Base):
   
    __tablename__ = "company_settings"

    id = Column(Integer, primary_key=True, index=True)

    Company_Name = Column(String(255), nullable=False, index=True)
    Contact_Person = Column(String(255), nullable=False, index=True)
    Address  = Column(String(255), nullable=False, index=True)
    Country  = Column(String(255), nullable=False, index=True)
    City = Column(String(255), nullable=False, index=True)
    State = Column(String(255), nullable=False, index=True)
    Postal_Code = Column(String(255), nullable=False, index=True)
    Email = Column(String(255), nullable=False, index=True)
    Phone_Number = Column(String(255), nullable=False, index=True)
    Mobile_Number = Column(String(255), nullable=False, index=True)
    Fax = Column(String(255), nullable=False, index=True)
    Website_Url = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Localization_Settings(Base):
   
    __tablename__ = "localization_settings"

    id = Column(Integer, primary_key=True, index=True)

    Default_Country = Column(String(255), nullable=False, index=True)
    Date_Format  = Column(String(255), nullable=False, index=True)
    Timezone  = Column(String(255), nullable=False, index=True)
    Default_Language = Column(String(255), nullable=False, index=True)
    Currency_Code = Column(String(255), nullable=False, index=True)
    Currency_Symbol = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    
class Theme_Settings(Base):
   
    __tablename__ = "theme_settings"

    id = Column(Integer, primary_key=True, index=True)

    Website_Name = Column(String(255), nullable=False, index=True)
    Light_Logo  = Column(String(255), nullable=False, index=True)
    Favicon  = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
     
class Roles_Permissions(Base):
   
    __tablename__ = "roles_permissions"

    id = Column(Integer, primary_key=True, index=True)

    Role_id = Column(String(255), nullable=False, index=True)
    Module_Access  = Column(String(255), nullable=False, index=True)
    Module_Permission  = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
        
class PHP_Email(Base):
   
    __tablename__ = "php_email"

    id = Column(Integer, primary_key=True, index=True)

    Email  = Column(String(255), nullable=False, index=True)
    Name  = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
       
class SMTP_Email(Base):
   
    __tablename__ = "smtp_email"

    id = Column(Integer, primary_key=True, index=True)

    SMTP_HOST  = Column(String(255), nullable=False, index=True)
    SMTP_USER  = Column(String(255), nullable=False, index=True)
    SMTP_PASSWORD  = Column(String(255), nullable=False, index=True)
    SMTP_PORT  = Column(String(255), nullable=False, index=True)
    SMTP_Security  = Column(String(255), nullable=False, index=True)
    Authentication_Domain  = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
       
class Invoice_Settings(Base):
   
    __tablename__ = "invoice_settings"

    id = Column(Integer, primary_key=True, index=True)

    Invoice_prefix  = Column(String(255), nullable=False, index=True)
    Invoice_Logo  = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
         
class Salary_Settings(Base):
   
    __tablename__ = "salary_settings"

    id = Column(Integer, primary_key=True, index=True)

    DA  = Column(String(255), nullable=False, index=True)
    HRA  = Column(String(255), nullable=False, index=True)
    DA_HRA_Switch  = Column(String(255), nullable=False, index=True)#button
    Employee_Share  = Column(String(255), nullable=False, index=True)
    Organization_Share  = Column(String(255), nullable=False, index=True)
    Fund_Settings_switch  = Column(String(255), nullable=False, index=True)#button
    Employee_ESI  = Column(String(255), nullable=False, index=True)
    Organization_ESI  = Column(String(255), nullable=False, index=True)
    ESI_Switch  = Column(String(255), nullable=False, index=True)#button

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
            
class TDS_Data(Base):
   
    __tablename__ = "tds_data"

    id = Column(Integer, primary_key=True, index=True)

    Salary_Settings_id  = Column(String(255), nullable=False, index=True)
    TDS_Switch  = Column(String(255), nullable=False, index=True)
    Salary_From  = Column(String(255), nullable=False, index=True)
    Salary_To  = Column(String(255), nullable=False, index=True)
    Percentage  = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
             
class Notifications_Settings(Base):
   
    __tablename__ = "notification_settings"

    id = Column(Integer, primary_key=True, index=True)

    Name  = Column(String(255), nullable=False, index=True)
    Current_status  = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
              
class Leave_Type(Base):
   
    __tablename__ = "leave_type"

    id = Column(Integer, primary_key=True, index=True)

    Name  = Column(String(255), nullable=False, index=True)
    days   = Column(String(255), nullable=False, index=True)
    Current_status  = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
                
class ToxBox_Setting(Base):
   
    __tablename__ = "ToxBox_Setting"

    id = Column(Integer, primary_key=True, index=True)

    ApiKey   = Column(String(255), nullable=False, index=True)
    ApiSecret    = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
                  
class Cron_Setting(Base):
   
    __tablename__ = "cron_setting"

    id = Column(Integer, primary_key=True, index=True)

    Cron_Key   = Column(String(255), nullable=False, index=True)
    Auto_Backup    = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
                    
class Register(Base):
   
    __tablename__ = "register"

    id = Column(Integer, primary_key=True, index=True)

    Email   = Column(String(255), nullable=False, index=True)
    Password  = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
                      
class Subscriptions(Base):
   
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)

    Plan_Name   = Column(String(255), nullable=False, index=True)
    Plan_Amount  = Column(String(255), nullable=False, index=True)
    Plan_Type  = Column(String(255), nullable=False, index=True)
    Users_No  = Column(String(255), nullable=False, index=True)
    Projects_No  = Column(String(255), nullable=False, index=True)
    Storage_Space_No  = Column(String(255), nullable=False, index=True)
    Description  = Column(String(255), nullable=False, index=True)
    Current_status  = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
                         
class FAQ(Base):
   
    __tablename__ = "faq"

    id = Column(Integer, primary_key=True, index=True)

    Question   = Column(String(255), nullable=False, index=True)
    Answer  = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
                             
class Terms_of_Service(Base):
   
    __tablename__ = "terms_of_service"

    id = Column(Integer, primary_key=True, index=True)

    Text   = Column(String(255), nullable=False, index=True)
    File  = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
                               
class Privacy_Policy(Base):
   
    __tablename__ = "privacy_policy"

    id = Column(Integer, primary_key=True, index=True)

    Text   = Column(String(255), nullable=False, index=True)
    File  = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())


#-------------------------------------->>>>> kasvishka
    

class Payroll_Items_Addition(Base):
   
    __tablename__ = "payroll_items_addition"

    id = Column(Integer, primary_key=True, index=True)

    Name   = Column(String(255), nullable=False, index=True)
    Category  = Column(String(255), nullable=False, index=True)
    Unit_calculation  = Column(String(255), nullable=False, index=True)
    Unit_Amount = Column(String(255), nullable=False, index=True)
    Assignee_radio = Column(String(255), nullable=False, index=True)
    Assignee_drop = Column(String(255), nullable=False,index=True) #added ths attribute


    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Payroll_Items_Overtime(Base):
   
    __tablename__ = "payroll_items_overtime"

    id = Column(Integer, primary_key=True, index=True)

    Name   = Column(String(255), nullable=False, index=True)
    Rate_type_id  = Column(String(255), nullable=False, index=True)
    Rate = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Rate_Type(Base):
   
    __tablename__ = "rate_type"

    id = Column(Integer, primary_key=True, index=True)

    Name   = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Payroll_Items_Deducation(Base):
   
    __tablename__ = "payroll_items_deducation"

    id = Column(Integer, primary_key=True, index=True)

    Name   = Column(String(255), nullable=False, index=True)
    Unit_calculation  = Column(String(255), nullable=False, index=True)
    Unit_Amount = Column(String(255), nullable=False, index=True)
    Assignee_radio = Column(String(255), nullable=False, index=True)
    Assignee_drop = Column(String(255), nullable=False,index=True) #added ths attribute
    
    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    
class Task_Board_Task (Base):

    __tablename__ = 'board_task'

    id = Column(Integer,primary_key=True,index=True)
    Name = Column(String(255), nullable=False, index=True)
    Priority = Column(String(255), nullable=False, index=True)
    task_id=Column(String(255), nullable=False,index=True) #added
    Due_Date = Column(String(255), nullable=False, index=True)
    Task_Followers = Column(String(255), nullable=False, index=True)
    
    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    
class Task_Board (Base):

    __tablename__ = "task_board"

    id = Column(Integer,primary_key=True,index=True)
    Name = Column(String(255), nullable=False, index=True)
    Colour = Column(String(100),  nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)#ACTIVE,INACTIVE
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

                           
class Interview_Questions(Base):
   
    __tablename__ = "interview_questions"

    id = Column(Integer, primary_key=True, index=True)

    Category_ID   = Column(String(255), nullable=False, index=True)
    Department_ID   = Column(String(255), nullable=False, index=True)
    Question   = Column(String(255), nullable=False, index=True)
    OPtion_A   = Column(String(255), nullable=False, index=True)
    OPtion_B   = Column(String(255), nullable=False, index=True)
    OPtion_C  = Column(String(255), nullable=False, index=True)
    OPtion_D  = Column(String(255), nullable=False, index=True)
    Correct_Answer  = Column(String(255), nullable=False, index=True)
    Code_Snippets  = Column(String(255), nullable=False, index=True)
    Answer_Explanation  = Column(String(255), nullable=False, index=True)
    Video_Link  = Column(String(255), nullable=False, index=True)
    Image   = Column(String(255), nullable=False, index=True)

    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
                           
class Question_Category(Base):
   
    __tablename__ = "question_category"

    id = Column(Integer, primary_key=True, index=True)
    Name   = Column(String(255), nullable=False, index=True)
    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())



class Employee_Leave(Base):
   
    __tablename__ = "employee_leave"

    id = Column(Integer, primary_key=True, index=True)

    Employee_id   = Column(String(255), nullable=False, index=True)
    Type_id   = Column(String(255), nullable=False, index=True)
    From_date  = Column(String(255), nullable=False, index=True)
    To_date = Column(String(255), nullable=False, index=True)
    Days_count = Column(String(255), nullable=False, index=True)
    Remaining_days = Column(String(255), nullable=False,index=True) #added ths attribute
    Reasons = Column(String(255), nullable=False,index=True) #added ths attribute
    
    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Employee_Personal_Info(Base):
   
    __tablename__ = "employee_personal_info"

    id = Column(Integer, primary_key=True, index=True)

    Employee_ID   = Column(String(255), nullable=False, index=True)
    Passport_No   = Column(String(255), nullable=False, index=True)
    Passport_Exp_Date   = Column(String(255), nullable=False, index=True)
    Tel  = Column(String(255), nullable=False, index=True)
    Nationality = Column(String(255), nullable=False, index=True)
    Religion = Column(String(255), nullable=False, index=True)
    Marital_status = Column(String(255), nullable=False,index=True) 
    spouse = Column(String(255), nullable=False,index=True) 
    No_children = Column(String(255), nullable=False,index=True) 
    
    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Emergency_Contact(Base):
   
    __tablename__ = "emergency_contact"

    id = Column(Integer, primary_key=True, index=True)

    Employee_ID   = Column(String(255), nullable=False, index=True)
    Primary_Name    = Column(String(255), nullable=False, index=True)
    Primary_Relationship     = Column(String(255), nullable=False, index=True)
    Primary_Phone    = Column(String(255), nullable=False, index=True)
    Primary_Phone_II = Column(String(255), nullable=False, index=True)
    Secondary_Name = Column(String(255), nullable=False, index=True)
    Secondary_Relationship = Column(String(255), nullable=False,index=True) 
    Secondary_Phone = Column(String(255), nullable=False,index=True) 
    Secondary_Phone_II = Column(String(255), nullable=False,index=True) 
    
    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    
class Education_Informations(Base):
   
    __tablename__ = "education_informations"

    id = Column(Integer, primary_key=True, index=True)

    Employee_ID   = Column(String(255), nullable=False, index=True)
    Institution    = Column(String(255), nullable=False, index=True)
    Subject     = Column(String(255), nullable=False, index=True)
    Starting_Date    = Column(String(255), nullable=False, index=True)
    Complete_Date = Column(String(255), nullable=False, index=True)
    Degree = Column(String(255), nullable=False, index=True)
    Grade = Column(String(255), nullable=False,index=True) 
    
    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    
Base.metadata.create_all(bind=engine)


    
class Experience_Informations(Base):
   
    __tablename__ = "experience_informations"

    id = Column(Integer, primary_key=True, index=True)

    Employee_ID   = Column(String(255), nullable=False, index=True)
    Company_Name    = Column(String(255), nullable=False, index=True)
    Location     = Column(String(255), nullable=False, index=True)
    Job_Position    = Column(String(255), nullable=False, index=True)
    Period_From = Column(String(255), nullable=False, index=True)
    Period_To = Column(String(255), nullable=False, index=True)
    
    status = Column(String(255), nullable=False, index=True)
    created_by = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

                        