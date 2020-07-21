from rest_framework import serializers
from .models import calc_data

class calc_dataSerializers(serializers.ModelSerializer):


    class Meta():
        model=calc_data
        fields='__all__'