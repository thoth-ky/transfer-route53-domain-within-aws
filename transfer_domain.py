
def transfer_domain(client, domain, new_account_id):
  '''
  returns
  {
    'OperationId': 'string',
    'Password': 'string'
  }
  '''

  return client.transfer_domain_to_another_aws_account(
    DomainName=domain,
    AccountId=new_account_id
  )