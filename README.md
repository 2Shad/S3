# S3 (Simple Storage Service)
### Amazon's Redundant Storage solution service.
How to connect:
- Install `python3-pip`
- Set alias `python=python3` and check `python --version`
- Install AWS CLI `sudo pip3 install awscli`
- Configure AWS CLI, `aws configure` enter keys, and region is `eu-west-1` and `json` format.
- Check and verify connection with `aws s3 ls`
  
![S3](S3.png)


- `aws s3 mb s3://{bucket-name}` Bucket naming conventions no `_`
- `aws s3 rm --recursive s3://{bucket-name}` to delete the content of bucket
- `aws s3 rb s3://{bucket-name}` to remove bucket

s3://eng103a-shadman-devops