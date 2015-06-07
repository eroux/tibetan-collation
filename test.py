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
testOrder("ཨོམ ཨོཾ ༀ ཨོཙ", "decomposed oM")
# Test page 55 of Manuel de Tibétain Standard by Nicolas Tournadre
testOrder("ག་རེ་ གངས་ གི་ གིས་ གུར་ གེ་སར་ གོ་ གྭ་ གྱང་ གྱུར་ གྲང་མོ་ གྲངས་ གླ་ གླང་ དགའ་ དགུ་ དགེ་བ་ དགོས་ དགྲ་ བགམས་ བགེགས་ མགུར་ མགྱོགས་ རྒན་ རྒོད་པོ་ རྒྱ་ རྒྱ་མ་ ལྒང་བུ་ སྒ་ སྒུག་ སྒོར་མོ་ སྒྱུར་ སྒྲ་ བརྒལ་ བརྒྱ་ བསྒོམས་ བསྒྱུར་ བསྒྲགས་ བསིགྲགས་", "NT")
# Tests from https://github.com/suizokukan/dchars/tree/master/tests/languages/bod
testOrder("ཀ་ ཀ་ཀ་ ཀ་ཀ་ནྰི་ལ ཀ་ཀ་ཎི་ལ་ ཀ་ཀ་མུ་ཁ་ ཀ་ཀོ་ལ་ ཀ་ཀྰ་ ཀ་བཀྱག་ ཀ་རྐ་ཏ་ ཀ་སྐྱོར་ ཀ་ཁ་ ཀ་ཁ་པ་ ཀ་ཁའི་རིམ་པ་ ཀ་ཁོལ་མ་ ཀ་འགོ་ ཀ་རྒྱན་ ཀ་རྒྱུག་ ཀ་སྒྲོགས་ ཀ་ཅ་ ཀ་ཅི་ ཀ་ཅོག་ཞང་གསུམ་ ཀ་ཆ་ ཀ་ཆུག་ ཀ་ཆེན་བཅུ་ ཀ་ཆེན་བཞི་ ཀ་གཉིས་པ་ ཀ་ཏ་པུར་ ཀ་ཏ་པུར་འཛག་ ཀ་ཏ་བུ་ར་ ཀ་ཏ་ཡ་ན་ ཀ་ཏ་རུ ཀ་ཏའི་བུ་ནོག་ཅན་ ཀ་ཏའི་བུ་མོ་ ཀ་ཏན་ ཀ་ཏི་ ཀ་ཏི་ཤེལ་གྱི་སྦུ་གུ་ཅན་ ཀ་ཏི་ཤེལ་གྱི་རྩ་ ཀ་ཏི་གསེར་གྱི་རྩ་ ཀ་ཏི་གསེར་གྱི་རྩ་ཆེན་ ཀ་ཏུ་ ཀ་ཏོ་ར་ ཀ་ཏྱ་བུ་མོ ཀ་ཏྱ་ཡ་ན ཀ་ཏྱྰ་ཡ་ན ཀ་ཏྱྰ་ཡ་ན་ཆེན་པོ ཀ་ཏྱྰ་ཡ་ན་ནོག་ཅན ཀ་ཏྱྰའི་བུ ཀ་ཏྱྰའི་བུ་ཆེན་པོ ཀ་ཏྱྰའི་བུ་ནོག་ཅན ཀ་ཏྱྰའི་བུ་མོ ཀ་རྟི་ཀ་ ཀ་སྟེགས་ ཀ་ཊོ་ར་ དཀ བཀ རྐ ལྐ སྐ བརྐ བསྐ ཁ མཁ འཁ ག གད གན གས རྒ ལྒ སྒ བརྒ བསྒ ང རྔ ལྔ སྔ བརྔ བསྔ ཅ གཅ བཅ ལྕ བལྕ ཆ མཆ འཆ ཇ མཇ འཇ རྗ ལྗ བརྗ ཉ གཉ མཉ རྙ སྙ བརྙ བསྙ ཏ གཏ བཏ རྟ ལྟ སྟ བརྟ བལྟ བསྟ ཐ མཐ འཐ ད དག དང དབ དམ རྡ ལྡ སྡ བརྡ བལྡ བསྡ ན རྣ སྣ བརྣ བསྣ པ དཔ ལྤ སྤ ཕ འཕ བ བག བད བར བས རྦ ལྦ སྦ མ མག མང མད མན རྨ སྨ ཙ གཙ བཙ རྩ སྩ བརྩ བསྩ ཚ མཚ འཚ ཛ མཛ འཛ རྫ བརྫ ཝ ཞ གཞ བཞ ཟ གཟ བཟ འ འག འད འབ ཡ གཡ ར ལ བརླ ཤ གཤ བཤ ས ཧ ལྷ ཨ", "dchars")
testOrder("གད་ གན་ གར་ གལ་ གས་ དག་ དང་ དབ་ དམ་ དར་ དལ་ དས་ བག བད་ བར་ བལ་ བས་ མག་ མད་ མབ་ མར་ མལ་ མས་", "2 letters ambiguous")

exit(EXIT_CODE)
