import subprocess
import boto3
import mlflow.sagemaker as mfs
import json
from from_root import from_root




def upload(s3_bucket_name, mlruns_dir=None):
        try:
            output = subprocess.run(["aws", "s3", "sync", "{}".format(mlruns_dir),
                                     "s3://{}".format(s3_bucket_name)],
                                    stdout=subprocess.PIPE,
                                    encoding='utf-8')
            
            print('\n saved to bucket: ', s3_bucket_name)
            

            return f"Done Uploading : {output.stdout}"

        except Exception as e:
            return f"Error Occurred While Uploading : {e.__str__()}"