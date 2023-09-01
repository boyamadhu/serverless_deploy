import pandas as pd
import boto3

try:
    import unzip_requirements
except ImportError:
    pass

import json

BUCKET_NAME = "sample-bucket-cargo-madhu"
CSV_FILE_NAME = "sample.csv"
REGION = "us-west-2"


def hello(event, context):
    s3 = boto3.client('s3', region_name=REGION)
    
    # Check if the bucket already exists
    data = {
        'Column1': [1, 2, 3, 4],
        'Column2': ['A', 'B', 'C', 'D']
    }
    df = pd.DataFrame(data)
    print(df)
    
    # Convert the DataFrame to a CSV file
    csv_data = df.to_csv(index=False)
    
    # Upload the CSV file to the S3 bucket
    s3.put_object(Bucket=BUCKET_NAME, Key=CSV_FILE_NAME, Body=csv_data)

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    
    return response