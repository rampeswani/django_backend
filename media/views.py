from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser
from .services import handle_file_upload

from rest_framework.response import Response
from rest_framework import status
from rest_framework.response import Response

@api_view(['POST'])
@parser_classes([MultiPartParser])
def upload_file(request):
    try:
        files = request.FILES.getlist('files', None)

        user = request.user

        uploaded_urls = handle_file_upload(files, user)

        return Response({
            'status': 'success',
            'message': 'File(s) uploaded successfully',
            'file_urls': uploaded_urls
        })

    except Exception as e:
        import traceback
        traceback.print_exc()
        return Response({'status': 'error', 'message': str(e)}, status=400)
