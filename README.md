![Python application](https://github.com/NikGor/MySite/actions/workflows/python-app.yml/badge.svg)

# MySite Project 🌐
This is a personal website project built with Django. It serves as a portfolio to showcase my skills and projects. The website includes my personal information, a brief about me section, and contact details.

## Local Setup 🛠️
Clone the repository to your local machine:

```bash
git clone https://github.com/NikGor/MySite.git
```

Navigate to the project directory:

```bash
cd MySite
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Apply the migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Run the server:

```bash
python manage.py runserver
```
Now, you can navigate to http://localhost:8000 in your web browser to see the website.

# Deployment on Heroku ☁️
Create a new app on Heroku.

Install the Heroku CLI on your machine, and log in:

```bash
heroku login
```
Navigate to your project directory and initialize a new Git repository:

```bash
git init
```
Add the Heroku app as a remote:

```bash
heroku git:remote -a your-heroku-app-name
```
Add and commit your changes:

```bash
git add .
git commit -m "Initial commit"
```
Push the changes to Heroku:

```bash
git push heroku master
```
Run the migrations:

```bash
heroku run python manage.py migrate
```
Now, your website is live on Heroku!

# Contributing 🤝
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

# Show your support ⭐
Give a ⭐️ if you like this project!

# License 📝
This project is MIT licensed.

Enjoy using MySite! 🎉