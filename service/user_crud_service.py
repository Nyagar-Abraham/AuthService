from sqlmodel import Session, select

# from schema import UpdateProfileRequest
from models import User


def get_users(session: Session):
    statement = select(User)
    users = session.exec(statement).all()
    if len(users) == 0:
       return []
    return users

# def update_user(db: Session,user_id: int ,user_payload: UpdateProfileRequest):
#     db_user = db.query(User).filter(User.email == user_payload.email).first()
#     if db_user is None:
#         return None
#     db.query(User).filter(User.id == user_id).update(
#         {
#             "email": user_payload.email,
#
#         }
#     )