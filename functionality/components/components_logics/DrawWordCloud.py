import matplotlib.pyplot as plt
from wordcloud import WordCloud


class DrawWordCloud:
    @staticmethod
    def draw_wordcloud(wordcloud_text):
        wordcloud = WordCloud(
            width=2000,
            height=1500,
            random_state=1,
            background_color='black',
            margin=20,
            colormap='Pastel1',
            collocations=False).generate(wordcloud_text)

        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()
