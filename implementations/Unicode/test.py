#!/usr/bin/env python3

from icu import RuleBasedCollator
from sys import exit

RULES = ''
with open ("rules.txt", "r") as rulesfile:
    RULES=rulesfile.read()

COLLATOR = RuleBasedCollator('[normalization on]\n'+RULES)

EXIT_CODE = 0

# Very simple test function: we 
def testOrder(argList, testName):
    global EXIT_CODE
    argList = argList.split(' ')
    newList = sorted(argList, key=COLLATOR.getSortKey)
    if argList != newList:
        EXIT_CODE = 1
        print(testName+' ... FAIL!')
        print("expected ["+(", ".join(argList))+"]")
        print("got      ["+(", ".join(newList))+"]")
    else:
        print(testName+' ... OK')

# Tests corresponding to all the prefix+superscript+main+suffix+second suffix possibilities,
# see https://github.com/eroux/tibetan-spellchecker/blob/master/doc/standard-syllable-structure.md
testOrder("ཀ ཀྭ ཀྱ ཀྲ ཀླ དཀ དཀྭ དཀྱ དཀྲ དཀླ བཀ བཀྭ བཀྱ བཀྲ བཀླ རྐ རྐྱ ལྐ སྐ སྐྱ སྐྲ བརྐ བརྐྱ བསྐ བསྐྱ བསྐྲ", "letter ཀ")
testOrder("ཁ ཁྭ ཁྱ ཁྲ མཁ མཁྭ མཁྱ མཁྲ འཁ འཁྭ འཁྱ འཁྲ", "letter ཁ")
testOrder("ག གྭ གྱ གྲ གྲྭ གླ དགྭ དགྱ དགྲ དགྲྭ བགྭ བགྱ བགྲ བགྲྭ བགླ མགྭ མགྱ མགྲ མགྲྭ འགྭ འགྱ འགྲ འགྲྭ རྒ རྒྱ ལྒ སྒ སྒྱ སྒྲ བརྒ བརྒྱ བསྒ བསྒྱ བསྒྲ", "letter ག")
testOrder("ང རྔ ལྔ སྔ བརྔ བསྔ", "letter ང")
testOrder("ཅ ཅྭ གཅ གཅྭ བཅ བཅྭ", "letter ཅ")
testOrder("ཇ རྗ ལྗ བརྗ", "letter ཇ")
testOrder("ཉ ཉྭ གཉྭ མཉྭ རྙ སྙ བརྙ བསྙ", "letter ཉ")
testOrder("ཏ ཏྭ ཏྲ གཏྭ གཏྲ བཏྭ བཏྲ རྟ ལྟ སྟ བརྟ བལྟ བསྟ", "letter ཏ")
testOrder("ཐ ཐྲ", "letter ཐ")
testOrder("ད དྭ དྲ དྲྭ གདྭ བདྭ མདྭ འདྭ འདྲ འདྲྭ རྡ ལྡ སྡ བརྡ བལྡ བསྡ", "letter ད")
testOrder("ན རྣ སྣ སྣྲ བརྣ བསྣ", "letter ན")
testOrder("པ པྱ པྲ དཔྱ དཔྲ ལྤ སྤ སྤྱ སྤྲ", "letter པ")
testOrder("ཕ ཕྱ ཕྱྭ ཕྲ འཕྱ འཕྱྭ འཕྲ", "letter ཕ")
testOrder("བ བྱ བྲ བླ དབྱ དབྲ འབྱ འབྲ རྦ ལྦ སྦ སྦྱ སྦྲ", "letter བ")
testOrder("མ མྱ མྲ དམྱ དམྲ རྨ རྨྱ སྨ སྨྱ སྨྲ", "letter མ")
testOrder("ཙ ཙྭ གཙྭ བཙྭ རྩ རྩྭ སྩ བརྩ བརྩྭ བསྩ", "letter ཙ")
testOrder("ཚ ཚྭ མཚྭ འཚྭ", "letter ཚ")
testOrder("ཛ རྫ བརྫ", "letter ཛ")
testOrder("ཞ ཞྭ གཞྭ བཞྭ", "letter ཞ")
testOrder("ཟ ཟྭ ཟླ བཟྭ བཟླ", "letter ཟ")
testOrder("ར རྭ རླ བརླ", "letter ར")
testOrder("ཤ ཤྭ གཤྭ བཤྭ", "letter ཤ")
testOrder("ས སྭ སྲ སླ གསྭ བསྭ བསྲ བསླ", "letter ས")
testOrder("ཧ ཧྭ ཧྲ ལྷ", "letter ཧ")
testOrder("ཀི ཀུ ཀེ ཀོ", "standard vowels")
testOrder("ཀ ཀཱ ཀི ཀཱི ཀྀ ཀཱྀ ཀུ ཀཱུ ཀེ ཀཻ ཀེེ ཀོ ཀོོ ཀཽ", "all vowels (+ee, oo)")
testOrder("ཀག ཀང ཀད ཀན ཀབ ཀམ ཀའ ཀའུ ཀར ཀལ ཀས", "standard suffixes")
testOrder("ཀག ཀགས ཀང ཀངས ཀད ཀན ཀབ ཀབས ཀམ ཀམས ཀའ ཀའུ ཀར ཀལ ཀས", "standard and second suffixes")
testOrder("ཀག ཀགས ཀང ཀངས ཀད ཀན ཀབ ཀབས ཀམ ཀམས ཀའ ཀའང ཀའམ ཀའི ཀའིའོ ཀའུ ཀའུའང ཀའུའམ ཀའུའི ཀའུའིའོ ཀའུའོ ཀའུར ཀའུས ཀའོ ཀར ཀལ ཀས", "standard, second and grammatical suffixes")
testOrder("ཀིག ཀིགས ཀིང ཀིངས ཀིད ཀིན ཀིབ ཀིབས ཀིམ ཀིམས ཀིའ ཀིའང ཀིའམ ཀིའི ཀིའིའོ ཀིའུ ཀིའུའང ཀིའུའམ ཀིའུའི ཀིའུའིའོ ཀིའུའོ ཀིའོ ཀིར ཀིལ ཀིས", "standard, second and grammatical suffixes with i")
testOrder("ཀག ཀགས ཀང ཀྃ ཀངས ཀད ཀམ ཀཾ ཀམས ཀའ", "standard, second and contracted suffixes")
testOrder("ཀིག ཀིགས ཀིང ཀིྃ ཀིངས ཀིད ཀིམ ཀིཾ ཀིམས ཀིའ", "contracted suffixes with i")
testOrder("ཀཀ ཀཁ ཀག ཀགས ཀང ཀངས ཀཉ ཀཏ ཀཊ ཀཐ ཀཋ ཀད ཀཌ ཀན ཀཎ ཀནད ཀཔ ཀཕ ཀབ ཀབས ཀམ ཀཾ ཀམས ཀཙ ཀཚ ཀཛ ཀཝ ཀའ ཀའང ཀའམ་ཀའན ཀའས ཀའི ཀའིམ ཀའུ ཀའུའི ཀའུར ཀའུས ཀའེ ཀའོ ཀཡ ཀར ཀརད ཀལ ཀལད ཀཤ ཀཥ ཀས ཀཧ", "suffixes (Di Jiang) (fixed)")
testOrder("ཀྙ ཀྥ ཀྭ ཀྱ ཀྱྭ ཀྱྲ ཀྲ ཀྲྭ ཀྲྱ ཀླ ཀྵ ཀྷ ཀྷྭ ཀྷྲ", "subscripts (Di Jiang)")
testOrder("ཨོམ ཨོཾ ༀ ཨོར", "decomposed oM")
testOrder("ཀར་ལུགས། ཀརྐ་ཊ།", "TDC p. 9")
testOrder("ཀརྨ་ ཀརྵ་ ཀལྤ་ ཀསྨིར་", "TDC p. 11")
testOrder("གངས་ལྷགས། གཉྫིར། གད།", "TDC p. 347")
testOrder("ཐར་ས། ཐརྐ།", "TDC p. 1153")
testOrder("པུས་ལྷང་ པུསྟིཀཿ་", "TDC p. 1619")
testOrder("ཕལ་མོ་ ཕལྒུ་ཎ་ ཕས་", "TDC p. 1711")
testOrder("བིལ་བ་ བིལྦ་", "TDC p. 1827")
testOrder("མང་ མཉྫ མད་", "TDC p. 2055")
testOrder("མར མརྒཏ་ མལ་", "TDC p. 2061")
testOrder("ཝརྟུ ཝར་ཏི་", "TDC p. 2367")
testOrder("ཤས་ ཤསྟཾ་ ཤི་", "TDC p. 2840")
testOrder("སར་ སརྒཿ་ སལ་", "TDC p. 2920")
testOrder("ཨར་ ཨརྒྷཾ་ ཨརྱ་", "TDC p. 3136")
testOrder("ཨལ་ ཨསྨ་ ཨཱརྱ་", "TDC p. 3137")
testOrder("བུད་དྷ། བུདྡྷཿ། བུདྡྷ་པཱ་ལ། བུདྡྷ་པཱ་ལི་ཏ། བུདྡྷ་ཤྲཱིཤནྟི། བུད་པ།", "TDC p. 1833")
testOrder("སིངས་པོ། སིངྒྷལ། སིད།", "TDC p. 2922")
testOrder("སེང་གེ་ཁ་འབབ་གངས་རི། སེངྒེ་ཁྱིམ། སེང་གེ་རྒྱན་གཞི།", "TDC p. 2934")
testOrder("ཛམ་ཐང་གཙང་པ་དགོན། ཛམྦུ་ཀ། ཛམྦུ་གླིང༌། ཛམྦུ་ཆུ་བོ། ཛམྦུ་ཆུ་གསེར། ཛམྦུ་པྲྀཀྵ། ཛམ་བྷ་ལ།", "TDC p. 2332")
testOrder("པར་པ་ཏ། པརྤ་ཏ། པར་པར།", "TDC p. 1615")
testOrder("བཻ་དཀར་གཡའ་སེལ། བཻཌཱུརྻ། བཻཌཱུརྻ་དཀར་པོ། བཻཌཱུརྻ་སྔོན་པོ། བཻཌཱུརྻ་སེར་པོ། བཻཌཱུརྻའི་མདོག་ཅན། བཻ་རོ་ཙ་ན། བཻཤྲ་བཎཿ། བེག་གེ།", "TDC p. 1839,1840")
testOrder("ག དགག དགང དག༵ང དག༷ང དགད དགས དགི དགི༵ དགི༷ དགི༵ དགི༷ དགུ བགྱ བགྲ བགྲ༵ བགྲ༷ བགྲུ བགྲུ༵ བགྲུ༷ བགླ", "ignored marks (mark-vowel and vowel-mark)")
# Test page 55 of Manuel de Tibétain Standard by Nicolas Tournadre
testOrder("ག་རེ་ གངས་ གི་ གིས་ གུར་ གེ་སར་ གོ་ གྭ་ གྱང་ གྱུར་ གྲང་མོ་ གྲངས་ གླ་ གླང་ དགའ་ དགུ་ དགེ་བ་ དགོས་ དགྲ་ བགམས་ བགེགས་ མགུར་ མགྱོགས་ རྒན་ རྒོད་པོ་ རྒྱ་ རྒྱ་མ་ ལྒང་བུ་ སྒ་ སྒུག་ སྒོར་མོ་ སྒྱུར་ སྒྲ་ བརྒལ་ བརྒྱ་ བསྒོམས་ བསྒྱུར་ བསྒྲགས་ བསྒྲིགས་", "NT")
testOrder("ཀ་ཀ་ ཀ་ཀ་ནཱི་ལ ཀ་ཀ་ཎི་ལ་ ཀ་ཀ་མུ་ཁ་ ཀ་གཉིས་པ་ ཀ་ཊོ་ར་ ཀ་ཏ་པུར་", "vowel-retroflex priority (Illuminator)")
# Tests from https://github.com/suizokukan/dchars/tree/master/tests/languages/bod
testOrder("ཀ་རྐ་ཏ་ ཀ་སྐྱོར་ ཀ་ཁ་ ཀ་ཁ་པ་ ཀ་ཁའི་རིམ་པ་ ཀ་ཁོལ་མ་ ཀ་འགོ་ ཀ་རྒྱན་ ཀ་རྒྱུག་ ཀ་སྒྲོགས་ ཀ་ཅ་ ཀ་ཅི་ ཀ་ཅོག་ཞང་གསུམ་ ཀ་ཆ་ ཀ་ཆུག་ ཀ་ཆེན་བཅུ་ ཀ་ཆེན་བཞི་ ཀ་གཉིས་པ་ ཀ་ཏ་པུར་ ཀ་ཏ་པུར་འཛག་ ཀ་ཏ་བུ་ར་ ཀ་ཏ་ཡ་ན་ ཀ་ཏ་རུ་ ཀ་ཏན་ ཀ་ཏའི་བུ་ནོག་ཅན་ ཀ་ཏའི་བུ་མོ་ ཀ་ཏི་ ཀ་ཏི་ཤེལ་གྱི་སྦུ་གུ་ཅན་ ཀ་ཏི་ཤེལ་གྱི་རྩ་ ཀ་ཏི་གསེར་གྱི་རྩ་ ཀ་ཏི་གསེར་གྱི་རྩ་ཆེན་ ཀ་ཏུ་ ཀ་ཏོ་ར་ ཀ་ཏྱ་བུ་མོ ཀ་ཏྱ་ཡ་ན ཀ་ཏྱཱ་ཡ་ན ཀ་ཏྱཱ་ཡ་ན་ཆེན་པོ ཀ་ཏྱཱ་ཡ་ན་ནོག་ཅན ཀ་ཏྱཱའི་བུ ཀ་ཏྱཱའི་བུ་ཆེན་པོ ཀ་ཏྱཱའི་བུ་ནོག་ཅན ཀ་ཏྱཱའི་བུ་མོ ཀ་རྟི་ཀ་ ཀ་སྟེགས་ དཀ བཀ རྐ ལྐ སྐ བརྐ བསྐ ཁ མཁ འཁ ག གད གན གས རྒ ལྒ སྒ བརྒ བསྒ ང རྔ ལྔ སྔ བརྔ བསྔ ཅ གཅ བཅ ལྕ བལྕ ཆ མཆ འཆ ཇ མཇ འཇ རྗ ལྗ བརྗ ཉ གཉ མཉ རྙ སྙ བརྙ བསྙ ཏ གཏ བཏ རྟ ལྟ སྟ བརྟ བལྟ བསྟ ཐ མཐ འཐ ད དག དང དབ དམ རྡ ལྡ སྡ བརྡ བལྡ བསྡ ན རྣ སྣ བརྣ བསྣ པ ལྤ སྤ ཕ འཕ བ བག བད བར བས རྦ ལྦ སྦ མ མག མང མད མན རྨ སྨ ཙ གཙ བཙ རྩ སྩ བརྩ བསྩ ཚ མཚ འཚ ཛ མཛ འཛ རྫ བརྫ ཝ ཞ གཞ བཞ ཟ གཟ བཟ འ འག འད འབ ཡ གཡ ར བརླ ལ ཤ གཤ བཤ ས ཧ ལྷ ཨ", "dchars (Illuminator)")
testOrder("ཁ གད་ གན་ གར་ གལ་ གས་ ང ད དག་ དང་ དབ་ དམ་ དར་ དལ་ དས་ ན ཕ བག བད་ བར་ བལ་ བས་ མ མག་ མང མད་ མན མབ་ མར་ མལ་ མས་ ཙ འག འད འབ", "2 letters")
testOrder("ད དངས ན ཕ བགས མ མགས མངས ཙ", "3 letters ambiguous with first letter as main letter")
testOrder("ཁ དགས འགས ང ད གདས བདས འདས ན ཕ དབས འབས མ དམས ཙ", "3 letters ambiguous with second letter as main letter")
testOrder("ག དགག དགང དགད དགན དགབ དགཝ དགའ དགར དགལ དགས བགག བགང བགད བགབ བགམ བགཾ བགཝ བགའ བགར བགལ མགག མགང མགད མགབ མགའ མགར མགལ འགག འགང འགད འགན འགབ འགམ འགཾ འགའ འགར འགལ འགས དངག དངང དངད དངན དངབ དངའ དངར དངལ མངག མངང མངད མངན མངབ མངའ མངར མངལ གདག གདང གདད གདན གདབ གདམ གདཾ གདའ གདར གདལ གདས བདང བདད བདབ བདམ བདཾ བདའ བདར བདལ བདས མདག མདང མདད མདན མདབ མདའ མདར མདལ མདས འདག འདང འདད འདན འདབ འདམ འདཾ འདའ འདར འདལ འདས གནག གནང གནད གནན གནབ གནམ གནཾ གནའ གནར གནལ གནས མནག མནང མནད མནན མནབ མནམ མནཾ མནའ མནར མནལ མནས དཔག དཔང དཔད དཔབ དཔའ དཔར དཔལ དཔས དབག དབང དབད དབན དབབ དབའ དབར དབལ དབས འབག འབང འབད འབན འབབ འབམ འབཾ འབའ འབར འབལ འབས དམག དམང དམད དམན དམབ དམཝ དམའ དམར དམལ དམས གསག གསང གསད གསན གསབ གསའ གསར གསལ གསས བསག བསང བསད བསབ བསམ བསཾ བསའ བསར བསལ བསས", "3 letters")
testOrder("ཁ དགི དགུ དགེ དགོ བགི བགུ བགེ བགོ མགི མགུ མགེ མགོ འགི འགུ འགེ འགོ ང དངི དངུ དངེ དངོ མངི མངུ མངེ མངོ ཅ ད གདི གདུ གདེ གདོ བདི བདུ བདེ བདོ མདི མདུ མདེ མདོ འདི འདུ འདེ འདོ ན གནི གནུ གནེ གནོ མནི མནུ མནེ མནོ དཔི དཔུ དཔེ དཔོ ཕ དབི དབུ དབེ དབོ འབི འབུ འབེ འབོ མ དམི དམུ དམེ དམོ ས གསི གསུ གསེ གསོ བསི བསུ བསེ བསོ ཧ", "2 letters ambiguous with vowels")
testOrder("ཁ དགྭ བགྭ མགྭ འགྭ ང དངྭ མངྭ ཅ ད གདྭ བདྭ མདྭ འདྭ ན ཕ དབྭ འབྭ མ དམྭ ས གསྭ བསྭ ཧ", "2 letters ambiguous with wasur")
testOrder("ད་ དམ་ ད͏མས་ གདའ་ མ་ དམར་ དམས་ དམི་", "non-standard disambiguation with CGJ")
testOrder("ང་ མངར་ མང⁠ས་ མངི་ མ་ མང་ མངས་ མད་", "non-standard disambiguation with WJ")

exit(EXIT_CODE)
