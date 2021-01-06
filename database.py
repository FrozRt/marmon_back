import typing

from databases import Database
from sqlalchemy import create_engine, MetaData
from sqlalchemy.sql import ClauseElement

from settings import DATABASE_URL, DEFAULT_SCHEMA


class DatabaseNorm(Database):
    @classmethod
    def log_query(cls, message):
        print(message)

    async def execute(self, query: typing.Union[ClauseElement, str], values: dict = None) -> typing.Any:
        self.log_query(query)
        async with self.connection() as connection:
            return await connection.execute(query, values)

    async def fetch_all(self, query: typing.Union[ClauseElement, str], values: dict = None) -> \
            typing.List[typing.Mapping]:
        self.log_query(query)
        return await super(DatabaseNorm, self).fetch_all(query=query, values=values)

    async def fetch_one(self, query: typing.Union[ClauseElement, str], values: dict = None) -> \
            typing.Optional[typing.Mapping]:
        self.log_query(query)
        return await super(DatabaseNorm, self).fetch_one(query=query, values=values)


database = DatabaseNorm(DATABASE_URL)
engine = create_engine(DATABASE_URL)
metadata = MetaData()
metadata.schema = DEFAULT_SCHEMA
metadata.create_all(engine)
