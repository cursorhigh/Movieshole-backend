from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User
from django.contrib.auth.models import User as Users
from django.contrib.auth import authenticate

@csrf_exempt
def google_auth(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        data=data['data']
        email = data.get('email')
        name = data.get('name')
        id = data.get('id')
        picture = data.get('picture')
        if email and name and id:
            user, created = User.objects.get_or_create(email=email, defaults={'name': name,'google_id': id,'picture': picture})
            if not created:
                user.name = name
                user.save()
            return JsonResponse({'status': 'success', 'user_id': user.id})
        return JsonResponse({'status': 'error', 'message': 'Invalid data'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

@csrf_exempt
def loginnow(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get("email")
        username=username.split('@')[0]
        email = data.get("email")
        password = data.get("password")
        if not username or not password:
            return JsonResponse(
                {"message": "Please provide both username and password."},
                status=400,
            )
        user = authenticate(username=username, password=password,email=email)
        if user is None:
            return JsonResponse(
                {"message": "Invalid username or password."},
                status=401,
            )
        return JsonResponse({'status': 'success',},status=200)
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)