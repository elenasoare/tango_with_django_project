import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    # create lists of dictionaries containing the pages
    #we want to add in each category
    # then create a dictionary of dictionaries for each category
    # it allows to iterate through each data structure, and add the data to our models.


    python_pages = [
        {"title" : "Official Python Tutorial",
         "url" : "http://docs.python.org/2/tutorial/",
         "views": 100},
        {"title" : "How to think like a Computer Scientist",
         "url" : "http://www.greenteapress.com/thinkpython/",
         "views":20},
        {"title" : "Learn Python in 10 Minutes",
         "url":"http://www.korokithakis.net/tutorials/python/",
         "views":4} ]
    django_pages = [
        {"title":"Official Django Tutorial",
         "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/",
         "views":30},
        {"title":"Django Rocks",
         "url":"http://www.djangorocks.com/",
         "views":28},
        {"title":"Bottle",
         "url":"http://www.tangowithdjango.com/",
         "views":6} ]
    other_pages = [
        {"title":"Bottle",
          "url":"http://bottlepy.org/docs/dev/",
         "views":15},
        {"title":"Flask",
         "url":"http://flask.pocoo.org",
         "views":17} ]
    cats = { "Python": {"pages":python_pages,"views":128,"likes":64},
             "Django": {"pages":django_pages,"views":64,"likes":32},
             "Other Frameworks": {"pages": other_pages,"views":32,"likes":16}}

    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category.
    # if you are using Python 2.x then use cats.iteritems() see
    # http://docs.quantifiedcode.com/python-anti-patterns/readability/
    # for more information about how to iterate over a dictionary properly.

    for cat, cat_data in cats.items():
        c = add_cat(cat,cat_data["views"],cat_data["likes"])
        for p in cat_data["pages"]:
            add_page (c, p["title"], p["url"],p["views"])


    # print the categories we have added
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print ("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, url, views = 0):
    p = Page.objects.get_or_create(category=cat, title = title)[0]
    p.url = url
    p.views = views
    p.save()
    return p
def add_cat(name, views = 0, likes = 0):
    c = Category.objects.get_or_create(name = name)[0]
    c.likes = likes
    c.views = views
    c.save()
    return c

#start execution

if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
