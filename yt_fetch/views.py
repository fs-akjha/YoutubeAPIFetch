from django.shortcuts import render
from django.conf import settings
import requests

def index(request):
    search_url='https://www.googleapis.com/youtube/v3/search'
    video_url='https://www.googleapis.com/youtube/v3/videos'
    channel_url='https://www.googleapis.com/youtube/v3/channels'

    search_params={
        'part':'snippet',
        'q':'#IndianDefence',
        'maxResults':10,
        'type':'video',
        'key':settings.YOUTUBE_DATA_API_KEY
    }

    cparams={
        'part':'snippet',
        'q':'#IPL',
        'maxResults':10,
        'type':'channel',
        'key':settings.YOUTUBE_DATA_API_KEY
    }




    channel_ids=[]
    r=requests.get(search_url,params=cparams)
    cresults=r.json()['items']

    for cresult in cresults:
        channel_ids.append(cresult['id']['channelId'])

    channel_params={
        'key':settings.YOUTUBE_DATA_API_KEY,
        'part':'snippet,status,brandingSettings,contentDetails,topicDetails,statistics',
        'id':','.join(channel_ids)
    }

    rc=requests.get(channel_url,params=channel_params)

    print(rc.text)


    video_ids=[]
    r=requests.get(search_url,params=search_params)
    results=r.json()['items']

    for result in results:
        video_ids.append(result['id']['videoId'])

    video_params={
        'key':settings.YOUTUBE_DATA_API_KEY,
        'part':'snippet,contentDetails,statistics,status,topicDetails,player',
        'id':','.join(video_ids)
    }

    r=requests.get(video_url,params=video_params)

    # print(r.text)

    return render(request,'yt_fetch/index.html')