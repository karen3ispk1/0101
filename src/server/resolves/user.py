from src.database.models import User as Model
from src.server.resolves.record import dbmanager


def get(id_: int) -> Model | None:
    res = dbmanager.execute_query(
        query=f'select * from {Model.__name__} where id=(?)',
        args=(id_,))

    return None if not res else Model(
        id=res[0],
        name=res[1],
        password=res[2]
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
                name=res[1],
                password=res[2]
            ))

    return res


def delete(id_: int) -> None:
    return dbmanager.execute_query(
        query=f'delete from {Model.__name__} where id=(?)',
        args=(id_,))


def create(new: Model) -> int | dict:
    res = dbmanager.execute_query(
        query=f"insert into {Model.__name__} (name, password) values(?,?) returning id",
        args=(new.name, new.password))

    if type(res) != dict:
        res = get(res[0])

    return res


def update(id_: int, new: Model) -> None:
    return dbmanager.execute_query(
        query=f"update {Model.__name__} set (name, password) = (?,?) where id=(?)",
        args=(new.name, new.password, id_))


def login(user_name: str, user_password: str) -> Model | None:
    res = dbmanager.execute_query(
        query='select id from User where name=(?) and password=(?) ',
        args=(user_name, user_password)
    )

    return get(res[0]) if res else None

