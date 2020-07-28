import jwt
import base64
from django.conf import settings
from rest_framework import serializers
from rest_framework.decorators import action
from datetime import datetime
from dateutil.relativedelta import relativedelta
from .models import Cue

class CueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cue
        exclude = ()

    def validate(self, data):
        isButt = data.get("isButt")
        isShaft = data.get("isShaft")
        if isButt is isShaft:
            raise serializers.ValidationError("하대인지 상대인지 체크해주세요")
        return data

    def create(self, validated_data):
        cue = super().create(validated_data)

        # 보증서 번호 생성
        # format : 두자리 현재년도 + 카운트(PK 최대 다섯자리로 가정)
        # ex) 20년도에 판매된 30번째 => 20-00030
        if(0 < cue.pk < 10):
            set_warrantyNumber = str(datetime.today().year%100) + "-00000" + str(cue.pk)
        elif(10 <= cue.pk < 100):
            set_warrantyNumber = str(datetime.today().year%100) + "-0000" + str(cue.pk)
        elif(100 <= cue.pk < 1000):
            set_warrantyNumber = str(datetime.today().year%100) + "-000" + str(cue.pk)
        elif(1000 <= cue.pk < 10000):
            set_warrantyNumber = str(datetime.today().year%100) + "-00" + str(cue.pk)
        elif(10000 <= cue.pk < 100000):
            set_warrantyNumber = str(datetime.today().year%100) + "-0" + str(cue.pk)
        else:
            set_warrantyNumber = str(datetime.today().year%100) + "-" + str(cue.pk)

        cue.warrantyNumber = set_warrantyNumber

        # 보증일 생성
        if cue.isButt:
            cue.warrantyDate = cue.purchasedDate + relativedelta(months=12)
            
        if cue.isShaft:
            cue.warrantyDate = cue.purchasedDate + relativedelta(months=6)
            
        cue.save()
        return cue
    
