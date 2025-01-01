from alembic import context

from core.config import settings
from db.base import Base

config = context.config

config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

target_metadata = Base.metadata