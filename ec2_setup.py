import boto3
from config import AMI_ID, INSTANCE_TYPE, KEY_NAME, ROLE_NAME

ec2 = boto3.resource('ec2')

def create_instance(security_group_id):
    try:
        user_data_script = """#!/bin/bash
apt update -y
apt install python3 python3-pip -y

pip3 install flask

cat <<EOF > app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "AWS Automation Successful!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
EOF

nohup python3 app.py > output.log 2>&1 &
"""

        instances = ec2.create_instances(
            ImageId=AMI_ID,
            InstanceType=INSTANCE_TYPE,
            KeyName=KEY_NAME,
            MinCount=1,
            MaxCount=1,
            SecurityGroupIds=[security_group_id],
            IamInstanceProfile={'Name': ROLE_NAME},
            UserData=user_data_script,
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [{'Key': 'Project', 'Value': 'AWS-Automation'}]
                }
            ]
        )

        instance = instances[0]

        print("Launching EC2 instance...")
        instance.wait_until_running()
        instance.reload()

        print("Instance running:", instance.id)
        print("Public IP:", instance.public_ip_address)

    except Exception as e:
        print("EC2 error:", e)