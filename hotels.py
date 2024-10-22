from itertools import count

from fastapi import Query, APIRouter
from schemas.hotels import Hotel, HotelPatch

router = APIRouter(prefix="/hotels", tags=["Отели"])

hotels = [
    {"id": 1, "title": "Sochi", "name": "Polyana"},
    {"id": 2, "title": "Дубай", "name": "Burj"},

    {"id": 3, "title": "Мальдивы", "name": "maldivi"},
    {"id": 4, "title": "Геленджик", "name": "gelendzhik"},

    {"id": 5, "title": "Москва", "name": "moscow"},
    {"id": 6, "title": "Казань", "name": "kazan"},

    {"id": 7, "title": "Санкт-Петербург", "name": "spb"},
]

@router.get("")
def get_hotels(
        id: int | None = Query(None, description="Айдишник"),
        title: str | None = Query(None, description="Название"),
        page: int | None = Query(None, description="Страница"),
        per_page: int | None = Query(None, description="Количество на странице"),
):
    count_per_paige = per_page
    count_paige = page
    id = id
    title = title

    if count_per_paige > 0:
        a = ((count_paige - 1) * count_per_paige)
        if count_paige > 0:
            return hotels[a:(a + count_per_paige)]
    else:
        return hotels[0:3] # стандарт при не заполненной per_page

    if id > 0: # надо переделать, чтобы работал общий список тоже
        hotels_ = []
        for hotel in hotels:
            if id and hotel["id"] != id:
                continue
            if title and hotel["title"] != title:
                continue
            hotels_.append(hotel)
        return hotels_

@router.delete("{hotel_id}")
def delete_hotel(hotel_id: int):
    global hotels
    hotels = [hotel for hotel in hotels if hotel["id"] != hotel_id]
    return {"status" : "OK"}

@router.post("")
def create_hotel(
        hotel_data: Hotel
):
    global hotels
    hotels.append({
        "id": hotels[-1]["id"] + 1,
        "title": hotel_data.title,
        "name": hotel_data.name
    })
    return {"status": "OK"}

@router.put("{hotel_id}", summary="Обновление")
def put_hotel(hotel_id: int, hotel_data: Hotel):
    global hotels
    for hotel in hotels:
        if hotel["id"] == hotel_id:
            hotel["title"] = hotel_data.title,
            hotel["name"] = hotel_data.name
            break
    return {"status": "OK"}

@router.patch("{hotel_id}", summary="Частичное обновление")
def patch_hotel(
        hotel_id: int,
        hotel_data: HotelPatch,
):
    global hotels
    for hotel in hotels:
        if hotel["id"] == hotel_id:
            if hotel_data.title:
                hotel["title"] = hotel_data.title
            if hotel_data.name:
                hotel["name"] = hotel_data.name
            break
    return {"status": "OK"}