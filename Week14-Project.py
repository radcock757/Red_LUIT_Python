#!/usr/bin/env python3.7

import boto3 #import boto3 module

dynamodb = boto3.resource('dynamodb') # Get the service resource.

my_table = dynamodb.create_table( # Create the DynamoDB table.
    TableName='Movies',
    KeySchema=[
        {
            'AttributeName': 'movie_title',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'director_name',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'movie_title',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'director_name',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

my_table.wait_until_exists() # Wait until the table exists.

with my_table.batch_writer () as batch: #Add items to the table
    batch.put_item(
        Item={
            'movie_title' : 'Titanic',
            'director_name' : 'James Cameron'
            }
        )
    batch.put_item(
        Item={
            'movie_title' : 'North by Northwest',
            'director_name' : 'Alfred Hitchcock'
            }
        )
    batch.put_item(
        Item={
            'movie_title' : 'Citizen Kane',
            'director_name' : 'Orson Welles'
            }
        )
    batch.put_item(
        Item={
            'movie_title' : 'The Quiet Man',
            'director_name' : 'John Ford'
            }
        )
    batch.put_item(
        Item={
            'movie_title' : 'Goodfellas',
            'director_name' : 'Martin Scorsese'
            }
        )
    batch.put_item(
        Item={
            'movie_title' : 'Jaws',
            'director_name' : 'Steven Spielberg'
            }
        )
    batch.put_item(
        Item={
            'movie_title' : 'The Shining',
            'director_name' : 'Stanley Kubrick'
            }
        )
    batch.put_item(
        Item={
            'movie_title' : 'Beetlejuice',
            'director_name' : 'Tim Burton'
            }
        )
    batch.put_item(
        Item={
            'movie_title' : 'Avatar',
            'director_name' : 'James Cameron'
            }
        )
    batch.put_item(
        Item={
            'movie_title' : 'The Sixth Sense',
            'director_name' : 'M. Night Shyamalan'
            }
        )
    batch.put_item(
        Item={
            'movie_title' : 'Top Gun: Maverick',
            'director_name' : 'Joseph Kosinski'
            }
        )
        

print(my_table.item_count) # Print out the number of items in the table.

response = my_table.scan() # Scan the table
item = response['Items']
print(*item, sep = "\n") # Print the results of the table scan