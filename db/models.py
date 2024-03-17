# coding: utf-8
from sqlalchemy import Column, Float, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class CaHousingDatum(Base):
    __tablename__ = "ca_housing_data"

    row_id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('ca_housing_data_row_id_seq'::regclass)"),
    )
    longitude = Column(Float(53))
    latitude = Column(Float(53))
    housing_median_age = Column(Float(53))
    total_rooms = Column(Float(53))
    total_bedrooms = Column(Float(53))
    population = Column(Float(53))
    households = Column(Float(53))
    median_income = Column(Float(53))
    median_house_value = Column(Float(53))
    ocean_proximity = Column(String)
