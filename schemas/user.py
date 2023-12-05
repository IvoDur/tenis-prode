def userEntity(user) -> dict:
    return {"_id": str(user["_id"]), "name": user["name"], "password": user["password"]}


def usersEntity(users) -> list[dict]:
    return [userEntity(user) for user in users]
