import datetime
import json
import os
import random
import re
import smtplib
import subprocess
import sys
import time
import webbrowser

if __name__ == "__main__":
    import requests
    import json
    url = ('https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=d8e6876288a8403784ec1f84cfb2f0bd')

    response = requests.get(url)
    text = response.text
    my_json = json.loads(text)
    for i in range(0, 11):
        print(my_json['articles'][i]['title'])