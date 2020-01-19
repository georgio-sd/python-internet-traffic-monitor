#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##############################################################################
# Delete old backup files and database records (run once a week)
##############################################################################
#
from datetime import datetime, timedelta
dt_past = datetime.now() - timedelta(183)
date_str = dt_past.strftime("%Y-%m-%d")

import mysql.connector
from mysql.connector import errorcode
try:
    cnx = mysql.connector.connect(user='traff', password='*****',
                                  host='localhost', database='traff')
except mysql.connector.Error as err:
    import sys
    sys.exit(err)

cursor = cnx.cursor(buffered=True)
cursor.execute("delete from traff where date<'" + date_str + "';")
cursor.execute("optimize table traff;")
cnx.commit()
cursor.close()
cnx.close()

import os
import re

for root, dirs, files in os.walk("/usr/local/mybilling/backup"):
    for filename in files:
        result = re.search('[0-9\-]{10}', filename)
        if result.group(0) < date_str:
             os.remove("/usr/local/mybilling/backup/" + filename)
