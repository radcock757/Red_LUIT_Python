#!/usr/bin/env python3.7

#Import Boto3
import boto3

sqs = boto3.client('sqs')

response = sqs.create_queue(
    QueueName='my_queue'
)

print('Queue created')
    