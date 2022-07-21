# mlflow-aws-integration


## Permissions
1.AmazonS3FullAccess
2.EC2InstanceProfileForImageBuilderECRContainerBuilds
3.AmazonEC2ContainerRegistryFullAccess
4.AWSAppRunnerServicePolicyForECRAccess

## To Mlflow Server
```bash
mlflow server --backend-store-uri postgresql://postgres:chandu99@database-1.cdje2gkuei78.us-west-1.rds.amazonaws.com/mlflow-db --default-artifact-root ./artifacts --host 127.0.0.1 -p 5000
```

## Dckerization and push to ECR
```bash
mlflow sagemaker build-and-push-container
```


