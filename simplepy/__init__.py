import psycopg2
import pytz
import gunicorn
import jsonschema
import Flask
import kafka-python

def joke():
    return (u'Wenn ist das Nunst\u00fcck git und Slotermeyer? Ja! ... '
            u'Beiherhund das Oder die Flipperwaldt gersput.')
