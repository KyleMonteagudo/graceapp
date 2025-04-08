from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import base64
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
import azure.cognitiveservices.speech as speechsdk

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Read configuration from environment variables
endpoint = os.getenv("ENDPOINT_URL", "INSERT AZURE OPENAI ENDPOINT URL") 
deployment = os.getenv("DEPLOYMENT_NAME", "INSERT DEPLOYMENT NAME")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "INSERT YOUR API KEY HERE")  

# Initialize Azure OpenAI Service client with key-based authentication    
client = AzureOpenAI(  
    azure_endpoint=endpoint,  
    api_key=subscription_key,  
    api_version="2024-05-01-preview",
)

@app.route("/chat", methods=["POST"])
def chat():
    user_text = request.json.get("text", "")
    
    # Build the chat prompt
    chat_prompt = [
        {
            "role": "system",
            "content": [{
                "type": "text",
                "text": ("You are an AI assistant that answers questions users input.")
            }]
        },
        {
            "role": "user",
            "content": [{
                "type": "text",
                "text": user_text
            }]
        }
    ]

    try:
        completion = client.chat.completions.create(
            model=deployment,
            messages=chat_prompt,
            max_tokens=4096,
            temperature=0.7,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None,
            stream=False
        )
        return jsonify({
            "choices": [
            {
                "message": {
                    "content": completion.choices[0].message.content
                }
            }
            ]
        }) 
     
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # For local testing use debug mode
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
