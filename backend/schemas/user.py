def userEntity(user) -> dict:
    return {
        "_id": str(user["_id"]),
        "mail": user["mail"],
        "username": user["username"],
        "name": user["name"],
        "last_name": user["last_name"],
        "password": user["password"],
    }


def usersEntity(users) -> list[dict]:
    return [userEntity(user) for user in users]
