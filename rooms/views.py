from rest_framework.generics import RetrieveAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Room
from .serializers import ReadRoomSerializer, WriteRoomSerializer


@api_view(["GET", "POST"])
def rooms_view(request):
    if request.method == "GET":
        rooms = Room.objects.all()
        serializer = ReadRoomSerializer(rooms, many=True).data
        return Response(serializer)
    elif request.method == "POST":
        serializer = WriteRoomSerializer(data=request.data)
        if serializer.is_valid():
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class SeeRoomView(RetrieveAPIView):

    queryset = Room.objects.all()
    serializer_class = ReadRoomSerializer


# class ListRoomsView(ListAPIView):
#     queryset = Room.objects.all()
#     serializer_class = RoomSerializer

# class based view wit APIview
# from rest_framework.views import APIView
# from rest_framework.response import Response
# class ListRoomsView(ListAPIView):
#     def get(self, request):
#         rooms = Room.objects.all()
#         serializer = RoomSerializer(rooms, many=True)
#         return Response(serializer.data)
#     def post(self, request):
#         pass

# function based view
# from rest_framework.decorators import api_view
# @api_view(["GET"])
# def list_rooms(request):
#     rooms = Room.objects.all()
#     serialized_rooms = RoomSerializer(rooms, many=True)
#     return Response(data=serialized_rooms.data)

