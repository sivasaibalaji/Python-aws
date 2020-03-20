import boto3
s3_resource = boto3.resource('s3')
bucket=s3_resource.buckets.all()
for each_in in bucket:
   print(each_in)