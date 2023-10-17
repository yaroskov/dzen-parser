import requests


class GetSiteContent:
    @staticmethod
    def get_site_content(url, headers):
        response = requests.get(url, headers=headers)
        content = response.content.decode("utf_8_sig")
        return content
