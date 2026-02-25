import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'parksathi.settings')
django.setup()

from parking.models import Parking

with open('kathmanduparking.geojson', encoding='utf-8') as f:
    data = json.load(f)


def get_lat_lon(geometry):
    coords = geometry['coordinates']

    # Case 1: Point
    if geometry['type'] == 'Point':
        return coords[1], coords[0]

    # Case 2: Polygon
    if geometry['type'] == 'Polygon':
        lon = coords[0][0][0]
        lat = coords[0][0][1]
        return lat, lon

    # Case 3: MultiPolygon
    if geometry['type'] == 'MultiPolygon':
        lon = coords[0][0][0][0]
        lat = coords[0][0][0][1]
        return lat, lon

    return None, None


for feature in data['features']:
    properties = feature['properties']
    geometry = feature['geometry']

    lat, lon = get_lat_lon(geometry)

    if lat is None:
        continue

    name = properties.get('name', 'Unknown Parking')

    Parking.objects.create(
        name=name,
        latitude=lat,
        longitude=lon,
        total_slots=50,
        available_slots=20,
        price_per_hour=20
    )

print("Parking data imported successfully!")