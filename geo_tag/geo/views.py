from django.shortcuts import render, redirect
import base64
from django.core.files.base import ContentFile
from .models import Complaint
import requests


def add_complaint(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        latitude = request.POST.get("latitude")
        longitude = request.POST.get("longitude")
        photo_data = request.POST.get("photo_data")

        # Reverse geocoding (FREE)
        address = None
        if latitude and longitude:
            url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={latitude}&lon={longitude}"
            response = requests.get(url, headers={"User-Agent": "geo_app"})
            data = response.json()

            if "display_name" in data:
                address = data["display_name"]

        # Convert base64 image
        format, imgstr = photo_data.split(';base64,')
        ext = format.split('/')[-1]
        photo = ContentFile(base64.b64decode(imgstr), name='captured.' + ext)

        complaint = Complaint.objects.create(
            title=title,
            description=description,
            latitude=latitude,
            longitude=longitude,
            address=address,
            photo=photo
        )

        return redirect("success", complaint.id)

    return render(request, "add_complaint.html")

def success(request, id):
    complaint = Complaint.objects.get(id=id)
    return render(request, "success.html", {"complaint": complaint})

def map_view(request):
    complaints = Complaint.objects.all()

    data = []
    for c in complaints:
        data.append({
            "title": c.title,
            "description": c.description,
            "latitude": c.latitude,
            "longitude": c.longitude,
            "photo": c.photo.url if c.photo else ""
        })
    return render(request, "map.html", {"complaints": data})