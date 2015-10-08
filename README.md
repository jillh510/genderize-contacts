# genderize-contacts
Figure out gender ratio from an array of given names

NB the genderize API allows 1000 free queries per day; if your list is over
1000 names, you can either split it into lists of 1000 and run them over a
few days, or you can upgrade to a paid account.

Instructions for getting a csv file of all your LinkedIn contacts are
found here: http://tins.rklau.com/2015/10/using-genderizeio-to-infer-gender-in.html.
Once you have the csv, to transform it into a file that you can copy-paste into
the 'names' array here, try the following (first step might only be needed on OS X
to handle the different newline formats between Windows and Mac):

cat mycontacts.csv | col -b > mycontacts.tmp

cat mycontacts.tmp | sed 's/^/"/;s/$/,"/' > mycontacts.out

mycontacts.out can now be pasted into the "names" array in genderize.py. You should remove the
extra comma on the last item.
