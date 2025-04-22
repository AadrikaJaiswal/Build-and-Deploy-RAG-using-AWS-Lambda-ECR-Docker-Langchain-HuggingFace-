import os
import json
import sys
import boto3

print("imported successfully...")

prompt= """
        you are a smart assistant so please let me know what is machine learning in smartest way?
"""

bedrock= boto3.client(service_name= "bedrock-runtime")

payload= {
    "prompt": "[INST]"+prompt+"[/INST]",
    #"max_gen_len": 512,
    "temperature": 0.3,
    "top_p": 0.9
}

body= json.dumps(payload)
model_id= "mistral.mixtral-8x7b-instruct-v0:1"

response= bedrock.invoke_model(
    body= body,
    modelId= model_id,
    accept= "application/json",
    contentType= "application/json"
)

# response_body= json.loads(response.get("body").read())
# response_text= response_body["generation"]
# print(response_text)

response_body = json.loads(response.get("body").read())
print(json.dumps(response_body, indent=2))  # 👈 See the full response format

# Then extract the text using the correct key
response_text = response_body["outputs"][0]["text"]
print(response_text)