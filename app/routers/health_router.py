from fastapi import APIRouter, Query

router = APIRouter()
@router.get('/', status_code=200, summary='ペット一覧取得')
async def get_health():
    """api状態確認用.

    """

    return 'OK'