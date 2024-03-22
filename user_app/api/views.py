from rest_framework.decorators import api_view
from .serializer import RegisterSerializer
from rest_framework.response import Response
@api_view(["POST"])
def registration_view(request):
    if request.method == "POST":
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


