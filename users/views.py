from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User

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

