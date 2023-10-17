from datetime import datetime, timedelta
from functionality.components.DzenParserComponents import DzenParserComponents


class DzenParser:
    current_date = datetime.now()
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'Cookie': 'nc=search-visits-per-week=1:1697485425000; zen_sso_checked=1; _yasc=Ac8+4q2PKdYCTHM0ioa35/SP6en7V3SQlN975irU3wLX0oWPdrF0fUvNESlimc3ZDQ==; Session_id=noauth:1697485424; sessar=1.1183.CiDPTkwuCDsbeGix-rU1Y9HPmZtWnotjb7bYqZ7pDbMAaw.c7AGJuDBazSmViTTenS-Zn-bzzKQTf6ZXIbTjaPH3jU; yandex_login=; ys=c_chck.525333564; yandexuid=3527933111692908044; mda2_beacon=1697485424679; sso_status=sso.passport.yandex.ru:synchronized; rec-tech=true; Zen-User-Data={%22zen-theme%22:%22light%22}; vid=97044b3ac710ed17; vidExpirationOneDay=true; tmr_lvid=093172792cb7ef89096f8bb9550c15ed; tmr_lvidTS=1697485429623; _ym_uid=1697485430491488670; _ym_d=1697485430; vsd=eyJnZW8iOiIxODgiLCJ1YSI6IkNIUk9NRSIsImVhIjoyNiwiZWciOjJ9; _ym_isad=2; tmr_detect=0%7C1697485432624',
    }

    def __init__(self, days_number, keyword, top_words_number):
        self.days_number = days_number
        self.keyword = keyword
        self.one_month_ago = self.current_date - timedelta(days=days_number)
        self.top_words_number = top_words_number
        self.url = f"https://dzen.ru/news/search?issue_tld=ru&text={self.keyword}+date%3A" \
              f"{self.one_month_ago.strftime('%Y%m%d')}..{self.current_date.strftime('%Y%m%d')}&sortby=date"

    def run(self):
        content = DzenParserComponents.get_site_content(self.url, self.headers)
        wordcloud_text = DzenParserComponents.get_top_words(content, self.top_words_number)
        DzenParserComponents.draw_wordcloud(wordcloud_text)
