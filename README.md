SublimeLinter-contrib-qmllint
================================

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [qmllint](https://code.qt.io/cgit/qt/qtdeclarative.git/tree/tools/qmllint). It will be used with files that have the "QML" syntax.

## Installation
SublimeLinter must be installed in order to use this plugin.

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before installing this plugin, you must ensure that `qmllint` is installed on your system. `qmllint` comes pre-packaged with Qt which could be installed with your Package Manager of choice (Homebrew, Yum, APT, e.t.c) or directly from [Qt.io](https://www.qt.io/download).

In order for `qmllint` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

## Settings
- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
