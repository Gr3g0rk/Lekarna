import requests
class DobiHtml:
    @staticmethod
    def dobi_html(url):
        """vrne vsebino html datoteke"""
        odziv = requests.get(url, headers = {'Accept-Language': 'en-US,en;q=0.5'})
        return odziv.text