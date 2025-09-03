from fastapi import HTTPException
from sqlmodel import Session, select
from models import UserLogin, UserCreate, User
from helpers.bcrypt import get_password_hash, verify_password

# class AuthCRUDService:
#     def __init__(self, session: Session):
#         self.session = session
#
#     def signup(self, user_payload: UserCreate) -> User:
#         statement = select(User).where(User.email == user_payload.email)
#         user_exist = self.session.exec(statement).first()
#         if user_exist is not None:
#             raise HTTPException(status_code=400, detail="Email already registered")
#
#         db_user = User.model_validate(user_payload)
#         db_user.password = get_password_hash(db_user.password)
#         self.session.add(db_user)
#         self.session.commit()
#         self.session.refresh(db_user)
#         return db_user


def signup(session: Session, user_payload: UserCreate):
    statement = select(User).where(User.email == user_payload.email)
    user_exist = session.exec(statement).first()
    if user_exist is not None:
        raise HTTPException(status_code=400, detail="Email already registered")



    db_user = User.model_validate(user_payload)
    db_user.password = get_password_hash(db_user.password)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

def authenticate_user(session: Session, user_payload: UserLogin) :
    email = user_payload.email
    password = user_payload.password

    statement = select(User).where(User.email == email)
    db_user = session.exec(statement).first()
    print("USER : ", db_user)
    if db_user is None:
        return None
    is_verified =verify_password(password, db_user.password)
    if not is_verified:

        return None
    return db_user




