# SPLITS THE FILES INTO 1 MILLION ROW CHUNKS

import json, os, calendar
from datetime import datetime
import boto3
import codecs

session = boto3.session.Session(profile_name="phx", region_name = "us-east-1")

def lambda_handler(event, context):
    
    cloudwatch = session.client('cloudwatch')
    date = datetime.now()
    first = date.replace(day=1)
    last = date.replace(day = calendar.monthrange(date.year, date.month)[1])
    print('first: ', first)
    print('last: ', last)
    
    targetGroupARN='arn:aws:lambda:us-east-1:704208842596:function:test'
    tgarray=targetGroupARN.split(':')
    target=tgarray[-1]
    print(target)
    
    response = cloudwatch.get_metric_data(
        MetricDataQueries=[
            {
                'Id': 'if1',
                'MetricStat': {
                    'Metric': {
                        'Namespace': 'AWS/Lambda',
                        'MetricName': 'Invocations',
                        'Dimensions': [
                            {
                                'Name': 'lambda',
                                'Value': 'test',
                            },
                        ]
                    },
                    'Period': 18000,
                    'Stat': 'Sum',
                    'Unit': 'Seconds'
                }
            },
        ],
        # StartTime=datetime(first.year, first.month, first.day),
        StartTime=datetime(2024, 3, 8),
        # EndTime=datetime(last.year, last.month, last.day),
        EndTime=datetime(2024, 3, 10),
    )
    
    print(response)
    return response

if __name__ == '__main__':
    event = "buk1"
    context = "buk2"
    lambda_handler(event, context)