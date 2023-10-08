from app import entities


def from_db_to_entity(user):
    return entities.User(
        id=user.id,
        first_name=user.first_name,
        middle_name=user.middle_name,
        last_name=user.last_name,
        description=user.description,
    )
