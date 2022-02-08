#!/usr/bin/env python
def create_bucket(bucket_name, location):
    bucket_name = input("what bucket do you want to create?\n")
    s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)


def delete_bucket(bucket_name):
    decision = input('Do you want to use the default "eng103a-shadman-test" bucket? (y/N): ').lower()
    if decision == 'n':
        bucket_name = input("what bucket do you want to delete?\n")
    s3.Bucket(bucket_name).delete()


def upload_file(bucket_name):
    decision = input('Do you want to use the default "eng103a-shadman-test" bucket? (y/N): ').lower()
    if decision == 'n':
        bucket_name = input("what bucket do you want use?\n")
    file_name = input("What file do you want to upload?\n")
    decision = input("Would you like to change the destination file name? (y/N): ").lower()
    if decision == 'y':
        destinationfile = input("What do you want to name the destination file?\n")
    else:
        destinationfile = file_name
    s3.Bucket(bucket_name).upload_file(file_name, destinationfile)


def download_file(bucket_name):
    decision = input('Do you want to use the default "eng103a-shadman-test" bucket? (y/N): ').lower()
    if decision == 'n':
        bucket_name = input("what bucket do you want use?\n")
    file_name = input("What file do you want to download?\n")
    decision = input("Would you like to change the destination file name? (y/N): ").lower()
    if decision == 'y':
        destinationfile = input("What do you want to name the destination file?\n")
    else:
        destinationfile = file_name
    s3.Bucket(bucket_name).download_file(file_name, destinationfile)


def delete_file(bucket_name):
    decision = input('Do you want to use the default "eng103a-shadman-test" bucket? (y/N): ').lower()
    if decision == 'n':
        bucket_name = input("what bucket do you want use?\n")
    file_name = input("What file do you want to delete?\n")
    s3.Object(bucket_name, file_name).delete()


import boto3
bucket_name = "eng103a-shadman-test"
location = {'LocationConstraint': "eu-west-1"}
s3 = boto3.resource('s3')


while True:
    option = input('\n\n(1) Create bucket\n(2) Delete bucket\n(3) Upload file\n(4) Download file\n(5) Delete file\n(6) Exit\nChoose Option [1-6]: ')
    print('\n')
    if option == '1':
        create_bucket(bucket_name, location)
    elif option == '2':
        delete_bucket(bucket_name)
    elif option == '3':
        upload_file(bucket_name)
    elif option == '4':
        download_file(bucket_name)
    elif option == '5':
        delete_file(bucket_name)
    elif option == '6':
        break
    else:
        print('Please choose a Valid option')