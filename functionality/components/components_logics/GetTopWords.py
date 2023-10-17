import re
from bs4 import BeautifulSoup
from collections import Counter


class GetTopWords:
    @staticmethod
    def get_top_words(content, top_words_number):
        soup = BeautifulSoup(content, "html.parser")

        articles = soup.find_all("article", class_="news-search-story news-search__main-item mg-grid__item")

        text = ""
        for article in articles:
            title = article.find("div", class_="mg-snippet__title").text.strip()
            summary = article.find("span", class_="mg-snippet__text").text
            text += title + " " + summary + " "

        text = re.sub('[^a-zA-Zа-яА-Я0-9- ]', '', text)
        words = text.split()

        words_cleared = []
        for word in words:
            if len(word) > 3:
                words_cleared.append(word)

        word_counts = Counter(words_cleared)
        top_words = word_counts.most_common(top_words_number)

        wordcloud_text = ""
        for word in top_words:
            wordcloud_text += word[0] + " "

        return wordcloud_text
