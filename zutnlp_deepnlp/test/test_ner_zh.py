
from __future__ import unicode_literals
from zutnlp_deepnlp import ner_tagger
tagger = ner_tagger.load_model(name = 'zh')
text = "患者 3 月前 前因 直肠 直肠癌 肠癌 于 在 我院 于 全麻 下行 直肠 直肠癌 肠癌 根治术 DIXON术 上腹部 闷痛不适 排黑便"
words = text.split(" ")
tagging = tagger.predict(words)
for (w,t) in tagging:
    pair = w + "/" + t
    print (pair)
