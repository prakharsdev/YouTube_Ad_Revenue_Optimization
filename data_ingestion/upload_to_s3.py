import boto3
import json

s3 = boto3.client('s3')
bucket_name = 'youtube-data-bucket'

def upload_to_s3(data, filename):
    s3.put_object(Bucket=bucket_name, Key=filename, Body=json.dumps(data))

if __name__ == "__main__":
    from fetch_youtube_data import fetch_youtube_data
    data = fetch_youtube_data()
    upload_to_s3(data, 'raw/youtube_data.json')
