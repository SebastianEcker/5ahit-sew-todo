from datetime import datetime, timezone

from sqlalchemy import String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from database.config import Base


# Create User class
class CategoryModels(Base):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    color: Mapped[str] = mapped_column(String(7), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    create_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now(timezone.utc))

    user: Mapped["UserModels"] = relationship("UserModels", back_populates='categories') # type: ignore
    tasks: Mapped["TaskModels"] = relationship("TaskModels", back_populates='category', cascade='all, delete') # type: ignore

    def __repr__(self) -> str:
        return f"<CategoryModels(id={self.id}, name={self.name}, color={self.color}, tasks={self.tasks}), user={self.user}>"
