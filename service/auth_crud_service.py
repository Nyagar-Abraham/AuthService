from sqlalchemy.orm import Session

import models
from schema import SignUpUserRequest
from helpers.bcrypt import get_password_hash


def signup(db: Session, user: SignUpUserRequest):
    user = db.query(models.User).filter(models.User.email ==user.email).first()
    if user is None:
        return None
    db_user = models.User(username=user.username, email=user.email, password=get_password_hash(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user