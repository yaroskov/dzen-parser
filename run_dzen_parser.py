from functionality.DzenParser import DzenParser


dzen_parser = DzenParser(days_number=30, keyword="игра", top_words_number=50)
dzen_parser.run()
