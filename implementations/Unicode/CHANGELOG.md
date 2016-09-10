# Change Log
All notable changes to the rule files will be documented in this file.
The version numbers are those of the [CLDR](http://cldr.unicode.org/). It follows [some conventions](http://keepachangelog.com/).

## [Unreleased] - 
### Fixed
 - ༀ (U+0F00) is now correctly sorted like its decomposition ཨོཾ (U+0F68 U+0F7C U+0F7E)
 - invalid syllables starting with a diacritic sign (U+0F71 - U+0FBC) are now after ཨ instead of between ལྷ and ཨ
 - དམས་ is now considered དམ+ས་ instead of the unattested ད+མས་
 - fix collation of following valid Classical Tibetan syllables (\* indicating also possible suffixes): གནབ་ གནར་ གནལ་ བགང་ དགི\*་ བགང་ བགབ་ བགལ་ བགི\*་ བགུ\*་ མགག་ མགང་ མགད་ མགབ་ མགའ་ མགི\*་ དངད་ དངབ་ དངའ་ དངལ་ དངི\*་ དངེ\*་ མངང་ མངད་ མངབ་ མངི\*་ མངུ\*་ མངེ\*་ གདད་ བདག་ བདང་ བདད་ བདབ་ བདི\*་ མདད་ མདབ་ མདལ་ མདས་ མདི\*་ གནབ་ གནར་ གནལ་ གནི\*་ གནེ\*་ མནད་ མནས་ མནི\*་ དཔི\*་ དཔོ\*་ དབི\*་ འབས་ དམད་ དམབ་ དམལ་ དམོ\*་ བསའ་ and བསས་
 - fix rule containing twice the same code (U+0F39)

### Added
 - U+0F62 = U+0F6A when followed with U+0F99 or U+0FB3 due to graphical equivalence
 - invalid vowel combinations: U+0F7B = U+0F7A U+0F7A and U+0F7D = U+0F7C U+0F7C
 - add theoretically possible but unattested དགྭ བགྭ མགྭ འགྭ གདྭ མདྭ འདྭ གནྭ མནྭ དམྭ and གསྭ
 - add U+0F6B (ཫ) after U+0F40 (ཀ) and U+0F6C (ཬ) after U+0F62 (ར)
 - add U+0F8B<<U+0F8C<<U+0F8D<<U+0F8E<<U+0F8F

### Changed
 - U+0F82 U+0F83 are classified with ང instead of མ
 - treat U+0F71 as a vowel mark


## CLDR29:
  - initial rules
