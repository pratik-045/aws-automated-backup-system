
# AWS Automated Backup System

## Overview
This project automates Amazon EBS volume snapshots using
AWS Lambda and Amazon EventBridge Scheduler.

## AWS Services Used
- Amazon EC2 and EBS
- AWS Lambda (Python / Boto3)
- Amazon EventBridge Scheduler
- AWS IAM
- Amazon SNS
- Amazon CloudWatch Logs

## Workflow
1. EventBridge Scheduler invokes Lambda daily.
2. Lambda creates an EBS snapshot.
3. The snapshot receives project tags.
4. Lambda publishes a notification to an SNS topic.
5. CloudWatch Logs records the function execution.

## Security
- Lambda uses an IAM execution role.
- SNS publishing is restricted to the project topic.
- Review and restrict EC2 snapshot permissions before production use.

## Testing
- Manually invoked the Lambda function.
- Verified that the EBS snapshot reached Completed status.
- Configured a recurring EventBridge schedule.

## Future Improvements
- Snapshot retention and automatic cleanup
- Notifications after snapshot completion
- Restore testing
- More restrictive IAM permissions
