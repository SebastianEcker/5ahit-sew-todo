from datetime import datetime, timezone

from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from database.config import Base

# Create User class
class TaskModels(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str]
    end_date: Mapped[datetime]
    completed: Mapped[bool] = mapped_column(default=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id", ondelete="CASCADE"), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    create_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now(timezone.utc))

    user: Mapped['UserModels'] = relationship(back_populates='tasks') # type: ignore
    category: Mapped['CategoryModels'] = relationship(back_populates='tasks') # type: ignore
    
    def __repr__(self) -> str:
        return (f"<TaskModels(id={self.id}, title={self.title}, description={self.description}, end_date={self.end_date}, "
                f"completed={self.completed}, category_id={self.category_id}, user_id={self.user_id}, create_time={self.create_time} "
                f"user={self.user!r}, category={self.category!r})>")
