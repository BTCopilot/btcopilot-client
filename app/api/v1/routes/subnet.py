from fastapi import APIRouter

router = APIRouter()


@router.post("/generate")
def generate():
    return {"message": "Welcome to the BTCopilot Subnet Interface"}
