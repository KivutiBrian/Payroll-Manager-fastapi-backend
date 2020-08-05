from fastapi import APIRouter

router = APIRouter()

@router.get('')
async def get_employees(parameter_list):
    pass
