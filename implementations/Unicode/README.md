# Unicode implementation of simple Tibetan collation

The main file is [rules.txt](rules.txt), it is meant to be used with the [Unicode Collation Algorithm](http://unicode.org/reports/tr10/) (UCA). See [ICU doc](http://userguide.icu-project.org/collation/customization) and [Unicode doc](http://www.unicode.org/reports/tr35/tr35-collation.html#Orderings) for rule file format.

The file [rules-WJ.txt](rules-WJ.txt) is an experimental test using Word Joiner (U+2060) to allow alternative disambiguation of the ambiguous syllables, see [documentation](../../doc/sorting-ambiguous-syllable.md) for more details.

# Installation

The most simple implementation should be provided with recent OSs through [CLDR](http://cldr.unicode.org/), so if you just want simple Tibetan collation, you do not need files from this repository.

If you want to use the rules.txt file directly, the easiest way to use them is to install Python 3 and [PyICU](http://pyicu.osafoundation.org/).

# Tests

To run the tests, simply run `./test.py`.

# Changes

See [CHANGELOG.md](CHANGELOG.md).

# TODO

- test da drag, and da drag disambiguation
- decide more generic conventions for Sanskrit sorting
