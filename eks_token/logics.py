import base64
import boto3
import re
from datetime import datetime, timedelta
from botocore.signers import RequestSigner

TOKEN_EXPIRATION_MINS = 15

def get_expiration_time():
    token_expiration = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRATION_MINS)
    return token_expiration.strftime('%Y-%m-%dT%H:%M:%SZ')

def get_bearer_token(cluster_id, region):
    STS_TOKEN_EXPIRES_IN = 60
    session = boto3.session.Session()

    client = session.client('sts', region_name=region)
    service_id = client.meta.service_model.service_id

    signer = RequestSigner(
        service_id,
        region,
        'sts',
        'v4',
        session.get_credentials(),
        session.events
    )

    params = {
        'method': 'GET',
        'url': f'https://sts.{region}.amazonaws.com/?Action=GetCallerIdentity&Version=2011-06-15',
        'body': {},
        'headers': {
            'x-k8s-aws-id': cluster_id
        },
        'context': {}
    }

    signed_url = signer.generate_presigned_url(
        params,
        region_name=region,
        expires_in=STS_TOKEN_EXPIRES_IN,
        operation_name=''
    )

    base64_url = base64.urlsafe_b64encode(signed_url.encode('utf-8')).decode('utf-8')

    # remove any base64 encoding padding:
    return 'k8s-aws-v1.' + re.sub(r'=*', '', base64_url)

def get_token(cluster_name: str, role_arn: str = None, region_name: str = None) -> dict:
    token = get_bearer_token(cluster_name, region_name)
    return {
        "kind": "ExecCredential",
        "apiVersion": "client.authentication.k8s.io/v1beta1",
        "spec": {},
        "status": {
            "expirationTimestamp": get_expiration_time(),
            "token": token
        }
    }
