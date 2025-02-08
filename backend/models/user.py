from datetime import datetime, date, timezone

from sqlalchemy import DATE, DateTime, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from database.config import Base


# Create User class
class UserModels(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    birthday: Mapped[date]
    create_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now(timezone.utc))
    last_login: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now(timezone.utc))

    tasks: Mapped[list["TaskModels"]] = relationship('TaskModels', back_populates='user', cascade='all, delete') # type: ignore
    categories: Mapped[list["CategoryModels"]] = relationship('CategoryModels', back_populates='user', cascade='all, delete') # type: ignore

    def __repr__(self) -> str:
        return f"<UserModels(id={self.id}, username={self.username}, password={self.password}, email={self.email}, birthday={self.birthday})>"
