import xlsparser
import scrapper
import logging as logger
from os import rename
import os
import time
from dotenv import load_dotenv
print("test")
load_dotenv()
logger.basicConfig(format='%(levelname)s %(module)s %(message)s', level=logger.DEBUG)

# Change logging level for some verbose modules
for module in ['selenium.webdriver.remote.remote_connection', 'selenium', 'urllib3.connectionpool']:
    logger.getLogger(module).setLevel(logger.INFO)
xlsx = scrapper.scrape_xlsx()

with open('new_edt.xlsx', 'wb') as file:
    file.write(xlsx)

UES = 'gs11, gs15, gs21, gs16'
calendar = xlsparser.make_ics(xlsx, UES)
name = 'alt'
with open(f'calendars/ssi-{name}.ics', 'w') as file:
    logger.info(f'Write on calendars/{name}.ics')
    file.write(calendar)
    time.sleep(1000)
