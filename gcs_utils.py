# gcs_utils.py

from google.cloud import storage  
import os

class GCSHandler:
    """A class to handle Google Cloud Storage operations."""

    def __init__(self):
        """Initialize the GCSHandler and check for credentials."""
        self.cred_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
        if not self.cred_path:
            raise EnvironmentError("Environment variable for credentials (GOOGLE_APPLICATION_CREDENTIALS) is not set.")
        print(f"Using credentials from: {self.cred_path}")

    def upload_blob(self, bucket_name, source_file_name, destination_file_name):
        """Uploads a file to the specified bucket."""
        try:
            storage_client = storage.Client()
            bucket = storage_client.bucket(bucket_name)
            blob = bucket.blob(destination_file_name)
            
            # Upload the file to the specified destination
            blob.upload_from_filename(source_file_name)
            print(f"{source_file_name} uploaded to {destination_file_name} in bucket {bucket_name}.")
        
        except Exception as e:
            print(f"An error occurred while uploading the file: {e}")

    def create_bucket(self, bucket_name):
        """Creates a new bucket in the project."""
        try:
            # Initialize a storage client
            client = storage.Client()
            
            # Create the bucket
            new_bucket = client.create_bucket(bucket_name)  # Create the bucket
            
            print(f"Bucket {new_bucket.name} created successfully.")
        
        except Exception as e:
            print(f"An error occurred while creating the bucket: {e}")
