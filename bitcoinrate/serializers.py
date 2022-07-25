from rest_framework import serializers 
from bitcoinrate.models import Bitcoinrate

class BitcoinrateSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Bitcoinrate
        fields = ('id',
                  'rate')