import requests
import io
from PIL import ImageDraw
from PIL import Image
SUBSCRIPTION_KEY = '3bc0862af3214ec3b8090c388298a1de'
assert SUBSCRIPTION_KEY
face_api_url = 'https://20220419liu.cognitiveservices.azure.com/face/v1.0/detect'

img = Image.open('nakata.png')
#print(img)
with io.BytesIO() as output:
    img.save(output, format="png")
    binary_img = output.getvalue()

#print(binary_img)
headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY
    }

params = {
    'returnFaceId' : 'true',
    'returnFaceAttributes' : 'age,gender,headpose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur'
}
res = requests.post(face_api_url, params=params,headers=headers, data=binary_img)

print(res)
results = res.json()

for result in results:


#print(result)

  rect = result['faceRectangle']
#print(rect)


  draw = ImageDraw.Draw(img)
#draw.line([(0,50),(200,50),(0,150),(200,150)],fill='red',width=5)


  draw.rectangle([(rect['left'],rect['top']),(rect['left']+rect['width'],rect['top']+rect['height'])],fill=None,outline='green',width=5)

print(img)