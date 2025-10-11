import boto3

# Creating S3 client object.
# Boto3 will use the credentials from 'aws configure'.

try:
    s3_client = boto3.client('s3')

    # Calling the list_buckets() method to get a list of all buckets
    response = s3_client.list_buckets()

    # Print the bucket names
    print("S3 Buckets:")
    if not response['Buckets']:
        print("  - No buckets found.")
    else:
        for bucket in response['Buckets']:
            print(f"  - {bucket['Name']}")

except Exception as e:
    print(f"An error occurred: {e}")