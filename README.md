## Lambda Function URL Terrahaxs Worker

This repo deploys the Terrahaxs Worker as a Lambda exposed via a function URL.

### Prerequisites

1. Install [AWS SAM](https://aws.amazon.com/serverless/sam/) installed.
2. Install Docker or alternative

### Setup

Before deploying you can modify the Dockerfile to have the correct versions of Terraform and any other dependencies you may
use in your workflow (i.e. Terragrunt). You may also want to review the `template.yaml` file to ensure the IAM policies
are suitable for your use-case.

*Note: ensure your Terraform lock files support the architecture specified in the `template.yaml` file. We are using `arm64` but you may
want to use `x86_64`.

### Deployment

You can deploy the worker as a lambda with a public url by running the following commands:

```bash
sam build
sam deploy --config-file samconfig.toml
```

*Note: ensure you are using the correct AWS Profile when deploying*