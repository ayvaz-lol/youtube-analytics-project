import os
import json
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""

        # Иницилизация атрибутов класса
        self.__channel_id = channel_id
        youtube = self.get_service()
        self.channel = youtube.channels().list(part='snippet,statistics',
                                               id=self.channel_id).execute()  # Информация о канале
        self.title = self.channel['items'][0]['snippet']['title']
        self.description = self.channel['items'][0]['snippet']['description']
        self.url = "https://www.youtube.com/channel/" + channel_id
        self.subscriber_count = int(self.channel['items'][0]['statistics']['subscriberCount'])
        self.video_count = int(self.channel['items'][0]['statistics']['videoCount'])
        self.view_count = int(self.channel['items'][0]['statistics']['viewCount'])

    @property
    def channel_id(self):
        """Геттер параметра channel_id"""
        return self.__channel_id

    @channel_id.setter
    def channel_id(self, new_name):
        """Ложный сеттер. При попытке изменить channel_id выводит сообщение об ошибке"""
        print("AttributeError: property 'channel_id' of 'Channel' object has no setter")

    @classmethod
    def get_service(cls):
        api_key = os.environ.get('API_KEY')
        return build('youtube', 'v3', developerKey=api_key)

    def to_json(self, filename):
        """Сохраняет информацию находящуюся в атрибутах экземпляра в файл"""
        dictionary = {
                "channel_id": self.__channel_id,
                "channel_title": self.title,
                "channel_description": self.description,
                "channel_url": self.url,
                "subscriber_count": self.subscriber_count,
                "video_count": self.video_count,
                "view_count": self.view_count
            }
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(dictionary, file, ensure_ascii=False)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))
        pass
