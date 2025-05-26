# services.py

import cloudinary.uploader
from .models import File
from django.core.exceptions import ValidationError

# Ideally move this to settings.py and import settings to use them here
cloudinary.config( 
    cloud_name="dqz4xasg5", 
    api_key="969749835419172", 
    api_secret="a5v1GiUa5cPZDpOLAdG3MIPAA-0",
    secure=True
)


def upload_file_to_cloudinary(file, folder_name):
    """Uploads a single file to Cloudinary and returns the secure URL."""
    try:
        result = cloudinary.uploader.upload(file, folder=folder_name)
        return result.get('secure_url')
    except Exception as e:
        raise Exception(f"Cloudinary upload failed: {str(e)}")


def handle_file_upload(files, user):
    """Handles validation, DB record creation, and file uploads."""
    if not files:
        raise ValidationError("No file provided")
    if not user.is_authenticated:
        raise ValidationError("User not authenticated")

    file_record = File.objects.create(
        user_id=user.id,
        role=user.role,
        created_by_id=user.id
    )

    folder_name = f"Data_{file_record.id}"
    uploaded_urls = []

    for file in files:
        url = upload_file_to_cloudinary(file, folder_name)
        if url:
            uploaded_urls.append(url)

    if uploaded_urls:
        file_record.file_url = uploaded_urls[0]
        file_record.save()

    return uploaded_urls
