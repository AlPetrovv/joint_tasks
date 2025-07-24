import datetime as dt

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column


class IDPKINTMixin:
    id: Mapped[int] = mapped_column(primary_key=True)


class CreatedAtMixin:
    created_at: Mapped[dt.datetime] = mapped_column(default=dt.datetime.now, server_default=func.now())
