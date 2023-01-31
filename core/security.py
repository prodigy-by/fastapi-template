from fastapi import Depends
from services.auth import get_user_auth
from core import exceptions
from models.schemas import Permission, UserAuth


BINARY_RIGHTS = {
    'create': 1,
    'view': 2,
    'update': 4,
    'delete': 8
}


def crud_permissions(right, user_right):
    user_right = int(user_right)
    access = user_right & BINARY_RIGHTS[right]
    if access != BINARY_RIGHTS[right]:
        return False
    return True


def check_permission(resource_type, right, user, item_id):
    user_permissions = user.permissions
    if item_id == '*':
        multiple_rights = user_permissions.get(f'{resource_type}-*')
        if multiple_rights == None:
            raise exceptions.PERMISSIONS_DENIED_EXCEPTION

        if not crud_permissions(right, multiple_rights):
            raise exceptions.PERMISSIONS_DENIED_EXCEPTION
    else:
        single_rights = user_permissions.get(f'{resource_type}-{item_id}')
        if single_rights == None:
            multiple_rights = user_permissions.get(f'{resource_type}-*')
            if multiple_rights == None:
                raise exceptions.PERMISSIONS_DENIED_EXCEPTION

            if not crud_permissions(right, multiple_rights):
                raise exceptions.PERMISSIONS_DENIED_EXCEPTION
        else:
            if not crud_permissions(right, single_rights):
                raise exceptions.PERMISSIONS_DENIED_EXCEPTION


def permissions(resource_type: str, right: str):

    def _permissions(user: UserAuth = Depends(get_user_auth), item_id: str = '*') -> Permission:

        check_permission(resource_type, right, user, item_id)

        return Permission(user=user, item_id=item_id)

    return _permissions
