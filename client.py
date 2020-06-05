import boto3

def get_aws_route53_client(ACCESS_KEY, SECRET_KEY, REGION_NAME):
  return boto3.client(
    'route53domains',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key= SECRET_KEY,
    region_name=REGION_NAME
  )