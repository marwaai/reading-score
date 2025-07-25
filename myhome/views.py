from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import os

def home(request):
    return render(request, 'myhome.html')

@csrf_exempt
def upload_audio(request):
    if request.method == 'POST':
        audio_file = request.FILES.get('audio')
        if not audio_file:
            return JsonResponse({"error": "No audio file found."}, status=400)

        # 📁 تأكد من وجود MEDIA_ROOT
        save_dir = os.path.join(settings.MEDIA_ROOT, 'upload-audio')
        os.makedirs(save_dir, exist_ok=True)

        filename = 'uploaded_audio.wav'
        save_path = os.path.join(save_dir, filename)

        try:
            with open(save_path, 'wb+') as destination:
                for chunk in audio_file.chunks():
                    destination.write(chunk)

            relative_path = os.path.join('media', 'upload-audio', filename)  # path للفرونت/الويب سوكيت
            print(f"✅ File saved to: {save_path}")

            return JsonResponse({
                "message": "File saved successfully.",
                "filename": filename,
                "path": relative_path  # هذا هو اللي تستخدمينه في WebSocket
            })

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=405)
