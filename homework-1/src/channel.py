import os
import json
from googleapiclient.discovery import build


class Channel:

    def __init__(self, channel_id: str):
        self.channel_id = channel_id
        youtube = build('youtube', 'v3', developerKey=os.environ.get('API_KEY'))
        self.channel = youtube.channels().list(part='snippet,statistics', id=self.channel_id).execute()

    def print_info(self):
        """Выводит в консоль информацию о канале"""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))
