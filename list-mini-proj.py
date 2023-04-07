#the list should be empty initially
services = []

#populate the list using append or insert
services.append('EC2')
services.append('RedShift')
services.append('Lambda')
services.append('S3')
services.append('RDS')
services.append('DynamoDB')
services.append('SageMaker')
services.append('OpenSearch')
services.append('SNS')

#print the list and the length of the list
print(len(services))

#remove two specific services from the list by name or by index.

#removed by index
del services[1:3]
#del services[3]
#removed by name
#services.remove("RedShift")

#print the new list and the new length of the list
print(services)
print(len(services))