from django.shortcuts import render
from .videoID import idGen, getInfo
from random import choice
import requests


def home(request):
    yt_api_key = "AIzaSyBvSej7w_2Aa_C79eWRBY0AYCrYbuKuM74"
    search_url = "https://www.googleapis.com/youtube/v3/search"
    video_url = "https://www.googleapis.com/youtube/v3/videos"
    if request.method == "GET":
        if idGen() is None:
            return render(
                request,
                "youtube/home.html",
                {"error_qouta": "Youtube API qouta exceeded",},
            )

        else:
            videoIds = ""
            videoIds = ",".join(idGen())
        # list returned by idgen()
        try:
            parameter_video = {
                "key": yt_api_key,
                "part": "snippet",
                "id": videoIds
                }
            result_video = requests.get(video_url, params=parameter_video).json()
            return render(request, "youtube/home.html", {"random_video": result_video},)
        except KeyError:
            return render(request, "youtube/home.html", {"error": "error in searching"})

    else:
        result_video = getInfo(request.POST["search"])
        if result_video is None:
            return render(
                request,
                "youtube/home.html",
                {"error_qouta": "Youtube API qouta exceeded"},
            )
        elif result_video == 0:
            return render(
                request,
                "youtube/home.html",
                {"error_channel": "Error in Search"},
            )

        else:

            return render(
                request,
                "youtube/home.html",
                {"result_video": result_video},
            )

