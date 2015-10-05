# Given an array of given names, determine what percent are male vs. female.
# NB the genderize API allows 1000 free queries per day; if your list is over
# 1000 names, you can either split it into lists of 1000 and run them over a
# few days, or you can upgrade to a paid account.
# Instructions for getting a csv file of all your LinkedIn contacts are
# found here: http://tins.rklau.com/2015/10/using-genderizeio-to-infer-gender-in.html
# Once you have the csv, to transform it into a file that you can copy-paste into
# the 'names' array here, try the following (first step might only be needed on OS X
# to handle the different newline formats between Windows and Mac)):
# cat mycontacts.csv | col -b > mycontacts.tmp
# cat mycontacts.tmp | sed 's/^/"/;s/$/,"/' > mycontacts.out
#
# mycontacts.out can now be pasted into the "names" array below. You should remove the
# extra comma on the last item.

import requests
import json

names = [
'John',
'Jane',
'Mumble',
'Susan L K',
'Hillary Rodham'
];

female = 0
male = 0
cant_tell = 0
undetermined_names = []

# if the name is multi-word, just use the first word. This should
# handle people who put their former surname or middle initial in
# the "first name" field.

for name in names:
  print name
  request_string = "http://api.genderize.io/?name=" + name.split(' ', 1)[0]
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
