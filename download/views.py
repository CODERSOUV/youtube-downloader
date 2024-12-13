import ssl
from pytube import YouTube
from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    if request.method == "POST":
        video_url = request.POST.get('video_url')
        try:
            yt = YouTube(video_url)
            stream = yt.streams.get_highest_resolution()
            response = HttpResponse(
                stream.stream_to_buffer(),
                content_type='video/mp4',
            )
            response['Content-Disposition'] = f'attachment; filename="{yt.title}.mp4"'
            return response
        except Exception as e:
            return render(request, "home.html", {"error": f"Error: {str(e)}"})
    return render(request, "home.html")
