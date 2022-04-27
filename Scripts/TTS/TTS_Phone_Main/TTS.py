from gtts import gTTS as g

class TTS:
    @staticmethod
    def convert(text, path, languageID = 0):
        if languageID == 0:
            language = 'de'  # 'en'
        else:
            language = 'en'

        g(text, lang=language).save(path)



