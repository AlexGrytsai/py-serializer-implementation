from car.models import Car
from car.serializers import CarSerializer
import json


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(instance=car)
    serializer_data = serializer.data

    return json.dumps(serializer_data, separators=(",", ":")).encode("utf-8")


def deserialize_car_object(json_bytes: bytes) -> Car:
    json_str = json_bytes.decode("utf-8")
    json_data = json.loads(json_str)
    serializer = CarSerializer(data=json_data)
    serializer.is_valid(raise_exception=True)

    return serializer.save()
