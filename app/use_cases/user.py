from app import mappers
from app.repositories import db


def get_user_fio_by_id(user_id: int) -> str:
    user_db = db.get_user_by_id(user_id)
    if user_db is None:
        return ""

    user_entity = mappers.user.from_db_to_entity(user_db)

    return user_entity.full_name()
