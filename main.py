import time
from iam_setup import create_user, create_role, create_instance_profile
from s3_setup import create_bucket
from ec2_setup import create_instance
from security_group import create_security_group

def main():
    print("Starting AWS Automation...")

    create_user()
    create_role()
    create_instance_profile()

    print("Waiting for IAM propagation...")
    time.sleep(10)

    create_bucket()

    sg_id = create_security_group()

    if sg_id:
        create_instance(sg_id)

    print("Deployment Complete!")

if __name__ == "__main__":
    main()