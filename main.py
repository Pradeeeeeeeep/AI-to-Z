import os
import boto3
from dotenv import load_dotenv

load_dotenv()

# Map API key from .env to AWS_BEARER_TOKEN_BEDROCK if provided
api_key = os.getenv("API_key") or os.getenv("AWS_BEARER_TOKEN_BEDROCK")
if api_key:
    os.environ["AWS_BEARER_TOKEN_BEDROCK"] = api_key

# Initialize Bedrock client using API key
client = boto3.client(
    service_name="bedrock-runtime",
    region_name=os.getenv("Region", "us-east-1")
)

# Select model
MODEL_ID = "moonshotai.kimi-k2.5"

txt = input("Ask me anything")

# Make request
response = client.converse(
    modelId=MODEL_ID,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "text": txt
                }
            ]
        }
    ],
    inferenceConfig={
        "maxTokens": 500,
        "temperature": 0.7
    }
)

# Extract response
answer = response["output"]["message"]["content"][0]["text"]

print(answer)