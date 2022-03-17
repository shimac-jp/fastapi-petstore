"""petsタグに関するスキーマ."""
from pydantic import BaseModel


class PetSummary(BaseModel):
    """ペット一覧用の情報.

    Args:
        BaseModel ([type]): [description]
    """
    pet_id: str
    name: str
    type: str
