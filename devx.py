import sys
import os
import argparse
import random
import string

import hashlib
from hashlib import sha1

# pip install requests
import requests

msg = hashlib.sha256();
msg.update(b'Simple is better than complex');
msg.digest();

msg.block_size;

msg.hexdigest();

msg = hashlib.md5();
msg.update(b'Simple is better than complex');
msg.hexdigest();

print(msg.digest_size)
print(msg.hexdigest())
print("done")
