# Unicode implementation of simple Tibetan collation

These files are meant to be used with the [Unicode Collation Algorithm](http://unicode.org/reports/tr10/) (UCA). See [ICU doc](http://userguide.icu-project.org/collation/customization) and [Unicode doc](http://www.unicode.org/reports/tr35/tr35-collation.html#Orderings) for rule file format.

# Installation

The most simple implementation should be provided with recent OSs through [CLDR](http://cldr.unicode.org/), so if you just want simple Tibetan collation, you do not need files from this repository.

If you want to use a custom, more complex one, the easiest way to use them is to install Python 3 and [PyICU](http://pyicu.osafoundation.org/).

# Tests

To run the tests, simply run `./test.py`.