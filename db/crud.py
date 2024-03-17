from sqlalchemy.orm import Session
from sqlalchemy import and_
# import models
from sqlalchemy.exc import IntegrityError
from typing import List


def write_record(db, model, data, message=None):
    record = model(**data)
    flag = True
    try:
        db.add(record)
        db.commit()
        db.refresh(record)
    except IntegrityError:
        if message:
            print(message)
        db.rollback()
        flag = False
    return flag


# def get_user_record_by_email(db, email_id):
#     q = db.query(models.User).filter(models.User.email_id == email_id)
#     r = q.all()
#     r_len = len(r)
#     if r_len == 1:
#         return r[0]
#     elif r_len > 1:
#         return f"Multiple records found for {email_id}!"
#     elif r_len == 0:
#         return None


# def update_user_record_token_by_email(db, record, token, token_update_ts):
#     record.token = token
#     record.token_update_ts = token_update_ts
#     db.commit()
#     db.refresh(record)
#     return True


# def mark_api_response(db, record, processed_ts, processed=False):
#     record.processed = processed
#     record.processed_ts = processed_ts
#     db.commit()
#     db.refresh(record)
#     return True


# def fltr_new_msg(msg, db: Session):
#     ids = [x.get("id") for x in msg]
#     q = db.query(models.ApiResponse.object_id).filter(
#         models.ApiResponse.object_id.in_(ids)
#     )
#     r = q.all()
#     r_p = [x[0] for x in r]
#     msg_fltr = list(filter(lambda x: x.get("id") not in r_p, msg))
#     return msg_fltr


# def get_responses(db, processed=False):
#     q = db.query(models.ApiResponse).filter(models.ApiResponse.processed == processed)
#     r = q.all()
#     return r
