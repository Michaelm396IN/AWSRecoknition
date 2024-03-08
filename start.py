#Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-custom-labels-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3
#from codeguru_profiler_agent import Profiler

def start_model(project_arn, model_arn, version_name, min_inference_units):

    client=boto3.client('rekognition',region_name="us-east-1")

    try:
        # Start the model
        print('Starting model: ' + model_arn)
        response=client.start_project_version(ProjectVersionArn=model_arn, MinInferenceUnits=min_inference_units)
        # Wait for the model to be in the running state
        project_version_running_waiter = client.get_waiter('project_version_running')
        project_version_running_waiter.wait(ProjectArn=project_arn, VersionNames=[version_name])

        #Get the running status
        describe_response=client.describe_project_versions(ProjectArn=project_arn,
            VersionNames=[version_name])
        for model in describe_response['ProjectVersionDescriptions']:
            print("Status: " + model['Status'])
            print("Message: " + model['StatusMessage']) 
    except Exception as e:
        print(e)
        
    print('Done...')
    
def main():
    project_arn='arn:aws:rekognition:us-east-1:471112774796:project/recoknition_ex/1709885642762'
    model_arn='arn:aws:rekognition:us-east-1:471112774796:project/recoknition_ex/version/recoknition_ex.2024-03-08T01.04.15/1709888655581'
    min_inference_units=1 
    version_name='recoknition_ex.2024-03-08T01.04.15'
    #custom_session = boto3.session.Session(profile_name='moorer_role', region_name='us-east-2')
    #Profiler(profiling_group_name="SampleProfilingGroup").start()
    start_model(project_arn, model_arn, version_name, min_inference_units)
    

if __name__ == "__main__":
    main()
   
