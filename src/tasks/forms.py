from pydantic import Field

from tasks.schemas import Task


class TaskCreateForm(Task):
    folder: str = Field(
        json_schema_extra={"search_url": "/api/jt/folders/forms/search_folder"}
    )
