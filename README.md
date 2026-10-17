
# AWS Automated Backup System

## Project Overview
This project automates Amazon EBS snapshot creation using AWS Lambda and Amazon EventBridge Scheduler. Amazon SNS sends an email notification when snapshot creation is initiated.

## AWS Services Used
- Amazon EC2
- Amazon EBS Snapshots
- AWS Lambda (Python and Boto3)
- Amazon EventBridge Scheduler
- AWS IAM
- Amazon SNS
- Amazon CloudWatch Logs

## Architecture
EventBridge Scheduler → AWS Lambda → Amazon EBS Snapshot
                                      └→ Amazon SNS Email

IAM controls permissions, and CloudWatch Logs records Lambda execution details.

## Workflow
1. EventBridge Scheduler invokes Lambda on a daily schedule.
2. Lambda requests an EBS snapshot for the configured volume.
3. The snapshot is tagged with the project name.
4. Lambda publishes a notification to an SNS topic.
5. CloudWatch Logs helps monitor execution and troubleshoot errors.
6. Snapshot status is verified in the EC2 console.

## Testing and Validation
- Successfully invoked the Lambda function manually.
- Verified that an EBS snapshot reached Completed status.
- Created and enabled a recurring EventBridge schedule.
- Verified successful Lambda execution in CloudWatch Logs.
- Configured an SNS email subscription.

## Security Considerations
- Lambda uses an IAM execution role.
- SNS publishing should be restricted to the intended topic.
- Review and reduce broad EC2 permissions before production use.
- Never commit AWS access keys, passwords, or sensitive account details.

## Limitations
- The SNS notification confirms snapshot creation was initiated, not that the snapshot completed.
- Snapshot retention and automatic cleanup are not yet implemented.
- Restore testing is a future improvement.

## Future Improvements
- Send notifications after snapshot completion.
- Add snapshot retention and automatic cleanup.
- Test recovery from a snapshot.
- Restrict IAM permissions further.
- Add an architecture diagram and practical screenshots.

## What I Learned
- Creating EBS snapshots with Boto3.
- Automating Lambda execution with EventBridge Scheduler.
- Configuring IAM permissions for AWS services.
- Sending notifications through SNS.
- Troubleshooting authorization errors using CloudWatch Logs.
