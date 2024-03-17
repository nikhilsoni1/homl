# coding: utf-8
from sqlalchemy import Boolean, Column, DateTime, String, Table, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class ApiResponse(Base):
    __tablename__ = "api_responses"

    email_id = Column(String, primary_key=True, nullable=False)
    object_id = Column(String, primary_key=True, nullable=False)
    response = Column(String)
    record_created_ts = Column(DateTime, nullable=False)
    processed = Column(Boolean, nullable=False, server_default=text("false"))
    processed_ts = Column(DateTime)


class EmailsMetadatum(Base):
    __tablename__ = "emails_metadata"

    object_id = Column(String, primary_key=True)
    email_id = Column(String, nullable=False)
    sender_email_ts = Column(DateTime, nullable=False)
    sender_email_id = Column(String)
    sender_email_domain = Column(String)


class User(Base):
    __tablename__ = "users"

    email_id = Column(String, primary_key=True)
    token = Column(String)
    token_update_ts = Column(DateTime)
    record_created_ts = Column(DateTime, nullable=False)
