import boto3
import json
from pprint import pprint
 
ec2 = boto3.client('ec2')
lab_instances = ec2.describe_instances()
 
instance_id = lab_instances["Reservations"][0]["Instances"][0]["InstanceId"]
print(json.dumps(instance_id, indent=2, default=str))

ec2.terminate_instances(instance_id=[instance_id])
print(f"instancia terminada : {instance_id}")