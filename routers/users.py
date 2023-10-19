from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/")
def gets():
    return {"this is user router"}
    # cmd = f"SELECT * FROM app_user"
    # cursor.execute(cmd)
    # conn.commit()
    # return cursor.fetchone()