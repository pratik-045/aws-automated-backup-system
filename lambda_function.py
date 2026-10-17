
import boto3
from datetime import datetime, timezone

ec2 = boto3.client("ec2")
sns = boto3.client("sns")

VOLUME_ID = "vol-***"
SNS_TOPIC_ARN = "arn:aws:sns:ap-south-1-***"


def lambda_handler(event, context):
    timestamp = datetime.now(timezone.utc).strftime(
        "%Y-%m-%d %H:%M UTC"
    )

    response = ec2.create_snapshot(
        VolumeId=VOLUME_ID,
        Description=f"Automated EBS backup - {timestamp}",
        TagSpecifications=[
            {
                "ResourceType": "snapshot",
                "Tags": [
                    {
                        "Key": "Name",
                        "Value": "pratik-automated-backup"
                    },
                    {
                        "Key": "Project",
                        "Value": "AWS-Automated-Backup"
                    }
                ]
            }
        ]
    )

    snapshot_id = response["SnapshotId"]

    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject="AWS EBS Backup Started",
        Message=(
            "EBS snapshot creation started.\n"
            f"Snapshot ID: {snapshot_id}\n"
            f"Volume ID: {VOLUME_ID}\n"
            f"Time: {timestamp}"
        )
    )

    return {
        "statusCode": 200,
        "snapshot_id": snapshot_id,
        "message": "Snapshot started and notification sent"
    }
