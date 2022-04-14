from typing import List, Optional
from fastapi import APIRouter, Query

# 開発モジュール
from app.models.pets import PetSummary
from app.infra.db.pets.pets_repo import PetsRepo

router = APIRouter()


@router.get('/pets', response_model=List[PetSummary], status_code=200, summary='ペット一覧取得')
async def get_pets(
        name: Optional[str] = Query(default=None, description='ペット名', example='pochi'),
        type: Optional[str] = Query(default=None, description='ペット種類', example='cat')):
    """ペット一覧取得.

    名前やタイプで絞り込みできます.

    \f
    Args:
        name (Optional[str], optional): [description]. Defaults to None.
        type (Optional[str], optional): [description]. Defaults to None.
    """
    pet_summaries = PetsRepo().get_pets()
    return pet_summaries
