#!/bin/bash
# exit immediately if a command exits with a nonzero exit status.
set -e
# treat unset variables as an error when substituting.
set -u

py.test -x
touch temp.db && rm temp.db
django-admin.py migrate --noinput
django-admin.py demo_data_login
django-admin.py demo_data_enquiry
django-admin.py runserver
