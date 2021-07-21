"""
Purpose
Shows how to implement an AWS Lambda function that handles input from direct
invocation.
"""

import logging
import math
import requests

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Define a list of Python lambda functions that are called by this AWS Lambda function.
ACTIONS = {
    'square': lambda x: x * x,
    'square root': lambda x: math.sqrt(x),
    'increment': lambda x: x + 1,
    'decrement': lambda x: x - 1,
}


def lambda_handler():
    """
    Accepts an action and a number, performs the specified action on the number,
    and returns the result.
    :param event: The event dict that contains the parameters sent when the function
                  is invoked.
    :param context: The context in which the function is called.
    :return: The result of the specified action.
    """
    # logger.info('Event: %s', event)

    r = requests.get('https://api.coingecko.com/api/v3/coins/list?include_platform=true', auth=('user', 'pass'))

    # result = ACTIONS[event['action']](event['number'])
    # logger.info('Calculated result of %s', result)

    # response = {'result': result}
    return r

print('hello')

response = lambda_handler()
print(response.json())
print(response.headers)

# curl -X 'GET' \
#   -o file.txt \
#   'https://api.coingecko.com/api/v3/coins/list?include_platform=true' \
#   -H 'accept: application/json'