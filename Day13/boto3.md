# Boto3: The AWS SDK for Python 🐍

Boto3 is the official Amazon Web Services (AWS) SDK for Python. It allows you to directly create, update, and delete AWS resources from your Python scripts. It's an essential tool for any developer working with AWS services like S3, EC2, Lambda, and more.

***

## Prerequisites

Before you start, make sure you have:
1.  **Python 3.6+** installed on your system.
2.  An **AWS account** with an IAM user.
3.  Your IAM user's **Access Key ID** and **Secret Access Key**.

***

## Installation and Configuration

Setting up Boto3 involves two main steps: installing the library itself and configuring your AWS credentials so the library knows which account to connect to.

### 1. Install Boto3

You can install the Boto3 library directly using `pip`, the Python package installer.

```bash
pip install boto3
```

### 2. Configure AWS Credentials

The recommended way to configure your credentials for Boto3 is by using the **AWS Command Line Interface (CLI)**. Boto3 will automatically find and use the credentials configured by the CLI.

First, install the AWS CLI:
```bash
pip install awscli
```

Next, run the `configure` command. It will prompt you for your credentials.

```bash
aws configure
```

You'll be asked for four pieces of information. The first two are essential for authentication.

* **AWS Access Key ID:** `[YOUR_ACCESS_KEY_ID]`
* **AWS Secret Access Key:** `[YOUR_SECRET_ACCESS_KEY]`
* **Default region name:** `us-east-1` (or your preferred region, e.g., `ap-south-1`)
* **Default output format:** `json` (This is the most common choice)

This command creates two files, `~/.aws/credentials` and `~/.aws/config`, which Boto3 uses to connect to your AWS account securely.

