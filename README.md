# eks-token
EKS Token package, an alternate to "aws eks get-token ..." CLI

![CodeQuality](https://github.com/peak-ai/eks-token/workflows/CodeQL/badge.svg) ![Publish](https://github.com/peak-ai/eks-token/workflows/Upload%20Python%20Package/badge.svg) ![stable](https://img.shields.io/github/v/release/peak-ai/eks-token) ![](https://img.shields.io/github/v/release/peak-ai/eks-token?include_prereleases) ![](https://img.shields.io/github/license/peak-ai/eks-token) ![](https://img.shields.io/github/languages/count/peak-ai/eks-token) ![](https://img.shields.io/github/languages/top/peak-ai/eks-token) ![](https://img.shields.io/github/issues-raw/peak-ai/eks-token) ![](https://img.shields.io/github/issues-pr-raw/peak-ai/eks-token) ![](https://img.shields.io/github/languages/code-size/peak-ai/eks-token) ![](https://img.shields.io/github/repo-size/peak-ai/eks-token)

![logo](https://raw.githubusercontent.com/peak-ai/eks-token/main/eks-iam.png)

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
```python
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

### Custom region

```python
from eks_token import get_token

cluster_name = "your-cluster-name"
role_arn = "your-role-arn"
region_name = "your-region-name"

token = get_token(cluster_name, role_arn=role_arn, region_name=region_name)
print(token)
```

## Contribution
Check our guidelines [here](CONTRIBUTING.md)
