import boto3
import json
from botocore.exceptions import ClientError
from config import IAM_USER_NAME, ROLE_NAME

iam = boto3.client('iam')

def create_user():
    try:
        iam.create_user(UserName=IAM_USER_NAME)
        print("User created:", IAM_USER_NAME)
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print("User already exists:", IAM_USER_NAME)
        else:
            raise e


def create_role():
    assume_role_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {"Service": "ec2.amazonaws.com"},
                "Action": "sts:AssumeRole"
            }
        ]
    }

    try:
        iam.create_role(
            RoleName=ROLE_NAME,
            AssumeRolePolicyDocument=json.dumps(assume_role_policy)
        )
        print("Role created:", ROLE_NAME)
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print("Role already exists:", ROLE_NAME)
        else:
            raise e


def create_instance_profile():
    try:
        iam.create_instance_profile(InstanceProfileName=ROLE_NAME)
        print("Instance profile created:", ROLE_NAME)
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print("Instance profile already exists:", ROLE_NAME)
        else:
            raise e

    try:
        iam.add_role_to_instance_profile(
            InstanceProfileName=ROLE_NAME,
            RoleName=ROLE_NAME
        )
        print("Role attached to instance profile")
    except ClientError as e:
        if e.response['Error']['Code'] in ['LimitExceeded', 'EntityAlreadyExists']:
            print("Role already attached")
        else:
            raise e