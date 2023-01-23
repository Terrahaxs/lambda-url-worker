## Lambda Function URL Terrahaxs Worker

This repo deploys the Terrahaxs Worker as a Lambda exposed via a function URL.

### Deployment

We use [AWS SAM](https://aws.amazon.com/serverless/sam/) to manage and deploy serverless functions.

Deployment is easy with:

```bash
sam build
sam deploy --config-file samconfig.toml
```