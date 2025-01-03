from setuptools import setup, find_packages

with open('README.md') as readme:
    long_description = readme.read()

setup(
    name='eks_token',
    version='0.3.0',
    author='Peak AI',
    author_email='support@peak.ai',
    description='EKS Token package, an alternate to "aws eks get-token ..." CLI',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/peak-ai/eks-token',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    keywords='eks k8s boto3 awscli python aws',
    install_requires=["awscli>=1.27.8"],
)
