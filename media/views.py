import cloudinary.uploader
from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser
from .models import File

cloudinary.config( 
    cloud_name = "dqz4xasg5", 
    api_key = "969749835419172", 
    api_secret = "a5v1GiUa5cPZDpOLAdG3MIPAA-0", # Click 'View API Keys' above to copy your API secret
    secure=True
)


@api_view(['POST'])
@parser_classes([MultiPartParser])
def upload_file(request):
    file = request.FILES.getlist('file',None)

    print("session",request)
    print("file is backend",file)
    user = request.user
    print("Session:", request.session)
    print("File received in backend:", file)

    if user.is_authenticated:
        print("User ID:", user.id)
        print("Username:", user.username)

        data  = File.objects.create(
            user_id = user.id,
            role = user.role,
            created_by_id = user.id 
        )
        if file:  # Ensure files were uploaded
            uploaded_urls = []  # Store all image URLs
            
            for file in file:
                # Upload file to Cloudinary
                response = cloudinary.uploader.upload(file, folder=f"Data_{data.id}")
                
                # Get the Cloudinary URL
                file_url = response.get('secure_url', '')  # Get secure URL
                
                if file_url:
                    uploaded_urls.append(file_url)

            # Store the first uploaded image URL (you can modify this for multiple images)
            if uploaded_urls:
                data.file_url = uploaded_urls[0]  # Save the first image
                data.save()
                #return redirect('property-list')
                return JsonResponse({
                    'status': 'success',
                    'message': 'File(s) uploaded successfully',
                    'file_urls': uploaded_urls
                })

   
    return JsonResponse({'status': 'error', 'message': 'No file provided'}, status=400)
