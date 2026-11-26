from fastapi import FastAPI

from routers.series import router as series_router

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


@app.get("/")
def inicio():
    return {"mensaje": "SeriesHub API funcionando"}


app.include_router(series_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)