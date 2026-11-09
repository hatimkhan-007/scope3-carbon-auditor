from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

class TenantCreate(BaseModel):
    name: str = Field(min_length=2, max_length=150)
    slug: str = Field(
        min_length=2,
        max_length=100,
        pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$"
    )

    class TenantResponse(BaseModel):
        id: UUID
        name: str
        slug: str
        is_active: bool
        created_at: datetime

        model_config = ConfigDict(from_attributes=True)