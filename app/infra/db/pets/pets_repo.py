from typing import List

# 開発モジュール
from app.infra.db.base_repo import BaseRepo
from app.models.pets import PetSummary


class PetsRepo():
    def __init__(self):
        self.base_repo = BaseRepo()

    def get_pets(self) -> List[PetSummary]:
        sql = """
            SELECT pet_id, name, type FROM pets;
        """
        try:
            self.base_repo.execute(sql=sql)
            rows = self.base_repo.fetchall()
            pet_summaries = []
            for row in rows:
                pet_summaries.append(
                    PetSummary(pet_id=row['pet_id'],
                               name=row['name'],
                               type=row['type']))
            return pet_summaries
        except Exception as e:
            self.base_repo.exception_handler(e)
            raise e
        finally:
            self.base_repo.clean_up()
