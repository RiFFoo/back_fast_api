from fastapi import Query, Body, APIRouter

router = APIRouter(prefix="/hotels", tags=["Отели"])

hotels = [
    {"id": 1, "title": "Sochi", "name": "Polyana"},
    {"id": 2, "title": "Дубай", "name": "Burj"},
]

@router.get("")
def get_hotels(
        id: int | None = Query(None, description="Айдишник"),
        title: str | None = Query(None, description="Название"),
):
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
        title: str = Body(embed=True)
):
    global hotels
    hotels.append({
        "id": hotels[-1]["id"] + 1,
        "title": title
    })
    return {"status": "OK"}

@router.put("{hotel_id}", summary="Обновление")
def put_hotel(hotel_id: int, title: str = Body(), name: str = Body()):
    global hotels
    for hotel in hotels:
        if hotel["id"] == hotel_id:
            hotel["title"] = title
            hotel["name"] = name
            break
    return {"status": "OK"}

@router.patch("{hotel_id}", summary="Частичное обновление")
def patch_hotel(hotel_id: int, title: str | None = Body(), name: str | None = Body()):
    global hotels
    for hotel in hotels:
        if hotel["id"] == hotel_id:
            if title:
                hotel["title"] = title
            if name:
                hotel["name"] = name
            break
    return {"status": "OK"}