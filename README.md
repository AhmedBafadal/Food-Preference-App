# MyPicks.com

## Description

App developed using Django that enables users to share their favorite food items with friends online.

The 'MyPicks' app allows allows each user to create a personalised menu item (with ingredients to either include or exclude) related to specific restaurants that they have posted.
Each user has access to their own menu feed upon registration and successful log in, whereby they can view the most recent posts of other users they have followed.
Depending on the preference of the user, any posts published may be set to be private or in public where it may be visible in their followers feeds.

## Implementation

Once registered, please refer to the terminal/console for an HTML message with the activation link and copy the generated activation key in order to login successfully (e.g. localhost:8000/activate/tzwnt1ou8twdgoxkwvcd0efxj9177u2cqas/).

## Installation

```
pip install dj-database-url==0.4.2
pip install Django==1.11.2
pip install django-crispy-forms==1.6.1
pip install gunicorn==19.7.1
pip install psycopg2==2.7.1
pip install pytz==2017.2
pip install olefile==0.44
pip install Pillow==4.1.1


python manage.py migrate
python manage.py runserver
```
