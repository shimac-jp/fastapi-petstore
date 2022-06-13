from fastapi import APIRouter, Query

router = APIRouter()
@router.get('/', status_code=200, summary='ヘルスチェック')
async def get_health():
    """ヘルスチェック.

    """

    return 'OK'