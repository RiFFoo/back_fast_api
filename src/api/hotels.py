from fastapi import Query, APIRouter, Body

from src.database import async_session_maker
from src.repositories.hotels import HotelsRepository
from src.schemas.hotels import HotelPatch, HotelAdd

from src.api.dependencies import PaginationDep

router = APIRouter(prefix="/hotels", tags=["Отели"])


@router.get("")
async def get_hotels(
        pagination: PaginationDep,
        title: str | None = Query(None, description="Название"),
        location: str | None = Query(None, description="Местонахождение"),
):
    per_page = pagination.per_page or 5
    async with async_session_maker() as session:
        return await HotelsRepository(session).get_all(
            location=location,
            title=title,
            limit=per_page,
            offset=per_page * (pagination.page - 1),
        )

@router.get("/{hotel_id}")
async def get_one_hotel(hotel_id: int):
    async with async_session_maker() as session:
        return await HotelsRepository(session).get_one_or_none(id=hotel_id)

@router.delete("{hotel_id}")
async def delete_hotel(hotel_id: int):
    async with async_session_maker() as session:
        await HotelsRepository(session).delete(id = hotel_id)
        await session.commit()
    return {"status" : "OK"}

@router.post("")
async def create_hotel(hotel_data: HotelAdd = Body(openapi_examples={
    "1": {
        "summary": "Сочи",
        "value": {
            "title": "Отель Сочи 5 звезд у моря",
            "location": "г. Сочи, ул. моря 1",
        }
    },
    "2": {
        "summary": "Дубай",
        "value": {
            "title": "Hotel Dubai resort",
            "location": "Sheikh street 2",
        }
    }
    })
):

    async with async_session_maker() as session:
        hotel_id = await HotelsRepository(session).add(hotel_data)
        await session.commit()

        return {"status": "OK", "data": hotel_id}

@router.put("{hotel_id}", summary="Обновление")
async def put_hotel(hotel_id: int, hotel_data: HotelAdd):
    async with async_session_maker() as session:
        await HotelsRepository(session).edit(hotel_data, id=hotel_id)
        await session.commit()
    return {"status": "OK"}

@router.patch("{hotel_id}", summary="Частичное обновление")
async def patch_hotel(
        hotel_id: int,
        hotel_data: HotelPatch,
):
    async with async_session_maker() as session:
        await HotelsRepository(session).edit(hotel_data, exclude_unset=True, id=hotel_id)
        await session.commit()
    return {"status": "OK"}