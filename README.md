# What does this demo showcase?
This demo shows a scenario where a customer calls into a contact center and the center IVR menu predicts his/her intention to call the service. 
This way, the customer experience is improved and time is saved. 

# How to launch & run this demo?

## Step 1: Create Personalize resources using this predefined SageMaker notebook
Click on the link below to launch a CloudFormation stack.  This CF template launches the necessary IAM roles and SageMaker notebooks. Run the training notebook.

[![Launch CloudFormation Stack1](images/cloudformation-launch-stack-1.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?templateURL=https://aws-contact-center-blog.s3.amazonaws.com/predict-customer-intent/personalize-training-notebook.yaml&stackName=predict-ci-nb&param_ResourceBucket=aws-contact-center-blog&param_PersonalizeResourceBucketRelativePath=predict-customer-intent/personalize/sourcecode.zip)
 
## Step 2: Launch Lambda Functions to invoke the Personalize service
1. Click on the link below to launch a CloudFormation stack.  This CF template launches the necessary lambda functions.

[![Launch CloudFormation Stack2](images/cloudformation-launch-stack-2.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?templateURL=https://aws-contact-center-blog.s3.amazonaws.com/predict-customer-intent/wrapper-lambda-functions.yaml&stackName=predict-ci-lf&param_ResourceBucket=aws-contact-center-blog&param_ResourceBucketKeyForUpdateEventLambdaFunction=predict-customer-intent/lambda/ccblog-update-real-time-customer-interactions-38d9b958-b7c9-4064-af7f-ddb06ced614b.zip&param_ResourceBucketKeyForGetRecommentationLambdaFunction=predict-customer-intent/lambda/ccblog-get-personalized-intent-d041341f-50b2-4017-8dee-3a885af2b0b9.zip&param_PersonalizeRegion=us-east-1&param_PredictionConfidenceScoreHighThreshold=0.8&param_PredictionConfidenceScoreLowThreshold=0.6&param_PersonalizeCampaignARN=Fill_this_in&param_PersonalizeModelTrackingID=Fill_this_in)
 

## Step 3: Integrate the Amazon Connect instance with the prediction service

To be added. 
