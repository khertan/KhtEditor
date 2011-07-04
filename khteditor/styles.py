#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2010 Benoît HERVIER
# Licenced under GPLv3

from PySide.QtGui import QColor, QTextCharFormat, QFont

def format(color, style=''):
    """Return a QTextCharFormat with the given attributes."""
    _color =  QColor()
    _color.setNamedColor(color)

    _format =  QTextCharFormat()
    _format.setForeground(_color)
    if 'bold' in style:
        _format.setFontWeight(QFont.Bold)
    if 'italic' in style:
        _format.setFontItalic(True)
    if 'underline' in style:
        _format.setFontUnderline(True)

    return _format


STYLES = {
            'default':{
                        'default': format('black'),
                        'background': format('white'),
                        'preprocessor': format('darkMagenta'),
                        'keyword': format('darkOrange'),
                        'datatype': format('darkMagenta'),
                        'special': format('darkMagenta'),
                        'operator': format('darkMagenta'),
                        'brace': format('darkGray'),
                        'number': format('blue'),
                        'defclass': format('blue'),
                        'string': format('green'),
                        'string2': format('green'),
                        'function': format('lightBlue'),
                        'comment': format('grey'),
                        'framework': format('blue'),
                        'mark1': format('darkOrange'),
                        'mark2': format('red'),
                        'linehighlight': format('#d5f5ff'),
                        'error': format('red', ('bold', 'underline'))},
            'dark':{
                        'default': format('lightgreen'),
                        'background': format('black'),
                        'preprocessor': format('#ff80ff'),
                        'keyword': format('yellow'),
                        'datatype': format('#60ff60'),
                        'special': format('orange'),
                        'operator': format('yellow'),
                        'brace': format('#858585'),
                        'number': format('#ffa0a0'),
                        'defclass': format('orange'),
                        'string': format('white'),
                        'string2': format('white'),
                        'function': format('#d5f5ff'),
                        'comment': format('#80a0ff'),
                        'framework': format('#d5f5ff'),
                        'mark1': format('darkOrange'),
                        'mark2': format('red'),
                        'linehighlight': format('darkblue'),
                        'error': format('red', ('bold', 'underline'))},
            'ninjaide':{
                        'default': format('black'),
                        'background': format('white'),
                        'preprocessor': format('darkMagenta'),
                        'keyword': format('darkMagenta'),
                        'datatype': format('darkMagenta'),
                        'special': format('orange'),
                        'operator': format('darkRed'),
                        'brace': format('#858585'),
                        'number': format('brown'),
                        'defclass': format('black'),
                        'string': format('green'),
                        'string2': format('darkGreen'),
                        'function': format('darkBlue'),
                        'comment': format('gray'),
                        'framework': format('blue'),
                        'mark1': format('darkOrange'),
                        'mark2': format('red'),
                        'linehighlight': format('#d5f5ff'),
                        'error': format('red', ('bold', 'underline'))}
            }
