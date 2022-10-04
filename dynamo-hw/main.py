import boto3
import hashlib
from boto3.dynamodb.conditions import Key, Attr

session = boto3.Session(
aws_access_key_id='<ACCESS KEY>',
aws_secret_access_key='<SECRETKEY>')
#Then use the session to get the resource
dynamodb=session.resource("dynamodb")
table=dynamodb.Table("dynamo_hw")
s3 = session.resource('s3')
bucket='buquettino'
my_bucket = s3.Bucket(bucket)
dict={}
for my_bucket_object in my_bucket.objects.all():
    body=my_bucket_object.get()['Body'].readline().decode('utf-8')
    encoded=body.encode()
    hash=hashlib.sha256(encoded).hexdigest()
    response = table.query(KeyConditionExpression=Key('hash').eq(hash))
    if response['Items'] != []:
        print('Duplicate detected - skipped')
        print("##################################################")
        continue
    dict['hash']=hash
    dict['firstline']=list(dict.fromkeys(body[:-2].split())) ##dict.fromkeys makes sure they do be unique
    dict['name']=my_bucket_object.key
    dict['size']=my_bucket_object.get()['ContentLength']
    dict['url']="https://"+bucket+".s3.amazonaws.com/"+my_bucket_object.key
    table.put_item(Item=dict)
    s3.Bucket('dynamo-hw-2nd-bucket').put_object( Key=dict['name'], Body=body)
    print("Item:")
    print(dict)
    print("inserted to the second bucket successfully")
    print("##################################################")
