from inc import functions
import urlparse
import re
import sys


def VineThumbnail(request):
    
    image_found = False
    url = request.get_full_path()
    video_id = url.split('/')[2]
    match = re.search(r'[a-zA-Z0-9]{10,15}', video_id)

    if match:
        filename = video_id + '.jpg'

        if not functions.imageExists(filename):
            data = functions.read('https://api.vineapp.com/timelines/posts/s/'+ video_id)
            tests = {'records', 'data'}

            if any(test in data for test in tests):
                thumbnail_url = data['data']['records'][0]['thumbnailUrl']
                functions.saveImage(thumbail_url, filename)

                if functions.imageExists(filename):
                    image_found = True;
        else:
            image_found = True


    if image_found:
        return functions.showImage(filename)
    else:
        return functions.showImage('../blank.jpg')