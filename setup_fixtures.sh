#!/bin/bash
for item in `find  | grep fixtures | grep json`
do
python manage.py loaddata $item
done
