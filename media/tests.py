from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
import io
from PIL import Image

User = get_user_model()

def generate_test_image():
    img = Image.new('RGB', (100, 100), color='red')
    file_obj = io.BytesIO()
    img.save(file_obj, format='PNG')
    file_obj.seek(0)
    return file_obj

class FileUploadTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)  # << THIS IS THE KEY

    def test_upload_single_file_authenticated(self):
        image = generate_test_image()
        upload_file = SimpleUploadedFile("test.png", image.read(), content_type="image/png")
        url = reverse('file')  # Make sure this name matches your URL pattern
        response = self.client.post(url, {'files': upload_file}, format='multipart')
        self.assertEqual(response.status_code, 200)
