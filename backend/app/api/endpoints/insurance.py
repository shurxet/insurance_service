from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def calculate_insurance():
    return "Test endpoint calculate_insurance"
