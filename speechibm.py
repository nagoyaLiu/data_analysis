# coding: UTF-8
import json
from os.path import join, dirname
from ibm_watson  import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# FIX_VALUE
FILE_NAME='C:\\Users\\B20735\\Desktop\\博士研究\\日本トップテン\\チャンネルNO1\\1.wav'

authenticator = IAMAuthenticator('95QLkX2S0hUO6iBv8dbQ1wJJllYqvXN8rHN4f2_MdVJc')
speech_to_text = SpeechToTextV1(
    authenticator=authenticator
)

speech_to_text.set_service_url('https://api.au-syd.speech-to-text.watson.cloud.ibm.com/instances/69bd3196-360e-48fa-95c8-81c4ca53ccfc')

class MyRecognizeCallback(RecognizeCallback):
    def __init__(self):
        RecognizeCallback.__init__(self)

    def on_data(self, data):
        print(json.dumps(data, ensure_ascii=False))


    def on_error(self, error):
        print('Error received: {}'.format(error))

    def on_inactivity_timeout(self, error):
        print('Inactivity timeout: {}'.format(error))

myRecognizeCallback = MyRecognizeCallback()

with open(join(dirname(__file__), './.', FILE_NAME),
              'rb') as audio_file:
    audio_source = AudioSource(audio_file)
    speech_to_text.recognize_using_websocket(
        audio=audio_source,
        content_type='audio/mp3',
        recognize_callback=myRecognizeCallback,
        model='ja-JP_BroadbandModel',
        keywords=['colorado'],
         keywords_threshold=0.5,
        max_alternatives=1)