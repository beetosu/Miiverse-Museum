import urllib.request, json, requests
from io import BytesIO
from PIL import Image

#kinda weird, by virtue of how they were archived, but...
#first get the correct snapshot of the image from the internet archive api
#then, format that snapshot to be just the image
#finally, load that url into an image object, and return that
def get_drawing(baseURL):
    archiveURL = "http://archive.org/wayback/available?url="+baseURL
    content = urllib.request.urlopen(archiveURL).read().decode()
    data = json.loads(content)
    if len(data['archived_snapshots']) > 0:
        imageURL = data['archived_snapshots']['closest']['url']
        imgURLSegments = imageURL.split("/")
        imgURLSegments[4] += "if_"
        imageURL = "/".join(imgURLSegments)

        response = requests.get(imageURL)
        return Image.open(BytesIO(response.content))
