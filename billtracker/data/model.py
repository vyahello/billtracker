"""Module contains a list of all database model."""
import sqlalchemy.ext.declarative as declarative
from sqlalchemy.ext.declarative import DeclarativeMeta

SqlAlchemyBase: DeclarativeMeta = declarative.declarative_base()
