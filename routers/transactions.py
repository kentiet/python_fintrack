from fastapi import APIRouter

router = APIRouter(
    prefix="/transactions",
    tags=["transactions"]
)

@router.get("/")
async def gets():
    return {"this is transaction api"}