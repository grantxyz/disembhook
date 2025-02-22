import requests
import json

class PyHook:
    def __init__(self, url):
        """Initialize the webhook with the given URL."""
        self.url = url

    def send(self, content):
        """
        Send a message or an embed depending on the instance name.
        If the instance name ends with 'emb', it sends an embed.
        """
        import inspect
        
        frame = inspect.currentframe().f_back
        var_name = [name for name, val in frame.f_locals.items() if val is self]

        if var_name and var_name[0].endswith("emb"):
            return self.send_embed("PyHook Message", content)
        else:
            return self.send_message(content)

    def send_message(self, content):
        """Send a normal text message to the webhook."""
        data = {"content": content}
        return self._send_request(data)

    def send_embed(self, title, description, color=0x3498db):
        """Send an embed message to the webhook."""
        embed = {
            "title": title,
            "description": description,
            "color": color
        }
        data = {"embeds": [embed]}
        return self._send_request(data)

    def send_file(self, file_path):
        """Send a file to the webhook."""
        with open(file_path, "rb") as file:
            files = {"file": file}
            return requests.post(self.url, files=files)

    def _send_request(self, data):
        """Internal method to send a POST request to the webhook."""
        headers = {"Content-Type": "application/json"}
        response = requests.post(self.url, json=data, headers=headers)
        return response.status_code, response.text

if __name__ == "__main__":
    webhook = PyHook("YOUR_WEBHOOK_URL_HERE")
    webhook.send("This is a normal message!")

    webhookemb = PyHook("YOUR_WEBHOOK_URL_HERE")
    webhookemb.send("This message is an embed!")
