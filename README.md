# eks-token
EKS Token package, an alternate to "aws eks get-token ..." CLI

## Usage

### Installation

```shell
pip install eks-token
```

### Basic usage

```python
from eks_token import get_token
from pprint import pprint

response = get_token(cluster_name='<value>')
pprint(response)
```
Expected Output
```json
{'apiVersion': 'client.authentication.k8s.io/v1alpha1',
 'kind': 'ExecCredential',
 'spec': {},
 'status': {'expirationTimestamp': '2020-10-01T15:05:17Z',
            'token': 'k8s-aws-v1.<token_value>'}}
```

### Extract token from response

```python
from eks_token import get_token

token = get_token(cluster_name='value')['status']['token']
print(token)
```

### Get Token signed for particular IAM role

Pass `role_arn`  argument to the function
```python
from eks_token import get_token

token = get_token(cluster_name='<value>', role_arn='<value>')['status']['token']
print(token)
```

## Contribution
Check our guidelines [here](CONTRIBUTING.md)