from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthTests(APITestCase):
    def setUp(self):
        # Because in main urls.py, LoginUtility URLs are included as 't/'
        self.register_url = '/t/register'
        self.login_url = '/t/login'
        self.current_user_url = '/t/get-user'

        # User data for registration
        self.user_data = {
            "username": "testuser",
            "password": "TestPassword123!",
            "email": "testuser@example.com",
            "first_name": "Test",
            "role": "user"  # Adjust if your User model expects something else here
        }
        
        # Create a user for login and get-user tests
        self.user = User.objects.create_user(
            username="existinguser",
            password="Password123!",
            email="existinguser@example.com",
            first_name="Existing",
            role="admin"  # adjust if necessary
        )

    def test_register_user(self):
        response = self.client.post(self.register_url, data=self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get("message"), "User created")
        self.assertTrue(User.objects.filter(username="testuser").exists())

    def test_register_invalid_user(self):
        # Missing password field to trigger error
        invalid_data = self.user_data.copy()
        invalid_data.pop("password")
        response = self.client.post(self.register_url, data=invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("password", response.data)

    def test_login_user(self):
        # Login with existing user credentials
        login_data = {
            "username": "existinguser",
            "password": "Password123!"
        }
        response = self.client.post(self.login_url, data=login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)


    def test_login_invalid_user(self):
        login_data = {
            "username": "wronguser",
            "password": "wrongpassword"
        }
        response = self.client.post(self.login_url, data=login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_current_user_authenticated(self):
        # Step 1: Login to get access token
        login_data = {
            "username": "existinguser",
            "password": "Password123!"
        }
        login_response = self.client.post(self.login_url, data=login_data, format='json')
        self.assertEqual(login_response.status_code, status.HTTP_200_OK)
        access_token = login_response.data.get('access')
        self.assertIsNotNone(access_token)

        # Step 2: Set Authorization header
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

        # Step 3: Call the protected endpoint
        response = self.client.get(self.current_user_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "existinguser")
        self.assertEqual(response.data["role"], "admin")

    def test_get_current_user_unauthenticated(self):
        response = self.client.get(self.current_user_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
