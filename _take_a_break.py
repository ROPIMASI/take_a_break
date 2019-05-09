a"""
# CONTENT: UDACITY UD036 PYTHON PROGRAMMING FUNDAMENTALS, MINI-PPROJECT-1.
# THEME: BREAK TIME AT COMPUTER WORK.
# PROJECT NAME / FILE: take_a_break.py .
# VERSION: 0.2 .
# AUTHOR: RONALDO PI MA SI.
# DATE: 2019-MAY.
# LANGUAGE: PYTHON.
# VERSION: 3.
# PLATAFORM: Microsoft Windows7, PYTHON 3.7 INTERPRETER, VISUAL STUDIO CODE.

# IMPORTANT NOTE / DISCLAIMER:
# This is a project made exclusively for study purposes. Nobody has obliga-
# tions, either responsibility on it or its effects. There is no guarantee
# it will work correctly.

# This is free and unencumbered software released into the public domain.
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
# For more information, please refer to <http://unlicense.org>
"""



# coding: utf-8
# Beginning with imports.
# import os
import sys
import time as t
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
import webbrowser as wb



def has_invalid_args(arg_list, valid_list):
    """Verify if 'arg_list' is a whole valid arguments list.

    User passes a list of arguments along with the command line in the shell.
    Developer tests whether those aguments are all valid using this function.
    For that, 'arg_list' will be compared to the 'valid_list'.

    Arguments:
        arg_list {string list}, required, ;
        valid_list {string list}, required, ;

    Attributes-Vars: None.
    Sub-Functions-Methods: None.
    Returns: {string list}, can has len()=0 or greater, representing only
        elements which are not in 'valid_list'.
    Raises: N/A.
    """
    return [elemt for elemt in arg_list if (elemt not in valid_list)]



def main(qty=1, uom='h', url=''):
    """Waits for user-specified time and opens browser with URL specified by user.

    The user defines how long must be the interval of concentration, and the URL
    which prefers for a happy break as a short rest.

    Arguments:
        qty {int} positive, optional, default=1, expresses how long will be
            waiting;
        uom {string} a single letter, optional, default='h' representing the
            unit of measurement will be used:
            's' {seconds};
            'm' {minutes};
            'h' {hour};
            'l' {list} lists all break-time already started on O.S., if 'l'
                other options above are ignored; #dev.note: Feature for a fu-
                ture version. note.dev#
            '?' {help} print, to standard output, the syntax and a short
                explanation, if '?' other options above are ignored;
        url {string} an address or object will be opened on web browser, IT
            MUST BE PASSED ALONG WITH 'URL:' TAG BEFORE THE ADDRESS, E.G:
            'url:www.vimeo.com' ;

    Attributes-Vars: None.
    Sub-Functions-Methods: None.
    Returns: None.
    Raises: N/A.
    """

    if uom=='s':
        uom=1
    if uom=='m':
        uom=60
    if uom=='h':
        uom=60*60

    while True:
        t.sleep(int(qty)*int(uom))
        wb.open(url)
    return



# t_a_b BEGIN

# t_a_b globals:
g_acceptable_args_v1 = ['h','m','s','?','l']

if (sys.argv[0]=='./take_a_break.py') or (sys.argv[0]=='./t_a_b') :
    #print(has_invalid_args(sys.argv[1:], g_acceptable_args_v1))
    #print(len(has_invalid_args(sys.argv[1:], g_acceptable_args_v1)))
    print(t.ctime())
    main(sys.argv[1], sys.argv[2], sys.argv[3])


### End.