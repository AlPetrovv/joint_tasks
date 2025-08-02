from typing import TYPE_CHECKING, Any, Union
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship

from core.schemas import RelationOptions
from db.utils import camel_case_to_snake_case

if TYPE_CHECKING:
    from db.all_models import AuthUser, Folder, Task, User


class RelationMixin:
    @classmethod
    def __get_options(cls, model: Any) -> dict[str, Union[str, bool, None]]:
        options_data = getattr(cls, f"_{camel_case_to_snake_case(model)}_options".lower())
        rel_options = RelationOptions(**options_data).model_dump()
        return rel_options

    @classmethod
    def __get_foreign_key(cls, model: Any) -> str:
        return getattr(cls, f"_{camel_case_to_snake_case(model)}_foreign_key".lower())

    @classmethod
    def _model_relation(
        cls, model: Any
    ) -> Mapped[Union["Task", "User", "Folder", "AuthUser"]]:
        rel_options = cls.__get_options(model)
        return relationship(
            model,
            back_populates=rel_options["back_populates"],
            uselist=rel_options["uselist"],
            cascade=rel_options["cascade"],
            remote_side=rel_options["remote_side"],
            single_parent=rel_options["single_parent"],
        )

    @classmethod
    def _model_relation_id(cls, model: Any) -> Mapped[int]:
        rel_options = cls.__get_options(model)
        return mapped_column(
            ForeignKey(
                cls.__get_foreign_key(model=model), ondelete=rel_options["on_delete"]
            ),
            unique=rel_options["id_unique"],
            nullable=rel_options["id_nullable"],
        )


class UserRelationMixin(RelationMixin):
    __user_model: str = "User"
    _user_foreign_key: str = "users.id"
    _user_options: dict = {}

    @declared_attr
    def user_id(cls) -> Mapped[int]:
        return cls._model_relation_id(model=cls.__user_model)

    @declared_attr
    def user(cls) -> Mapped["User"]:
        return cls._model_relation(model=cls.__user_model)


class FolderRelationMixin(RelationMixin):
    __folder_model: str = "Folder"
    _folder_foreign_key: str = "folders.id"
    _folder_options: dict = {}

    @declared_attr
    def folder_id(cls) -> Mapped[int]:
        return cls._model_relation_id(model=cls.__folder_model)

    @declared_attr
    def folder(cls) -> Mapped["Folder"]:
        return cls._model_relation(model=cls.__folder_model)


class TaskRelationMixin(RelationMixin):
    __task_model: str = "Task"
    _task_foreign_key: str = "tasks.id"
    _task_options: dict = {}

    @declared_attr
    def task_id(cls) -> Mapped[int]:
        return cls._model_relation_id(model=cls.__task_model)

    @declared_attr
    def task(cls) -> Mapped["Task"]:
        return cls._model_relation(model=cls.__task_model)


class AuthUserRelationMixin(RelationMixin):
    __auth_user_model: str = "AuthUser"
    _auth_user_foreign_key: str = "auth_users.id"
    _auth_user_options: dict = {}

    @declared_attr
    def auth_user_id(cls) -> Mapped[int]:
        return cls._model_relation_id(model=cls.__auth_user_model)

    @declared_attr
    def auth_user(cls) -> Mapped["AuthUser"]:
        return cls._model_relation(model=cls.__auth_user_model)
