UW Python Winter 2013 Project
===============
Goals for the project:
* Use Django and MySQL to build a simple site the accepts data in a form and displays it
* Utilize Google API User Auth
* Deploy the project to AppEngine while using Google's Cloud MySQL 
* Build on the use the UserProfiles to better understand relational tables in Django. I really just wanted to simply
  create a form wher a user could edit their profile in a form and save it. Not a trivial task which I could not get to work.

Challenges:
* I ended up using a boilerplate Django 1.4 project that included some examples for setting up the Cloud MySQL
  Setting this up took some time getting OAuth to work, but worked flawlessly once I had everything in place.
* Once I got my project all set up GAE and created my MySQL cloud instance, things work quite well.
  Useful Instructions: http://howto.pui.ch/post/39245389801/tutorial-django-on-appengine-using-google-cloud-sql

  Syncing Django DB to Cloud MySQL Instance: SETTINGS_MODE='prod' python manage.py syncdb
  Syncing Project to AppEngine: appcfg.py --oauth2 update mysite

* Setting up the OneToOne and ManyToMany relationships between a user and a Program and Activity table. At this point I still
  do not have it working unfortunely.
* I spent many many hours on trying to find the best way to extend the User class for UserProfiles. For whatever reason, if I
  define the 'user' in a new UserProfile class model with a OneToOne instead of a ForeignKey, I cannot get the user manager to
  work properly. ie. userprofile_set.all(). I was also not able to get .get_profile() as was suggested in many posts I found.
  So I left it with using a ForeignKey and this seemed to get things working.
* I'm having terrible problems getting the forms.ModelForm module to work.

What does work.
* I got bootstrap working to make things look pretty
* I implemented the gaeauth module to get Google User Auth working while adding a new django User the first time they log in.
* The Django Admin is fully functional which took some time with mapping my MySQL tables. I had considered using the non-rel
  for deploying to GAE, but this would have prevent me from using the Admin module.
* The Profile page will show you only the name of the User, but I still need to figure out why I cannot bring UserProfile show
  userprofile attrs. I'm close but not quite there.


How to get this working locally:
http://pythoncentral.org/setting-up-the-python-environment-with-virtualenv/
easy_install pip
pip install virtualenv
pip install django

Install MySQL on OSX:
Grab a image file from www.mysql.com using the 64-bit dmg file and install.
http://www.mysql.com/downloads/mysql/

Once the two installs have been run you will need to manually start the server from a console or reboot your mac. 
http://dev.mysql.com/doc/refman/5.1/en/macosx-installation-pkg.html

Run the following commands
export DYLD_LIBRARY_PATH=/usr/local/mysql/lib/
PATH=$PATH:/usr/local/mysql/bin

Next step was to install the python mysqldb module within a virtualenv python instance using 

pip install MySQL-python

You can test that mysql is working from a console 

Mysql –u root –p

The password should be a blank password so just hit enter when prompted for a password

Type this to see the databases available:
Show databases;
(semicolon needed at the end of each command)


Download Install Google Appengine Python SDK 1.7.5+
Run the following:

export GAE="/usr/local/google_appengine"
export PYTHONPATH="$PYTHONPATH:$GAE:$GAE/lib/django_1_4"
export PATH=${PATH}:$GAE/lib/django_1_4/django/bin/
export PATH=${PATH}:/usr/local/mysql/bin

Run locally:

    git clone git@github.com:conordean/uwpy-winter2013.git
    cd uwpy-winter2013
    ./serve.sh

Visit <http://localhost:8080>








