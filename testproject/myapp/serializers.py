from rest_framework import serializers
from .models import Destination, Trip, Booking

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'

class TripSerializer(serializers.ModelSerializer):
    destination = DestinationSerializer(read_only=True)
    destination_id = serializers.PrimaryKeyRelatedField(
        queryset=Destination.objects.all(),
        source='destination',
        write_only=True
    )
    class Meta:
        model = Trip
        fields = ['id', 'start_date', 'end_date', 'price', 'available_seats', 'destination', 'destination_id']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def validate(self, data):
        if data['end_date'] <= data['start_date']:
            raise serializers.ValidationError("End date must be after the start date")
        
        return data

