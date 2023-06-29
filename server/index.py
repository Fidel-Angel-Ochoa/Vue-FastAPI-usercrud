from fastapi import FastAPI
from routes.user import user
from fastapi.middleware.cors import CORSMiddleware

# this is the app
app= FastAPI(
    title="Vuejs-FastAPI CRUD",
    description="This is a CRUD that use Vuejs, FastAPI and Mysql",
    version="0.1.0",
    openapi_tags=[{
        "name":"Users",
        "description":"CRUD Users Routers"
    }]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://vue-fastapi-usercrud.pages.dev"],
    allow_credentials= True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# here we said that in the app include de routes that are in user
app.include_router(user)