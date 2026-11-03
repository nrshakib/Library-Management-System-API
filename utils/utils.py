from rest_framework.response import Response

def api_response(message, data, status_code):
    return Response({
        "message": message,
        "status_text": "success",
        "data": data
    }, status=status_code)