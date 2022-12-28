from src.database.models import Record as Model
from src.database.dbmanager import DbManager
import settings

dbmanager = DbManager(db_path=settings.DATABASE_PATH)


def get(id_: int) -> Model | None:
    res = dbmanager.execute_query(
        query=f'select * from {Model.__name__} where id=(?)',
        args=(id_,))

    return None if not res else Model(
        id=res[0],
        time_start=res[1],
        user_id=res[2],
        staff_id=res[3],
        service_id=res[4]
    )


def get_all() -> list[Model] | dict:
    l = dbmanager.execute_query(
        query=f"select * from {Model.__name__}",
        fetchone=False)

    res = []

    if l:
        for res in l:
            res.append(Model(
                id=res[0],
                time_start=res[1],
                user_id=res[2],
                staff_id=res[3],
                service_id=res[4]
            ))

    return res


def delete(id_: int) -> None:
    return dbmanager.execute_query(
        query=f'delete from {Model.__name__} where id=(?)',
        args=(id_,))


def create(new: Model) -> int | dict:
    res = dbmanager.execute_query(
        query=f"insert into {Model.__name__} (time_start, userID, staffID, serviceID) values(?,?,?,?) returning id",
        args=(new.time_start, new.user_id, new.staff_id, new.service_id))

    if type(res) != dict:
        res = get(res[0])

    return res


def update(id_: int, new: Model) -> None:
    return dbmanager.execute_query(
        query=f"update {Model.__name__} set (time_start, userID, staffID, serviceID) = (?,?,?,?) where id=(?)",
        args=(new.time_start, new.user_id, new.staff_id, new.service_id, id_))
