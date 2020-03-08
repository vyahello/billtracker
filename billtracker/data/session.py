import os
import sqlalchemy
import sqlalchemy.orm
from sqlalchemy.orm import Session
from billtracker.data.model import SqlAlchemyBase
# noinspection PyUnresolvedReferences
from billtracker.data.__all_models import *


class DatabaseSession:
    factory = None
    engine = None
    folder = None

    @staticmethod
    def global_init(file: str) -> None:

        if DatabaseSession.factory:
            return

        if not file or not file.strip():
            raise Exception("You must specify a data file.")

        DatabaseSession.folder = os.path.dirname(file)
        connection: str = f"sqlite:///{file}"
        print("Connecting to DB at: {}".format(connection))

        engine = sqlalchemy.create_engine(connection, echo=False)
        DatabaseSession.engine = engine
        DatabaseSession.factory = sqlalchemy.orm.sessionmaker(bind=engine)
        SqlAlchemyBase.metadata.create_all(engine)

    @staticmethod
    def create_session() -> Session:
        return DatabaseSession.factory()
