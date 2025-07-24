from typing import Literal, Optional

from pydantic import BaseModel


class RelationOptions(BaseModel):
    id_unique: Optional[bool] = None
    id_nullable: Optional[bool] = True
    many_to_one_relation: bool = True
    on_delete: Literal["CASCADE", "NO ACTION", "SET NULL", "RESTRICT", "DELETE"] = "CASCADE"
    back_populates: Optional[str] = None
    cascade: Literal["all, delete-orphan", "save-update, merge"] = "save-update, merge"
