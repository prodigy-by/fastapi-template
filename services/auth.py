import grpc
from fastapi import Request
from proto.auth_pb2 import UserRequest, CodeResponse
from proto.auth_pb2_grpc import AuthStub
from core import exceptions
from core.config import (
    AUTH_URL
)

def get_token(request: Request) -> str:
    '''Getting token from request header'''

    authorization = request.headers.get("Authorization")
    if not authorization:
        raise exceptions.CREDENTIALS_EXCEPTION

    token_list = authorization.split()
    if len(token_list) != 2:
        raise exceptions.CREDENTIALS_VALIDATION_EXCEPTION

    if token_list[0] != 'Bearer':
        raise exceptions.CREDENTIALS_VALIDATION_EXCEPTION

    return token_list[1]


def deauthenticate(request: Request) -> CodeResponse:
    '''Deauthenticating user'''

    token = get_token(request)
    try:
        channel = grpc.insecure_channel(AUTH_URL)
        client = AuthStub(channel)
        request = UserRequest(token=token)
        response = client.deauthenticate(request)
    except:
        raise exceptions.CREDENTIALS_VALIDATION_EXCEPTION

    return response
