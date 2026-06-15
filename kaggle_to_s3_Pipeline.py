"""
Project: Kaggle to AWS S3 Data Pipeline

Description:
This script automates the process of:
1. Downloading a dataset from Kaggle
2. Creating an AWS S3 bucket
3. Uploading the dataset to AWS S3

Technologies Used:
- Python
- Kaggle API
- AWS S3
- Boto3


"""

from kaggle.api.kaggle_api_extended import KaggleApi
# kaggle.api.kaggle_api_extended ek module path hai jahan KaggleApi class stored hai 
# KaggleApi class import kar rahe hain dataset download ke liye
import boto3
# boto3 AWS services use karne ke liye library hai


#
# Download dataset from Kaggle
def download_dataset(dataset_link):
    api = KaggleApi()
    api.authenticate()

    api.dataset_download_files(
        dataset_link,
        path="kaggle_data",
        unzip=True
    )

    print("Dataset downloaded successfully")


# Create S3 bucket

def create_bucket(bucket_name, region="ap-south-1"):
    s3 = boto3.client("s3", region_name=region)

    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            "LocationConstraint": region
        }
    )

    print("bucket created successfully")


# Upload file to S3
def upload_file_to_s3(file_path, bucket_name, object_name):
    s3 = boto3.client("s3")

    s3.upload_file(
        file_path,
        bucket_name,
        object_name
    )

    print(" File uploaded successfully")


# ---------------- MAIN PROGRAM ---------------- #

DATASET = "mehmettahiraslan/customer-shopping-dataset"
BUCKET_NAME = "ronak-python-kaggle"

# Step 1: Download dataset
# download_dataset(DATASET)

# Step 2: Create bucket (Run only once)
# create_bucket(BUCKET_NAME)

# Step 3: Upload dataset to S3
upload_file_to_s3(
    file_path="D:/Big Data/kaggle_data/customer_shopping_data.csv",
    bucket_name=BUCKET_NAME,
    object_name="customer_shopping_data.csv"
)