# virtual environment (venv)

virtual environment is an isolated environment that lets you install packages separately for each project which results in avoiding version conflicts between projects.

1. Create a virtual environment
--> run the below in terminal 
python -m venv venv_name

--> this will create a folder (venv_name) containing its own Python interpreter and site-packages.

2. Activate the virtual environment

--> On Windows (Command Prompt or PowerShell):
venv_name\Scripts\activate

--> On Bash:
source venv_name/bin/activate

--> Once activated, you’ll see folder name (venv_name) in your terminal prompt.

3. Install packages inside it
pip install <requests>

4. Deactivate when done
--> run below in terminal 
deactivate

