"""
SublimeLinter Plugin for QML/JS.

Written by Temi Adeoye
Copyright (c) 2019
License: MIT
"""

from SublimeLinter.lint import Linter, util


class QMLLint(Linter):
    """Provides an interface to qmllint binary."""

    cmd = 'qmllint $temp_file'
    regex = r'^(?P<filename>.+):(?P<line>\d+) : (?P<message>.+)$'
    multiline = True
    error_stream = util.STREAM_STDERR
    tempfile_suffix = 'qml'
    defaults = {
        'selector': 'source.qml',
    }
