from fastapi import FastAPI

from routers.series import router as series_router


app = FastAPI()


@app.get("/")
def inicio():
    return {"mensaje": "SeriesHub API funcionando"}


app.include_router(series_router)
