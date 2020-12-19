# CheckYourScore

A tool to check your scores and notify you when they are updated on Hello IITK Platform

## How to Run

### First Time

#### Grab a cookie

Update the `username` and `password` fields with your IITK username and password and run `python3 getCookie.py`.

#### Store it for later

Paste the output of `python3 getCookie.py` in the `cook` field of `checkMarks.py`.

#### Enter your courses

Fill the `subjects` array in `checkMarks.py` with your courses.

Note: These entries need to be in lowercase, and appropriate suffix (a/b/nothing) must be attached based on how your course name appears on Hello IITK.

#### Let it rip

Run `python3 checkMarks.py > prevMarks.txt` to get your current marks.

### What's next?

Schedule `checkMarks.sh` to run every hour or so. It will send you a notification if your scores have changed.

Warning: Make sure you are not making requests too frequently, or you may get in trouble.
