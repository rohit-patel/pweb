===============================
portfolio
===============================

.. image:: https://badge.fury.io/py/portfolio.png
    :target: http://badge.fury.io/py/portfolio

.. image:: https://pypip.in/d/portfolio/badge.png
    :target: https://crate.io/packages/portfolio?version=latest


portfolio website

* Free software: BSD license

Requirements
------------

* Django 1.10+
* Python 2.7
* Django CMS 3.4+

.. _django-cms: https://github.com/divio/django-cms

Installation
----------------------------

#. Clone the git repository.
#. Create a production.py file in portfolio/portfolio/portfolio/settings by copying what's in the example_production.py
    * Fill database details in the file you just created
    * Add the site admins in the ADMINS variable
    * Add server host in ALLOWED_HOSTS

#. Install all third party packages by running::

    $ pip install -r requirements/development.txt

#. Apply migrations::

    $ python manage.py migrate

