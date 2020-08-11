from fastapi import APIRouter

router = APIRouter()

@router.get('',
summary='return a list of all payrolls'
)
async def get_payrolls():
    pass