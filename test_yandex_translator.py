"""yandex translator test"""

from yandex_translate import YandexTranslate
from config import API_KEY


translate = YandexTranslate(API_KEY)
print('Languages:', translate.langs)
print('Translate directions:', translate.directions)
print('Detect language:', translate.detect('Привет, мир!'))
print('Translate:', translate.translate('Привет, мир!', 'ru-be'))  # or just 'en'
