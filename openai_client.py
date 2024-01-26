import json
import os
import requests
import base64
from dotenv import load_dotenv
import re

load_dotenv()

# Function to encode the image to base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

prompt = """You are a nutritionist, tasked with digitalizing nutritional values of a specific food or drink item. The attached image(s) depict(s) one particular food or drink item. Your job is to provide the fields for this item as shown in the examples below.
You MUST answer in JSON format only.
The field names MUST be InformalFoodName, KiloCaloriesPerItem, WeightGramsPerItem, CarbohydrateGramsPerItem, FiberGramsPerItem, FatGramsPerItem, ProteinGramsPerItem, and NumberOfItemConsumed.
If the serving size is known, you MUST assume the consumption, weight, and nutritive value for one serving.
You MUST avoid comments and your response MUST be a valid JSON object.
You MUST avoid '```' in your response.
You MUST avoid '//' in your response.
You MUST fill in all the fields in the examples below with estimates and avoid unknown values.
You MUST estimate every value to your best habilities and make sure all values are filled in.

### Example of an Apple:

{
    "InformalFoodName": "Apple, Red, Medium Sized",
    "KiloCaloriesPerItem": 95.0,
    "WeightGramsPerItem": 200.0,
    "CarbohydrateGramsPerItem": 25.0,
    "FiberGramsPerItem": 4.0,
    "FatGramsPerItem": 0.0,
    "ProteinGramsPerItem": 0.5,
    "NumberOfItemConsumed": 1.0
}

### Example of a 33 grams Serving:

{
    "InformalFoodName": "100% Vegan Protein Powder",
    "KiloCaloriesPerItem": 131.0,
    "WeightGramsPerItem": 33.0,
    "CarbohydrateGramsPerItem": 0.6,
    "FiberGramsPerItem": 0.0,
    "FatGramsPerItem": 2.6,
    "ProteinGramsPerItem": 24.0,
    "NumberOfItemConsumed": 1.0
}

### Example of Nutritional Values per 100 grams:

{
    "InformalFoodName": "Almond Milk, Mediterranean",
    "KiloCaloriesPerItem": 26.0,
    "WeightGramsPerItem": 100.0,
    "CarbohydrateGramsPerItem": 0.4,
    "FiberGramsPerItem": 0.4,
    "FatGramsPerItem": 1.1,
    "ProteinGramsPerItem": 0.5,
    "NumberOfItemConsumed": 1.0
}
"""

class OpenAIClient:
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')

    def get_nutritional_info(self, image_files):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ]
        # Add each image as a base64 encoded string to the messages
        for image_path in image_files:
            base64_image = encode_image(image_path)
            messages[0]["content"].append(
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                    }
                }
            )
        payload = {
            "model": "gpt-4-vision-preview",
            "messages": messages,
            "max_tokens": 300
        }
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        print(f'\n********\n* {image_files}\n********\n')
        print(response.json())
        message_text = response.json()['choices'][0]['message']['content'].replace('```json\n', '').replace('\n```', '')
        if message_text.endswith('%'):
            message_text = message_text[:-1]
        print(message_text)
        # ChatGPT response may contain a comment at the end of the line. Let's remove this!
        message_text = re.sub(r'//.*$', '', message_text, flags=re.MULTILINE)
        result = json.loads(message_text)
        return result
