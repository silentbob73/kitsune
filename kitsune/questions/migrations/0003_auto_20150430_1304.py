# -*- coding: utf-8 -*-
"""
Update list of locale choices in the `question.locale` and `questionlocale.locale` fields.
"""

from __future__ import unicode_literals

from django.db import models, migrations
import kitsune.sumo.models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_initial_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='locale',
            field=kitsune.sumo.models.LocaleField(default=b'en-US', max_length=7, choices=[(b'af', 'Afrikaans'), (b'ar', '\u0639\u0631\u0628\u064a'), (b'az', 'Az\u0259rbaycanca'), (b'bg', '\u0411\u044a\u043b\u0433\u0430\u0440\u0441\u043a\u0438'), (b'bn-BD', '\u09ac\u09be\u0982\u09b2\u09be (\u09ac\u09be\u0982\u09b2\u09be\u09a6\u09c7\u09b6)'), (b'bn-IN', '\u09ac\u09be\u0982\u09b2\u09be (\u09ad\u09be\u09b0\u09a4)'), (b'bs', 'Bosanski'), (b'ca', 'catal\xe0'), (b'cs', '\u010ce\u0161tina'), (b'da', 'Dansk'), (b'de', 'Deutsch'), (b'ee', '\xc8\u028begbe'), (b'el', '\u0395\u03bb\u03bb\u03b7\u03bd\u03b9\u03ba\u03ac'), (b'en-US', 'English'), (b'es', 'Espa\xf1ol'), (b'et', 'eesti keel'), (b'eu', 'Euskara'), (b'fa', '\u0641\u0627\u0631\u0633\u06cc'), (b'fi', 'suomi'), (b'fr', 'Fran\xe7ais'), (b'fy-NL', 'Frysk'), (b'ga-IE', 'Gaeilge (\xc9ire)'), (b'gl', 'Galego'), (b'gu-IN', '\u0a97\u0ac1\u0a9c\u0ab0\u0abe\u0aa4\u0ac0'), (b'ha', '\u0647\u064e\u0631\u0652\u0634\u064e\u0646 \u0647\u064e\u0648\u0652\u0633\u064e'), (b'he', '\u05e2\u05d1\u05e8\u05d9\u05ea'), (b'hi-IN', '\u0939\u093f\u0928\u094d\u0926\u0940 (\u092d\u093e\u0930\u0924)'), (b'hr', 'Hrvatski'), (b'hu', 'Magyar'), (b'id', 'Bahasa Indonesia'), (b'ig', 'As\u1ee5s\u1ee5 Igbo'), (b'it', 'Italiano'), (b'ja', '\u65e5\u672c\u8a9e'), (b'km', '\u1781\u17d2\u1798\u17c2\u179a'), (b'kn', '\u0c95\u0ca8\u0ccd\u0ca8\u0ca1'), (b'ko', '\ud55c\uad6d\uc5b4'), (b'ln', 'Ling\xe1la'), (b'lt', 'lietuvi\u0173 kalba'), (b'ml', '\u0d2e\u0d32\u0d2f\u0d3e\u0d33\u0d02'), (b'ne-NP', '\u0928\u0947\u092a\u093e\u0932\u0940'), (b'nl', 'Nederlands'), (b'no', 'Norsk'), (b'pl', 'Polski'), (b'pt-BR', 'Portugu\xeas (do Brasil)'), (b'pt-PT', 'Portugu\xeas (Europeu)'), (b'ro', 'rom\xe2n\u0103'), (b'ru', '\u0420\u0443\u0441\u0441\u043a\u0438\u0439'), (b'si', '\u0dc3\u0dd2\u0d82\u0dc4\u0dbd'), (b'sk', 'sloven\u010dina'), (b'sl', 'sloven\u0161\u010dina'), (b'sq', 'Shqip'), (b'sr-Cyrl', '\u0421\u0440\u043f\u0441\u043a\u0438'), (b'sw', 'Kiswahili'), (b'sv', 'Svenska'), (b'ta', '\u0ba4\u0bae\u0bbf\u0bb4\u0bcd'), (b'ta-LK', '\u0ba4\u0bae\u0bbf\u0bb4\u0bcd (\u0b87\u0bb2\u0b99\u0bcd\u0b95\u0bc8)'), (b'te', '\u0c24\u0c46\u0c32\u0c41\u0c17\u0c41'), (b'th', '\u0e44\u0e17\u0e22'), (b'tr', 'T\xfcrk\xe7e'), (b'uk', '\u0423\u043a\u0440\u0430\u0457\u043d\u0441\u044c\u043a\u0430'), (b'ur', '\u0627\u064f\u0631\u062f\u0648'), (b'vi', 'Ti\u1ebfng Vi\u1ec7t'), (b'wo', 'Wolof'), (b'xh', 'isiXhosa'), (b'yo', '\xe8d\xe8 Yor\xf9b\xe1'), (b'zh-CN', '\u4e2d\u6587 (\u7b80\u4f53)'), (b'zh-TW', '\u6b63\u9ad4\u4e2d\u6587 (\u7e41\u9ad4)'), (b'zu', 'isiZulu')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='questionlocale',
            name='locale',
            field=kitsune.sumo.models.LocaleField(default=b'en-US', unique=True, max_length=7, choices=[(b'af', 'Afrikaans'), (b'ar', 'Arabic'), (b'az', 'Azerbaijani'), (b'bg', 'Bulgarian'), (b'bn-BD', 'Bengali (Bangladesh)'), (b'bn-IN', 'Bengali (India)'), (b'bs', 'Bosnian'), (b'ca', 'Catalan'), (b'cs', 'Czech'), (b'da', 'Danish'), (b'de', 'German'), (b'ee', 'Ewe'), (b'el', 'Greek'), (b'en-US', 'English'), (b'es', 'Spanish'), (b'et', 'Estonian'), (b'eu', 'Basque'), (b'fa', 'Persian'), (b'fi', 'Finnish'), (b'fr', 'French'), (b'fy-NL', 'Frisian'), (b'ga-IE', 'Irish (Ireland)'), (b'gl', 'Galician'), (b'gu-IN', 'Gujarati'), (b'ha', 'Hausa'), (b'he', 'Hebrew'), (b'hi-IN', 'Hindi (India)'), (b'hr', 'Croatian'), (b'hu', 'Hungarian'), (b'id', 'Indonesian'), (b'ig', 'Igbo'), (b'it', 'Italian'), (b'ja', 'Japanese'), (b'km', 'Khmer'), (b'kn', 'Kannada'), (b'ko', 'Korean'), (b'ln', 'Lingala'), (b'lt', 'Lithuanian'), (b'ml', 'Malayalam'), (b'ne-NP', 'Nepali'), (b'nl', 'Dutch'), (b'no', 'Norwegian'), (b'pl', 'Polish'), (b'pt-BR', 'Portuguese (Brazilian)'), (b'pt-PT', 'Portuguese (Portugal)'), (b'ro', 'Romanian'), (b'ru', 'Russian'), (b'si', 'Sinhala'), (b'sk', 'Slovak'), (b'sl', 'Slovenian'), (b'sq', 'Albanian'), (b'sr-Cyrl', 'Serbian'), (b'sw', 'Swahili'), (b'sv', 'Swedish'), (b'ta', 'Tamil'), (b'ta-LK', 'Tamil (Sri Lanka)'), (b'te', 'Telugu'), (b'th', 'Thai'), (b'tr', 'Turkish'), (b'uk', 'Ukrainian'), (b'ur', 'Urdu'), (b'vi', 'Vietnamese'), (b'wo', 'Wolof'), (b'xh', 'Xhosa'), (b'yo', 'Yoruba'), (b'zh-CN', 'Chinese (Simplified)'), (b'zh-TW', 'Chinese (Traditional)'), (b'zu', 'Zulu')]),
            preserve_default=True,
        ),
    ]
