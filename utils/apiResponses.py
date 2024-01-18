from django.http import JsonResponse

# success : 200
CODE_SUCCESS = 200

CODE_Failed = 400
NOK = "NOK"
OK = "OK"


def APIResponse(status: str = "ok", code: int = 200, messages="success", data=None):
    if data is None:
        data = []

    return JsonResponse({
        "status": status,
        "code": code,
        "message": messages,
        "data": data
    }, status=code)
