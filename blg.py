#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##############################################################################
# Save traffic counters into database (run every 15 minutes)
##############################################################################
#
from datetime import datetime
now = datetime.now()
date_time = now.strftime("%Y-%m-%d %H:%M:%S")

import mysql.connector
from mysql.connector import errorcode
try:
    cnx = mysql.connector.connect(user='traff', password='m*****',
                                  host='localhost', database='traff')
except mysql.connector.Error as err:
    import sys
    sys.exit(err)

from subprocess import call
call("/usr/local/mybilling/cnt_save", shell=True)

import re
in_cnt = open("/usr/local/mybilling/tmp/cnt_in", "r")
for s in in_cnt:
    if not re.match("^(C|Z|    pkts)", s):
        trf_in=int(s.split()[1])
in_cnt.close()

out_cnt = open("/usr/local/mybilling/tmp/cnt_out", "r")
for s in out_cnt:
    if not re.match("^(C|Z|    pkts)", s):
        trf_out=int(s.split()[1])
out_cnt.close()

if (trf_in+trf_out)>0:
    sql = "insert into traff values(%s, %s, %s)"
    val = (trf_in, trf_out, date_time)
    cursor = cnx.cursor()
    cursor.execute(sql, val)
    cnx.commit()
    cursor.close()
cnx.close()
