---
sidebar_position: 3
---

# Python requests

1. Navigate to [_**Account Settings**_](http://app.xleaplabs.com/settings/api_keys) and generate an API Key for CLI
   usage.
2. Securely store your API Key. You'll need it for future steps.
3. Start sending data using python as documented next

```python title="setup.py"
import requests

BASE_URL = "https://api.xleaplabs.com"
API_KEY = "<********* private key from dashboard>"  # should be private

response = requests.post(
    f"{BASE_URL}/v1/api/data",
    json={
        {
            "question": "<Your question or prompt template with {context_var}>",
            "answer": "<llm response as text or stringified json>",
            "contexts": [
                "<array of strings sent to the llm model as key value pair>",
                "context_var: this is sample context",
            ],
            "ground_truths": [],
            "tags": {
                "key": "value",
                "version": 1,
                "env": "prod",
                "client": "cli/web/runner",
            },
        }
    },
    headers={
        "Authorization": f"API_KEY {API_KEY}",
        "content-type": "application/json",
    },
)

print(response)
```

A new blog post is now available at [http://localhost:3000/blog/greetings](http://localhost:3000/blog/greetings).
