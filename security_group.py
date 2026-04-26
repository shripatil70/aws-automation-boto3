import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

def create_security_group():
    try:
        # Try creating new SG
        response = ec2.create_security_group(
            GroupName='flask-sg',
            Description='Allow HTTP access'
        )

        sg_id = response['GroupId']

        ec2.authorize_security_group_ingress(
            GroupId=sg_id,
            IpPermissions=[
                {
                    'IpProtocol': 'tcp',
                    'FromPort': 80,
                    'ToPort': 80,
                    'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                }
            ]
        )

        print("Security Group created:", sg_id)
        return sg_id

    except ClientError as e:
        if e.response['Error']['Code'] == 'InvalidGroup.Duplicate':
            print("Security Group already exists. Fetching existing one...")

            # 🔍 Find existing SG
            response = ec2.describe_security_groups(
                Filters=[{'Name': 'group-name', 'Values': ['flask-sg']}]
            )

            sg_id = response['SecurityGroups'][0]['GroupId']
            print("Using existing SG:", sg_id)
            return sg_id

        else:
            print("SG error:", e)
            return None