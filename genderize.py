# Given an array of given names, determine what percent are male vs. female.
# Instructions for getting a csv file of all your LinkedIn contacts:
# Export LinkedIn connections (https://www.linkedin.com/people/export-settings)
# Import the file into a Google Sheet
# Delete everything but the first name field ("Given Name")
# Export the sheet as a csv, named mycontacts.csv
#
# If you're on a Mac, you may need to change the formatting slightly:
# cat mycontacts.csv | col -b > mycontacts.tmp
# mv mycontacts.tmp mycontacts.csv
#
# NB the genderize API allows 1000 free queries per day; if your list is over
# 1000 names, you can either split it into lists of 1000 and run them over a
# few days, or you can upgrade to a paid account.

import requests
import json

female = 0
male = 0
cant_tell = 0
undetermined_names = []

# if the name is multi-word, just use the first word. This should
# handle people who put their former surname or middle initial in
# the "first name" field.
f = open('mycontacts.csv', 'r')

for name in f:
  request_string = "http://api.genderize.io/?name=" + name.split(' ', 1)[0].strip()
  r = requests.get(request_string)
  result = json.loads(r.content)
  if result['gender'] == 'female':
    female = female + 1
  elif result['gender'] == 'male':
    male = male + 1
  else:
    cant_tell = cant_tell + 1
    undetermined_names.append(name)

ratio = float(female)/(female + male)
print "Female: " + str(female)
print "Male: " + str(male)
print "Percent female " + '{:.1%}'.format(ratio)
print "Undetermined: " + str(cant_tell)
print undetermined_names
