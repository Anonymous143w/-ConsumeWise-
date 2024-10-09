from django.urls import path
from core.views import home, query_view, ImageUploadView, result_view   # Import the class-based view
from .views import ProcessImageView

urlpatterns = [
    path('', home, name='home'),
    path('query/', query_view, name='query_view'),
    path('upload-image/', ImageUploadView.as_view(), name='upload_image'),  # Use .as_view() for class-based view
    path('result/', result_view, name='result'),  path('process-image', ProcessImageView.as_view(), name='process_image'),      # Show the result of the prediction

]
