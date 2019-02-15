
  # check whether at least two elements were entered
import boto3
import sys

ec2 = boto3.client('ec2',aws_access__id='<YOUR ID KEY>', aws_secret_access_key='<YOUR ACCESS KEY>',region_name='YOUR REGION')



def main():  
  if len(sys.argv) < 2:
    print ("Usage: python aws.py {start|stop|status + InstanceID}")
    print ("OR: python aws.py {show}\n")

    sys.exit(0)
  else:
    action = sys.argv[1] 

  if action == "start":
    startInstance()
  elif action == "stop":
    stopInstance()
  elif action == "status":
    status()
  elif action == "show":
    show()
  else:
    print ("Usage: python aws.py {start|stop|show (to show instances)}\n")  
  #Instance_ID = sys.argv[2]


def show():
  response = ec2.describe_instances()
  num = 0
  for reservation in response["Reservations"]:
   for instance in reservation["Instances"]:
     num+=1
     print("{0}.".format(num),instance["InstanceId"])
     print("\t-",instance["InstanceType"])

def status():
  ec2resource = boto3.resource('ec2',aws_access_key_id='<YOUR ID KEY>', aws_secret_access_key='<YOUR ACCESS KEY>',region_name='<YOUR REGION>')

  instance = ec2resource.Instance('{0}'.format(sys.argv[2]))
  print(instance.state['Name'])

     

def startInstance():
  print("Staring instance.....\n")
  try:
    #ec2.instance(instance_ids='{0}'.format(sys.argv[2])).start()
    ec2.start_instances(InstanceIds=['{0}'.format(sys.argv[2])])
  except:
    print("Have you forgotten to enter the ID flag?\n If not, just check that the ID is correct")
    sys.exit(0)

def stopInstance():
  print ("Stopping the instance...")
  try:
    ec2.stop_instances(InstanceIds=['{0}'.format(sys.argv[2])])  
  except:
    print("Have you forgotten to enter the ID flag?\n If not, just check that the ID is correct")
    sys.exit(0)

if __name__ == '__main__':
  main()
