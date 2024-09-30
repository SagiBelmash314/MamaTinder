from fastapi import APIRouter, FastAPI

app = FastAPI()

router = APIRouter()


@router.get("/")
def root():
    """Basic EntryPoint"""
    return "FastAPI"


app.include_router(router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="localhost", port=8080, reload=True)
