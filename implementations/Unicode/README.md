# Unicode implementation of simple Tibetan collation

The main file is [rules.txt](rules.txt), it is meant to be used with the [Unicode Collation Algorithm](http://unicode.org/reports/tr10/) (UCA). See [ICU doc](http://userguide.icu-project.org/collation/customization) and [Unicode doc](http://www.unicode.org/reports/tr35/tr35-collation.html#Orderings) for rule file format.

# Installation

The most simple implementation should be provided with recent OSs through [CLDR](http://cldr.unicode.org/), so if you just want simple Tibetan collation, you do not need files from this repository.

If you want to use the rules.txt file directly, the easiest way to use them is to install Python 3 and [PyICU](http://pyicu.osafoundation.org/).

If you have ICU52, you must use the `rules-icu52.txt` file, due to some changes in the collation algorithm implementation (see [icu bug #12834](http://bugs.icu-project.org/trac/ticket/12834))

# Tests

To run the tests, simply run `./test.py`.

# Changes

See [CHANGELOG.md](CHANGELOG.md).

# Ticket links

- [CLDR #8506](http://unicode.org/cldr/trac/ticket/8506) (link seems dead)
- [CLDR #9895](http://unicode.org/cldr/trac/ticket/9895)
- [ICU #13224](http://bugs.icu-project.org/trac/ticket/13224)
