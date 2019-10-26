#Zip all Lambda functions
#cd domain-setter-lambda; zip -r ../domain-setter-lambda.zip *; cd ..
#cd es-cognito-auth-lambda; zip -r ../es-cognito-auth-lambda.zip *; cd ..
#cd kibana-customizer-lambda; zip -r ../kibana-customizer-lambda.zip *; cd ..

import boto3

bucket_prefix = "waf-dashboards-"
regions = ["us-east-1","us-east-2","us-west-1","us-west-2","ca-central-1","eu-central-1","eu-west-1","eu-west-2","eu-west-3","eu-north-1","ap-northeast-1","ap-northeast-2","ap-northeast-3","ap-southeast-1","ap-southeast-2","ap-south-1","sa-east-1"]

for region in regions:
    print("Working on region: " + region);
    bucket_name = bucket_prefix + region
    #s3 = boto3.client('s3', region_name=region)
    #s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': region})

    file1 = 'domain-setter-lambda.zip'
    file2 = 'es-cognito-auth-lambda.zip'
    file3 = 'kibana-customizer-lambda.zip'

    s3 = boto3.resource('s3')
    s3.Bucket(bucket_name).upload_file(file1,file1)
    s3.Bucket(bucket_name).upload_file(file2,file2)
    s3.Bucket(bucket_name).upload_file(file3,file3)

    s3 = boto3.client('s3', region_name=region)
    s3.put_object_acl(ACL='public-read', Bucket=bucket_name, Key=file1)
    s3.put_object_acl(ACL='public-read', Bucket=bucket_name, Key=file2)
    s3.put_object_acl(ACL='public-read', Bucket=bucket_name, Key=file3)


#Delete all local resources which are not needed anymore
#rm domain-setter-lambda.zip
#rm es-cognito-auth-lambda.zip
#rm kibana-customizer-lambda.zip
