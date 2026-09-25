AUTHORIZED_SERVER_ID = "1020369849622470686"


def authorized(server_id: str) -> bool:
    return str(server_id) == AUTHORIZED_SERVER_ID


def check_server(server_id: str) -> None:
    if not authorized(server_id):
        raise PermissionError("Unauthorized server")
