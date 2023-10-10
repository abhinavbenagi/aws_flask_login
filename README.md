# Flask Development Environment Setup



## FLASK Installation

1) Create flask environment:

```bash
python3 -m venv myapp
```
2) Activate the Environment
```bash
myapp\Scripts\activate
```
3) Install Flask
```bash
pip install Flask
```
4) Test the Development Environment

```bash
vi application.py
```
```python
from flask import Flask
application = Flask(__name__)
@application.route('/')
def hello_world():
    return 'Hello world!'

if __name__=="__main__":
    application.run(debug=True)
```



## Git commands:
```bash
git init 
```
```bash
create .gitignore file
```
```bash
git status
```
```bash
git add .
```
```bash
git commit -m "first commit"
```
```bash
git remote add origin https://github.com/abhinavbenagi/aws_flask_login.git
```
```bash
git branch -M main
```
```bash
git push -u origin main
```
## If you make any changes:
```bash
git add .
git commit -m "first commit"
git push origin head

```



## Contributing
