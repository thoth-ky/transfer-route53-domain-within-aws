
def accept_domain(client, domain, password):
  '''
  returns
  {
    'OperationId': 'string',
  }
  '''

  return client.accept_domain_transfer_from_another_aws_account(
    DomainName=domain,
    Password=password
  )