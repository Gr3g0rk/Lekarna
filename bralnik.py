import requests

class Bralnik:
    @staticmethod
    def pridobi_html(url):
        """Pridobi html vsebino spletne strani."""
        odziv = requests.get(url, headers = {
            'Accept-Language': 'en-US,en;q=0.5'
            })
        return odziv.text