from dotenv import load_dotenv
import os
from sys import exit
import requests
from rich.console import Console


class Translate:
    def __init__(self):
        self._env = load_dotenv()
        self.c = Console()

    def translate(self, text) -> None:
        self.c.log(f" Text in translate method: [blue]{text}")
        try:
            url = os.getenv('URL')
            key = os.getenv('KEY')
            headers = {
                'content-type': 'application/json',
                'X-RapidApi-Key': key,
            }

            response = requests.request("POST", url, json='text', headers=headers)

            print(response.text)

            if response.status_code == 400:
                print('Erro na API de tradução')
        except Exception as ex:
            exit(1)
            self.c.log(f'Um erro ocorreu ao traduzir [red]{ex}')