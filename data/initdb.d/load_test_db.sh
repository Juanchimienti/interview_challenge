#!/bin/bash

cd /docker-entrypoint-initdb.d/test_db
mysql -u root -p"${MYSQL_ROOT_PASSWORD}" ${MYSQL_DATABASE} < employees.sql
