import os
import json
import re
import base64
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .ocr.ocr_service import process_image  # Import your OCR/ML processing function

# Initialize your ML model (make sure to provide the correct path to your model)
ml_model = MLModel(model_path=os.path.join(settings.BASE_DIR, 'path/to/your/model'))

# Home view
def home(request):
    return render(request, 'core/home.html')

# Query view
def query_view(request):
    if request.method == "POST":
        query = request.POST.get('query')
        return render(request, 'core/query.html', {'query': query})

# Image upload view (class-based)
class ImageUploadView(View):
    def post(self, request):
        # Disable CSRF protection for development (do NOT use in production)
        data = json.loads(request.body)
        image_data = data['image']
        
        # Decode the image data
        image_data = re.sub('^data:image/.+;base64,', '', image_data)
        image_data = base64.b64decode(image_data)

        # Save the image
        image_path = os.path.join(settings.MEDIA_ROOT, 'uploaded_images', 'uploaded_image.png')
        with open(image_path, 'wb') as f:
            f.write(image_data)

        # Process the uploaded image using the ML model
        result = process_image(image_path)  # Call your ML model here

        # Return the result as JSON response
        return JsonResponse({'result': result})

# Upload image view (function-based for traditional uploads)
def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        # Handle uploaded file
        uploaded_image = request.FILES['image']
        image_path = os.path.join(settings.MEDIA_ROOT, 'uploaded_images', uploaded_image.name)

        # Save the image
        with open(image_path, 'wb+') as destination:
            for chunk in uploaded_image.chunks():
                destination.write(chunk)

        # Process the uploaded image using the ML model
        result = process_image(image_path)  # Call your ML model here

        # Redirect to result page with the processed output
        return render(request, 'core/result.html', {'result': result})

    return render(request, 'core/upload.html')

# Result view (displays the output)
def result_view(request):
    # Display result logic could go here if needed, or it can be removed since results are displayed in the upload_image view
    return render(request, 'core/result.html')
