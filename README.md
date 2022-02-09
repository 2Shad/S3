# S3 (Simple Storage Service)
### Amazon's S3 service offers Highly avaliable, scalable and redundent storage, at reasonable prices with their different tiers. It is generally used to store data that would be displayed in web, and for backup in case of a disaster.

![S3](S3.png)

## AWS-CLI

How to connect:
- Install `python3-pip`
- Set alias `python=python3` and check `python --version`
- Install AWS CLI `sudo pip3 install awscli`
- Configure AWS CLI, `aws configure` enter keys, and region is `eu-west-1` and `json` format.
- Check and verify connection with `aws s3 ls`


How to use AWS-CLI:
- To **Create** a bucket `aws s3 mb s3://{bucket-name}` *Note: bucket names cannot have `_` or caps*
- To **Upload** a file to bucket `aws s3 cp {file} s3://{bucket-name}`
- To **Download** a file from bucket ``aws s3 cp s3://{bucket-name}/{file} {destination}`
- To **Delete** all bucket content `aws s3 rm --recursive s3://{bucket-name}`
- To **Delete** a bucket `aws s3 rb s3://{bucket-name}` *Note: bucket first need to be empty*

## AWS with Python
We will use the boto3 pip package for this. We would first need to install said package.

How to use boto3:
First we need to create a variable associated with the boto3 class as 's3', `s3 = boto3.resource('s3')`

Key boto3 commands:
- To **Create** a bucket `s3.create_bucket(Bucket={bucket_name}, CreateBucketConfiguration={location})`
- To **Delete** a bucket `s3.Bucket({bucket_name}).delete()`
- To **Upload** a file to bucket `s3.Bucket({bucket_name}).upload_file({file_name}, {destination_file})`
- To **Download** a file from bucket `s3.Bucket({bucket_name}).download_file({file_name}, {destination_file})`
- To **Delete** a file from bucket `s3.Object({bucket_name}, {file_name}).delete()`

Using these boto3 commands we could create a [Python script](s3.py).