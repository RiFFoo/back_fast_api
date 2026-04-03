from pydantic import BaseModel, ConfigDict


class RoomsAddRequest(BaseModel):
    title: str
    description: str | None = None
    price: int
    quantity: int

class RoomsAdd(BaseModel):
    hotel_id: int | None = None
    title: str | None = None
    description: str | None = None
    price: int | None = None
    quantity: int | None = None


class Rooms(RoomsAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)


class RoomsPatchRequest(BaseModel):
    title: str | None = None
    description: str | None = None
    price: int | None = None
    quantity: int | None = None


class RoomsPatch(BaseModel):
    hotel_id: int | None = None
    title: str | None = None
    description: str | None = None
    price: int | None = None
    quantity: int | None = None


