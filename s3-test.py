import boto3


# constants
BUCKET_NAME = "pretty-curly-girl"
S3_FILE = "smile3.webp"
LOCAL_NAME = "smile.webp"


# test listing
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print("BUCKET_NAME")


# test downloading
bucket.download_file(S3_FILE, LOCAL_NAME)

# test uploading
data = open('smile.webp', 'rb')
bucket.put_object(Key='smile3.webp', Body=data)
