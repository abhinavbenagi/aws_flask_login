1) Create flask environment:
python3 -m venv <name of environment>

2) Activate the Environment
<name of environment>\Scripts\activate

3) Install Flask
pip install Flask

4) Test the Development Environment
vi application.py

from flask import Flask
application = Flask(__name__)
@application.route('/')
def hello_world():
    return 'Hello world!'

if __name__=="__main__":
    application.run(debug=True)


Git commands:

git init 

create .gitignore file

git status

git add .
git commit -m "first commit"

git remote add origin https://github.com/abhinavbenagi/aws_flask_login.git
git branch -M main
git push -u origin main

If you make any changes in code:

git add .
git commit -m "first commit"
git push origin head



