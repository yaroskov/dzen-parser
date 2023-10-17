from functionality.components.components_logics.GetSiteContent import GetSiteContent
from functionality.components.components_logics.GetTopWords import GetTopWords
from functionality.components.components_logics.DrawWordCloud import DrawWordCloud


class DzenParserComponents:
    @staticmethod
    def get_site_content(url, headers):
        return GetSiteContent.get_site_content(url, headers)

    @staticmethod
    def get_top_words(content, top_words_number):
        return GetTopWords.get_top_words(content, top_words_number)

    @staticmethod
    def draw_wordcloud(wordcloud_text):
        return DrawWordCloud.draw_wordcloud(wordcloud_text)
