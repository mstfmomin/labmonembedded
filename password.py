#!/usr/bin/env python

import cgi
import cgitb

cgitb.enable()

print "Content-type: text/html\n\n"

form=cgi.FieldStorage()

if "user_name" not in form:
    print "<h1>No username was entered</h1>"
else:
    text=form["user_name"].value
    print "<h1>Username:</h1>"
    print cgi.escape(text)

if "password" not in form:
    print "<h1>No password was entered</h1>"
else:
    text=form["password"].value
    print "<h1>Password:</h1>"
    print cgi.escape(text)
