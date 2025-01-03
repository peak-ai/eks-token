from datetime import datetime, timedelta
from botocore import session
from awscli.customizations.eks.get_token import STSClientFactory, TokenGenerator, TOKEN_EXPIRATION_MINS

work_session = session.get_session()
client_factory = STSClientFactory(work_session)

def get_expiration_time():
        token_expiration = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRATION_MINS)
        return token_expiration.strftime('%Y-%m-%dT%H:%M:%SZ')
    
def get_token(cluster_name: str, role_arn: str = None, region_name: str = None) -> dict:
    sts_client = client_factory.get_sts_client(role_arn=role_arn, region_name=region_name)
    token = TokenGenerator(sts_client).get_token(cluster_name)
    return {
            "kind": "ExecCredential",
            "apiVersion": "client.authentication.k8s.io/v1beta1",
            "spec": {},
            "status": {
                "expirationTimestamp": get_expiration_time(),
                "token": token
            }
        }
