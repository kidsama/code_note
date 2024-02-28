#!/bin/bash

#database="liu"
#table_name="l_tiku"

database="kcm_main"
table_name="area"

sqlacodegen --noviews  mysql+pymysql://root:lwx984502@127.0.0.1:3306/$database --table $table_name