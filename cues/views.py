import jwt
import base64
import sys
from django.conf import settings
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import permissions
from .models import Cue
from .serializers import CueSerializer
from rest_framework.response import Response



class CueViewSet(ModelViewSet):

    queryset = Cue.objects.all()
    serializer_class = CueSerializer
    pagination_class = None

    # encoded_jwt = jwt.encode({"warrantyNumber": cue.warrantyNumber}, settings.SECRET_KEY, algorithm="HS256")
    # b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ3YXJyYW50eU51bWJlciI6IjIwLTAwMDYwIn0.bh6Sd_Hv8bvbWsrOM56ovfzu-ZEAak1EY74fA-SYVnM'

    @action(detail=False)
    def search(self, request):
        productName = request.GET.get("sn", None)        
        secretcode = request.GET.get("secretcode", None)
        decode_warrantyNumber = None
        if secretcode is not None:
            secretcode = secretcode[2:-1]
            encode_warrantyNumber = secretcode.encode('utf-8')
            decode_warrantyNumber = jwt.decode(encode_warrantyNumber, settings.SECRET_KEY, algorithms="HS256")
            decode_warrantyNumber = list(decode_warrantyNumber.values())[0]
        
        filter_kwargs = {}

        if productName is not None:
            filter_kwargs["warrantyNumber"] = productName
        try:
            cues = Cue.objects.filter(**filter_kwargs)
        except ValueError:
            cues = Cue.objects.all()

        if decode_warrantyNumber is not None:
            filter_kwargs["warrantyNumber"] = decode_warrantyNumber
        try:
            cues = Cue.objects.filter(**filter_kwargs)
        except ValueError:
            cues = Cue.objects.all()

        
        serializer = CueSerializer(cues, many=True).data
        return Response(serializer)



        # results = paginator.paginate_queryset(cues, request)
        # serializer = CueSerializer(results, many=True)
        # return paginator.get_paginated_response(serializer.data)


        # serializer = CueSerializer(cues, many=True)
        # return Response(data=serializer, status=status.HTTP_200_OK)
        
        # results = self.paginate_queryset(cues, request)
        # serializer = CueSerializer(results, many=True)
        # return Response(serializer.data)

        # room = serializer.save(user=request.user)
#       room_serializer = RoomSerializer(room).data
#       return Response(data=room_serializer, status=status.HTTP_200_OK)
