# Overview

This is an Anime search website. This website allows a user to type in their Favorite Anime show and it will display it for them with a picture, rating and synopsis.
The Website is drawing from an API called Jinkan

The site also has a sign up form which is incomplet at the moment. However it collects the user information from an form and stores it into a database. This databese will be used in the future to allow user the access to do the search.

When the app is first launched the Sign up page will display, allowing the user to enter their credentials. There is a navigation bar on the right which links to the search page, on the search page there is a search bar which allows the user ot enter their anime of choice.

To start this app, a user must be the the project folder in their terminal. Whne in the terminal, run the command "python manage.py runserver" and a link will appear on the result, click or copy that link to a search bar, hit enter ans the page will load.

The purpose of writing this software was to gain and expereince with the Django framework and to build dynamic website.



[Software Demo Video](https://youtu.be/so7dC8Twsi4)

# Web Pages
The Home page - currentle has nothing, however in the future it should display an anime video and list of anime that you could search or do with the site

The search page - Allows the user to search for their anime of choice, it dynamically updates the page with every search.

The sign up page - It taks in users credentials and then stores them into a database. It uses a Form model which links the form dorectly to the databse.

# Development Environment

Json library- to convert the API passed to a json file and then searches the json file to look for the user search.

Django - Django creates an project in which you can create multiple apps, hoever this one just uses one app. Django also helps you to integrate html, css with Python

sqllite- it uses a sqllite database to store the user credentials, Django comes with this database as default, however you could change what database you perfer.

# Useful Websites


* [W3 School](https://www.w3schools.com/)
* [Django tutorial](https://www.djangoproject.com/)
* [youtube Django tutorial(Telusko)](https://www.youtube.com/watch?v=OTmQOjsl0eg&list=WL&index=113&t=8708s)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* Have a login and signup page which lets user use the search engine
* Have home page display an random anime video and list of anime searches
* Allow the user to view trailer videos( if available) from their search.