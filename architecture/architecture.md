
# Architecture

1. EventBridge Scheduler invokes the Lambda function daily.
2. Lambda uses Boto3 to request an EBS snapshot.
3. The snapshot is tagged with the project name.
4. Lambda publishes a notification to Amazon SNS.
5. CloudWatch Logs captures execution details.
6. IAM controls the permissions required by the workflow.

## Important
The SNS message confirms that snapshot creation was started.
Check the snapshot status in EC2 to confirm completion.
