#!/usr/bin/env python3
#
#

import sys
import logging
import random
import os
from sdcclient import SdMonitorClient

JOB_NAME = os.getenv('JOB_NAME')
NODE_NAME = os.getenv('NODE_NAME')
NAMESPACE = os.getenv('NAMESPACE')

SYSDIG_API_TOKEN = os.getenv('SYSDIG_MONITOR_API_TOKEN')
SYSDIG_API_URL = os.getenv('SYSDIG_MONITOR_API_URL')


class ValueTooSmallError(Exception):
  def __init__(self, number, message="Number is too small."):
      self.number = number
      self.message = message
      super().__init__(self.message)
  
  def __str__(self) -> str:
      return self.message


def post_sysdig_event(sysdig_token, sysdig_url, event_message):
    
    try:
     sdclient = SdMonitorClient(token=sysdig_token, sdc_url=sysdig_url)
     event_name = f'Kubernetes Job - {JOB_NAME} - failed'
     scope = f'kubernetes.job.name = \"{JOB_NAME}\" and kubernetes.namespace.name = \"{NAMESPACE}\"'
     logger.info(f'Sysdig Event Filter: {scope}')
     description = f'{event_message}'
     logger.info(f'Event Description: {description}')
     resp = sdclient.post_event(event_name, description=event_message, severity="medium", event_filter=scope, tags=None)
     logger.info(f"Sysdig Event Posted: {resp[0]}")
     logger.info(f"Event Payload: {resp[1]['event']}")
     return resp
    except Exception as err:
        logging.info(f'Unexpected Error: {err}')
        raise 



logger = logging.getLogger('log_to_console')
logger.setLevel(logging.DEBUG)
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
logger.addHandler(console)

try:
  random_int = random.randint(0,10)
  logger.info(f'Random Number is: {random_int}')
  if random_int <= 5:
    job_result = False
    raise ValueTooSmallError(random_int)
except ValueTooSmallError as err:
    event = f'{err.number} -> {err.message}'
    logger.info(event)
    response = post_sysdig_event(SYSDIG_API_TOKEN, SYSDIG_API_URL, event)
else:
    job_result = True
    logger.info(f'Random int is {random_int} and is greater than 5.')
finally:
  if job_result == True:
    exit_code = 0
    logger.info(f"Job {JOB_NAME} completed successfully.")
  else:
    exit_code = 1
    logger.info(f"Job {JOB_NAME} failed.")
  
sys.exit(exit_code)
     