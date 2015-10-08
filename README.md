# genderize-contacts
Figure out gender ratio from an array of given names


Instructions for getting a csv file of all your LinkedIn contacts:
Export LinkedIn connections (https://www.linkedin.com/people/export-settings)
Import the file into a Google Sheet
Delete everything but the first name field ("Given Name")
Export the sheet as a csv, named mycontacts.csv

If you're on a Mac, you may need to change the formatting slightly:

cat mycontacts.csv | col -b > mycontacts.tmp

mv mycontacts.tmp mycontacts.csv


NB the genderize API allows 1000 free queries per day; if your list is over
1000 names, you can either split it into lists of 1000 and run them over a
few days, or you can upgrade to a paid account.

