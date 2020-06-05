from os import getenv

from client import get_aws_route53_client
from transfer_domain import transfer_domain
from accept_domain import accept_domain


AWS_ACCESS_KEY = getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY = getenv('AWS_SECRET_KEY')
REGION_NAME = getenv('REGION_NAME')
DOMAIN_NAME = getenv('DOMAIN_NAME')

RECEIVING_AWS_ACESS_KEY = getenv('RECEIVING_AWS_ACESS_KEY')
RECEIVING_AWS_SECRET_KEY = getenv('RECEIVING_AWS_SECRET_KEY')
RECEIVING_REGION_NAME= getenv('RECEIVING_REGION_NAME')
RECEIVING_ACCOUNT_ID = getenv('RECEIVING_ACCOUNT_ID')

transfer
client = get_aws_route53_client(
  AWS_ACCESS_KEY, AWS_SECRET_KEY, REGION_NAME,
)

response = transfer_domain(client=client, domain=DOMAIN_NAME, new_account_id=RECEIVING_ACCOUNT_ID)

print(f'Transfer results: {response}')
password = response["Password"]

# ACCEPT DOMAIN

receiving_client = get_aws_route53_client(
 RECEIVING_AWS_ACESS_KEY, RECEIVING_AWS_SECRET_KEY, RECEIVING_REGION_NAME
)

response = accept_domain(
  client=receiving_client,
  domain=DOMAIN_NAME,
  password=password
)


print(f'Accept Results: {response}')

print('RECEIVER DOMAINS LIST\n\n')

print(receiving_client.list_domains())