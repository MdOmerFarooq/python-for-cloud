from dotenv import load_dotenv
import os
import sys

load_dotenv()

input_username = 'mdomer'
input_password = sys.argv[1]

if input_password == os.getenv('saved_password'):
    print(f'Welcome {input_username}')
else :
    print(f"wrong password try again :( ")

