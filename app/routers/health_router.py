@router.get('/', response_model=String, status_code=200, summary='ペット一覧取得')
async def get_pets():
    """api状態確認用.

    """

    return 'OK'