"""
Project: AWS EC2 Instance Automation using Python & Boto3

Description:
This script automates the creation of an AWS EC2 instance using
Python and the Boto3 library.

Technologies Used:
- Python
- AWS EC2
- Boto3

Features:
- Connects to AWS EC2 service
- Creates a new EC2 instance
- Uses a specified AMI and instance type
- Demonstrates basic cloud automation

Author: Ronak Saini
"""

import boto3

# Create EC2 resource
ec2 = boto3.resource(
    'ec2',
    aws_access_key_id='YOUR_ACCESS_KEY',
    aws_secret_access_key='YOUR_SECRET_KEY',
    region_name='ap-south-1'
)

# Launch EC2 Instance
instance = ec2.create_instances(
    ImageId='ami-0f5ee92e2d63afc18',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro'
)

print("✅ EC2 Instance Created Successfully")