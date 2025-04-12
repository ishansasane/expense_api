from fastapi import APIRouter

router = APIRouter(
    prefix="/expense",
    tags=["expense"],
)

@router.get("/")
def get_expenses():
    return {"message": "Get all expenses"}