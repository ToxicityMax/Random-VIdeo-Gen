import requests
from .randomWords import genWords

yt_api_key = "AIzaSyBvSej7w_2Aa_C79eWRBY0AYCrYbuKuM74"
search_url = "https://www.googleapis.com/youtube/v3/search"
video_url = "https://www.googleapis.com/youtube/v3/videos"
channel_url = "https://www.googleapis.com/youtube/v3/channels"


def idGen():
    videoids = []
    words = genWords()
    for word in words:
        parameter_search = {
            "key": yt_api_key,
            "part": "snippet",
            "q": word,
            "maxResults": 1,
        }
        result_search = requests.get(search_url, params=parameter_search).json()

        try:
            videoids.append(result_search["items"][0]["id"]["videoId"])
        except KeyError:
            try:
                result_search["error"]["code"] == 403
                return None
            except KeyError:
                pass

    return videoids


def getInfo(query):
    # returns a json and a string
    parameter_search = {
        "key": yt_api_key,
        "part": "snippet",
        "q": query,
        "maxResults": 1,
    }
    result_search = requests.get(search_url, params=parameter_search).json()

    try:
        videoid = result_search["items"][0]["id"]["videoId"]
        channelid = 0
    except KeyError:
        try:
            channelid = result_search["items"][0]["id"]["channelId"]
        except KeyError:
            result_search["error"]["code"] == 403
            return None
        if channelid == 0:

            parameter_video = {
                "key": yt_api_key,
                "part": "snippet",
                "id": videoid,
            }

            return requests.get(video_url, params=parameter_video).json()
        else:
            return 0

            #parameter_channel = {
            #    "key": yt_api_key,
            #    "part": "snippet",
            #    "id": channelid,
            #}
            #return requests.get(channel_url, params=parameter_channel).json(), channelid

