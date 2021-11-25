#!/bin/bash

sleep 10

mongoimport --host my_mongo --db tutorial_db --collection cashback --type json --jsonArray --file /mongo-seed/CASHBACK.json
