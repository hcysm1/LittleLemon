
from rest_framework import serializers


from .models import MenuItem,Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta():
        model = Booking
        fields = ['id', 'name','no_of_guests','booking_date']


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta():
        model = MenuItem
        fields = ['id', 'title','price','inventory']