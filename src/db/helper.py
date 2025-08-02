from asyncio import current_task

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_scoped_session,
    async_sessionmaker,
    create_async_engine,
)

from config import settings


class DBHalper:
    def __init__(self, db_url: str, echo: bool = False):
        self.engine = create_async_engine(
            url=db_url,
            echo=echo,
        )

        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    def get_connection(self):
        with self.engine.begin() as conn:
            return conn

    def get_scoped_session(self):
        """
        Return a scoped session.

        The session is tied to the current task. Each task will have its own session.
        The session is created using `session_factory` and `scopefunc`.

        The session is scoped to the current task. This means that the session will be
        closed when the task is finished.

        :return: A scoped session.
        """
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )
        return session

    async def session_dependency(self) -> AsyncSession:
        """
        Session dependency for FastAPI.

        This method is a dependency for FastAPI.
        It creates a scoped session and yields it.
        After the session is used, it is removed.
        """

        async with self.session_factory() as session:
            yield session
        # session = self.get_scoped_session()
        # yield session
        # await session.close()

    async def dispose(self):
        await self.engine.dispose()

db_helper = DBHalper(
    db_url=settings.db.url,
    echo=settings.db.echo,
)
