#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##############################################################################
# Backup traff database
##############################################################################
#

from datetime import datetime
now = datetime.now()
date = now.strftime("%Y-%m-%d")

from subprocess import call
call("mysqldump --opt -u traff -p***** traff | \
      gzip > /usr/local/mybilling/backup/traff.sql." + date + ".gz", shell=True)
