from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from routes import router

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates 
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI(title="Hrm Tool",version="1.00")
templates = Jinja2Templates(directory="templates")

app.add_middleware(

    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(SessionMiddleware, secret_key="some-random-string")

app.mount("/templates/assets", StaticFiles(directory="templates/assets"), name="assets")#english
app.mount("/templates/assets_2", StaticFiles(directory="templates/assets_2"), name="assets_2")#english


# GET operation at route '/'
@app.get('/Error')   
def root_api(request:Request):
    return templates.TemplateResponse('Admin/Pages/Error/error-500.html',context={'request': request})

# GET operation at route '/'
@app.get('/')   
def root_api():
    return {"message": "Welcome to our Project"}

app.include_router(router, prefix='/HrmTool')



my_routers  = app.router.routes

all_urls = []

# Define a catch-all route that will match any path not explicitly defined
@app.get("/{path:path}")
def catch_all(path: str,request:Request):
    if path not in all_urls:
        return templates.TemplateResponse('Admin/Pages/Error/error-404.html',context={'request': request})

for i in my_routers:
    all_urls.append(i.path)