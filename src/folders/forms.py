from pydantic import Field

from folders.schemas import Folder


class FolderSelectForm(Folder):
    folder: str = Field(
        json_schema_extra={"search_url": "/api/jt/folders/forms/search_folder"}
    )
