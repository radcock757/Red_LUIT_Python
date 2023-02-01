#List of AWS Services

#Create Empty List
AWS_services_list = []

#Add items to the list
AWS_services_list.append ("EC2")
AWS_services_list.append ("Lambda")
AWS_services_list.append ("DyanmoDB")
AWS_services_list.append ("ECS")
AWS_services_list.append ("EFS")
AWS_services_list.append ("AutoScalingGroups")
AWS_services_list.append ("ElasticLoadBalancers")
AWS_services_list.append ("ElasticBeanstalk")

#Print the list
print(AWS_services_list)

#Insert items to the list
AWS_services_list.insert (3, "CodePipeline")
AWS_services_list.insert (6, "CodeStar")

#Print updated list
print(AWS_services_list)

#Print the first item in the list
print(AWS_services_list[0])

#Print the 5th item in the list
print(AWS_services_list[4])



