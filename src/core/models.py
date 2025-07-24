from sqlalchemy.orm import (DeclarativeBase, Mapped, declared_attr,
                            mapped_column)


class Base(DeclarativeBase):

    @declared_attr.directive
    def __tablename__(self):
        return self.__name__.lower()

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'{self.__class__.__name__}'
