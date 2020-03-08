"""Module contains a set of methods to operate sessions."""
import os
from typing import Callable
import sqlalchemy
import sqlalchemy.orm
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session
from billtracker.data.model import SqlAlchemyBase

# noinspection PyUnresolvedReferences
from billtracker.data.__all_models import *


class DatabaseSession:
    """Represents database session."""

    factory: Callable[[], Session] = None  # type: ignore
    engine: Engine = None
    folder: str = None  # type: ignore

    @staticmethod
    def initialize(file: str) -> None:
        """Initializes database.

        Args:
            file: database file path
        """
        if DatabaseSession.factory:
            return
        if not file or not file.strip():
            raise Exception("You must specify a data file.")
        DatabaseSession.folder = os.path.dirname(file)
        connection: str = f"sqlite:///{file}"
        print(f"Connecting to DB at: {connection}")
        engine: Engine = sqlalchemy.create_engine(connection, echo=False)
        DatabaseSession.engine = engine
        DatabaseSession.factory = sqlalchemy.orm.sessionmaker(bind=engine)
        SqlAlchemyBase.metadata.create_all(engine)

    @staticmethod
    def create_session() -> Session:
        """Creates current database session."""
        return DatabaseSession.factory()
