"""
Database connection and session management.
Simple and straightforward - creates engine, provides sessions.
"""
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import declarative_base

from backend.config.settings import settings

# base class for all database models
Base = declarative_base()

# create teh db engine (connects to db)
engine = create_async_engine(
    settings.DATABASE_URL,  # Gets URL from settings (which reads .env)
    echo=settings.DEBUG,    # Show SQL queries if DEBUG=True
)


# creates the session
async_session_maker = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


# gets the database session
async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Provides a database session to FastAPI routes.
    Automatically commits on success, rolls back on error, and closes.
    
    Usage in routes:
        @router.get("/users")
        async def get_users(db: AsyncSession = Depends(get_db_session)):
            result = await db.execute(select(User))
            return result.scalars().all()
    """
    async with async_session_maker() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


# initializes the database (start up function)
async def init_db() -> None:
    """
    Create all database tables.
    Only use in development
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# shut down the db
async def close_db() -> None:
    """Close all database connections when app shuts down."""
    await engine.dispose()