#!/bin/bash
if [ -e Ganison_dataset_1.csv] && [ -e Ganison_dataset_2.csv] && [ -e ganison_dataset_3.csv]&& [ -e ganison_dataset_4.csv]&& [ -e ganison_dataset_5.csv]
then
    python DataFromatting.py
    python manage.py loaddata area award class school student subject
else
    echo "Please copy datasets to the root folder"
fi


