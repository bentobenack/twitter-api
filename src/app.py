
from fastapi import FastAPI, status
# from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

from api.v1.users.routes.user import user as user_router
from api.v1.tweets.routes.tweet import tweet as tweet_router
from api.v1.auth.routes.auth import auth as auth_router
from api.v1.files.routes.file import file as file_router
from config.db_config import Base, engine

app = FastAPI(
    title="Twitter API",
    description="This is a copy of Twitter API",
    version="0.0.1",
    openapi_tags=[
        {
            "name": "Users",
            "description": "Users Routes",
        },
        {
            "name": "Tweets",
            "description": "Tweets Routes",
        }
    ]
)

@app.get(path="/", status_code=status.HTTP_200_OK, tags=["Home"])
def home():
    return {"message": "Welcome to Twitter API"}

app.include_router(user_router, prefix="/api/v1/users")
app.include_router(tweet_router, prefix="/api/v1/tweets")
app.include_router(auth_router, prefix="/api/v1/auth")
app.include_router(file_router, prefix="/api/v1/files")

Base.metadata.create_all(bind=engine)

    
    
# app.add_middleware(HTTPSRedirectMiddleware)

    

