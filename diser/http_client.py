import requests

class HTTP:

    def __init__(self, token):
        self.token = token
        self.base = "https://discord.com/api/v10"

    def send(self, channel_id, content):

        url = f"{self.base}/channels/{channel_id}/messages"

        headers = {
            "Authorization": f"Bot {self.token}"
        }

        data = {
            "content": content
        }

        requests.post(url, headers=headers, json=data)
