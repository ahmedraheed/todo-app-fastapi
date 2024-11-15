from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str | None = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    is_completed: bool

class TaskResponse(TaskBase):
    id: int
    is_completed: bool

    class Config:
        orm_mode = True
