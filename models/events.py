from pydantic import BaseModel , Field
from typing import List


class Event(BaseModel):
    id: int
    title: str = Field(...,examples=["FastAPI Book Launch",])
    image: str = Field(...,examples=["https://linktomyimage.com/image.png"])
    description: str = Field(...,examples=["We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",])
    tags: List[str] = Field(...,examples=["python", "fastapi", "book","launch"])
    location: str = Field(...,examples=["Google Meet"])