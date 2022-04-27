import googleapiclient.discovery as dis
from urllib.parse import parse_qs,urlparse

#https://youtube.com/playlist?list=PLPV88C9y83a6JZPkaZKk4yi7mTdttEE97

hasIdAlready = input("If you have the Id press 1 \nIf you have a link press 2") == "1"

if hasIdAlready:
    playlistId = input("Paste your Playlist ID here:")
else:
    url = input("Paste your Playlist link here:")
    query = parse_qs(urlparse(url).query,keep_blank_values=True)
    playlistId = query["list"][0]

youtube = dis.build("youtube","v3",developerKey="AIzaSyC-04gvOEXnnp3hoCcacMn72lJuDo4eDFk")
request = youtube.playlistItems().list(part = "snippet",playlistId = playlistId,maxResults = 100)
response = request.execute()
playlistItems = []

while request is not None:
    response = request.execute()
    playlistItems+=response["items"]
    request = youtube.playlistItems().list_next(request,response)

print()
for link in playlistItems:
    print("https://www.youtube.com/watch?v="+link["snippet"]["resourceId"]["videoId"]+"&list="+playlistId+"&t=0s")

print()
print(f"Found {len(playlistItems)} video links.")