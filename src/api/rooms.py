
from fastapi import APIRouter, Query

from src.repositories.rooms import RoomsRepository
from schemas.rooms import RoomsAdd, RoomsPatch
from src.database import async_session_maker

router = APIRouter(prefix="/rooms", tags=["Номера"])


@router.get("")
async def get_rooms(
        hotel_id: int | None = Query(None),
        title: str | None = Query(None, description="Название"),
        description: str | None = Query(None, description="Дополнение"),
        price: int | None = Query(None, description="Цена"),
        quantity: int | None = Query(None, description="Количество"),
):
    async with async_session_maker() as session:
        return await RoomsRepository(session).get_all(
            hotel_id=hotel_id,
            title=title,
            description=description,
            price=price,
            quantity=quantity,
            )

@router.get("/{rooms_id}")
async def get_one_room(room_id: int):
    async with async_session_maker() as session:
        return await RoomsRepository(session).get_one_or_none(id=room_id)

@router.post("")
async def add_room(
        data: RoomsAdd,
):
    async with async_session_maker() as session:
        hotel_id = await RoomsRepository(session).add(data)
        await session.commit()
        return hotel_id

@router.put("{rooms_id}", summary="Обновление")
async def put_rooms(rooms_id: int, hotel_data: RoomsAdd):
    async with async_session_maker() as session:
        await RoomsRepository(session).edit(hotel_data, id=rooms_id)
        await session.commit()
    return {"status": "OK"}

@router.patch("{rooms_id}", summary="Частичное обновление")
async def patch_rooms(
        rooms_id: int,
        hotel_data: RoomsPatch,
):
    async with async_session_maker() as session:
        await RoomsRepository(session).edit(hotel_data, exclude_unset=True, id=rooms_id)
        await session.commit()
    return {"status": "OK"}

@router.delete("{rooms_id}")
async def delete_rooms(rooms_id: int):
    async with async_session_maker() as session:
        await RoomsRepository(session).delete(id = rooms_id)
        await session.commit()
    return {"status" : "OK"}