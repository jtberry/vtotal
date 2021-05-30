# Virus Total

## Purpose
Configuring a python script to use the Virus Total api. Will then move to Lambda to have run when a file is uploaded to s3. 

### Package for Lambda
This will let you create the package for you lambda. Since we have to import requests we have package all needed libraries for the lambda to run. You can name all this whatever you want.
>Command:
>```bash
>$ mkdir your_folder_name
>$ cd your_folder_name
>$ ls
>virus_total.py
>$ pip3 install --target ./package >requests
>$ cd package
>$ zip -r ../virus-total.zip .
>$ cd ..
>$ zip -g virus-total.zip virus_total.py
>```
For now you can create your function via awscli, will be updating for CFN or Terraform Deployment
>Command:
>```bash
>aws lambda create-function --function-name <function >anme> --zip-file fileb://<your zip file> --handler ><your script name>.lambda_handler --runtime python3.>8 --role arn:aws:iam::<your account:role/<your role>
>```

### Permissions
You will the standard lambda execution role but this also uses AWS Secrets Manager for the API KEY for Virus Total. This will need basic permissions to read the secrets to the one key. 