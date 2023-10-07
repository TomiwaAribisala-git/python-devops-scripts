# A python script that checks an AWS EC2 Instance State and Status in a specific region

import boto3

# Define the EC2 instance ID you want to check
instance_id = 'i-08d002a6b831c8a47'

# Initialize a Boto3 EC2 client
ec2 = boto3.client('ec2', region_name="eu-north-1")

def check_instance_state_and_status():
    try:
        # Describe the instance status
        response = ec2.describe_instance_status(InstanceIds=[instance_id])

        if len(response['InstanceStatuses']) == 0:
            print(f"Instance {instance_id} does not exist or has no status information.")
        else:
            instance_status = response['InstanceStatuses'][0]
            instance_state = instance_status['InstanceState']['Name']
            instance_status_check = instance_status['SystemStatus']['Status']

            print(f"Instance ID: {instance_id}")
            print(f"Instance State: {instance_state}")
            print(f"System Status Check: {instance_status_check}")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    check_instance_state_and_status()