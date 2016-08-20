# Source of collation articles

This directory contains the sources for some articles on Tibetan collation.

## Dependencies

The articles are made with [LuaTeX](http://luatex.org/), and use a few standard packages.

The directory contains a [git submodule](http://blogs.atlassian.com/2013/03/git-submodules-workflows-tips/) so you must run `git submodule update --init` the first time you want to use these files.

You need the [Linux Libertine](http://www.linuxlibertine.org/index.php?id=1&L=1), [Noto Sans Tibetan](https://www.google.com/get/noto/#sans-tibt) and [Noto Sans CJK](https://www.google.com/get/noto/help/cjk/) to compile the document.

You also need [perl](https://www.perl.org/) to transform the bibliography.

To install everything under Debian: 

```
sudo apt install fonts-noto fonts-noto-cjk perl git
```

## Compilation

Run `make` to compile the documents (Linux/MacOS only).