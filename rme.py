import sys
import os
import argparse
import random
import string

from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
        
#        asdfdsf
# tcommi2


