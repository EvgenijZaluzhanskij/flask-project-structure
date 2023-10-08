from app import app
from app import use_cases


@app.route('/api/v1/user/<int:user_id>', methods=['GET'])
def get_user_fio_by_id(user_id: int):
    # Serialize

    fio = use_cases.get_user_fio_by_id(user_id)

    # Deserialize
    return fio, 200
