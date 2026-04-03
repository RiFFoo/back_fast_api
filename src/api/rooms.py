
from fastapi import APIRouter, Body, Query

from src.repositories.rooms import RoomsRepository
from schemas.rooms import RoomsAdd, RoomsPatch, RoomsAddRequest, RoomsPatchRequest
from src.database import async_session_maker

router = APIRouter(prefix="/hotels", tags=["Номера"])


@router.get("/{hotel_id}/rooms")
async def get_rooms(hotel_id: int):
    async with async_session_maker() as session:
        return await RoomsRepository(session).get_filtered(hotel_id=hotel_id)

@router.get("/{hotel_id}/rooms/{rooms_id}")
async def get_one_room(hotel_id: int, room_id: int):
    async with async_session_maker() as session:
        return await RoomsRepository(session).get_one_or_none(id=room_id, hotel_id=hotel_id)

@router.post("/{hotel_id}/rooms")
async def add_room(hotel_id: int, data: RoomsAddRequest = Body()):
    _room_data = RoomsAdd(hotel_id=hotel_id, **data.model_dump())
    async with async_session_maker() as session:
        room = await RoomsRepository(session).add(_room_data)
        await session.commit()
        return {"status": "OK", "data": room}

@router.put("/{hotel_id}/rooms/{rooms_id}", summary="Обновление")
async def put_rooms(hotel_id: int, rooms_id: int, room_data: RoomsAddRequest):
    _room_data = RoomsAdd(hotel_id=hotel_id, **room_data.model_dump())
    async with async_session_maker() as session:
        await RoomsRepository(session).edit(_room_data, id=rooms_id)
        await session.commit()
    return {"status": "OK"}

@router.patch("/{hotel_id}/rooms/{rooms_id}", summary="Частичное обновление")
async def patch_rooms(
        hotel_id: int,
        rooms_id: int,
        room_data: RoomsPatchRequest,
):
    _room_data = RoomsPatch(hotel_id=hotel_id, **room_data.model_dump(exclude_unset=True))
    async with async_session_maker() as session:
        await RoomsRepository(session).edit(_room_data, exclude_unset=True, id=rooms_id, hotel_id=hotel_id)
        await session.commit()
    return {"status": "OK"}

@router.delete("/{hotel_id}/rooms/{rooms_id}")
async def delete_rooms(hotel_id: int, rooms_id: int):
    async with async_session_maker() as session:
        await RoomsRepository(session).delete(id = rooms_id, hotel_id = hotel_id)
        await session.commit()
    return {"status" : "OK"}