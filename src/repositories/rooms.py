from src.models.rooms import RoomsOrm
from src.repositories.base import BaseRepository
from src.schemas.rooms import Rooms

from sqlalchemy import select, func


class RoomsRepository(BaseRepository):
    model = RoomsOrm
    schema = Rooms

    async def get_all(
            self,
            hotel_id,
            title,
            description,
            price,
            quantity,
    ) -> list[Rooms]:
        query = select(RoomsOrm)
        if hotel_id:
            query = query.filter(RoomsOrm.hotel_id==hotel_id)
        if title:
            query = query.filter(func.lower(RoomsOrm.title).contains(title.strip().lower()))
        if description:
            query = query.filter(func.lower(RoomsOrm.description).contains(description.strip().lower()))
        if price:
            query = query.filter(RoomsOrm.price==price)
        if quantity:
            query = query.filter(RoomsOrm.quantity==quantity)

        print(query.compile(compile_kwargs={"literal_binds": True}))
        result = await self.session.execute(query)

        return [Rooms.model_validate(rooms, from_attributes=True) for rooms in result.scalars().all()]