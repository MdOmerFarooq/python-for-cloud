# Environment variables 

Environment variables are key–value pairs stored in OS that programs can read while running.

## Why Use Environment Variables?

- Keep **API keys and passwords secret** (not in our source code)
- Store **config values** like database URLs or usernames
- Make our project **work on any machine** without changing code

-->  to Set Environment Variables run :
on bash :
export MY_NAME="Omer"

On Windows :
(cmd)
set MY_NAME=Omer
(powershell)
$env:MY_NAME="Omer"

--> to use the created  Environment Variables in source code use :
1. we need to use the built-in os module
2. use os.getenv() function

ex :
import os

name = os.getenv("MY_NAME")
print("Hello", name)

## however this environment variables are temporary and only last until we close the terminal.

To avoid this we can use .env file to store all the  environment variables in our project .
1. for this we need to cerate a .env file in our project 
2. install the python-dotenv package using pip install python-dotenv
3. Declare the env variables in .env file ex : API_KEY=abc123
4. in our source code :

from dotenv import load_dotenv
import os

load_dotenv()
print(os.getenv("API_KEY"))

--> this way the source code is able to access the api key safely and without needing to type in terminal 