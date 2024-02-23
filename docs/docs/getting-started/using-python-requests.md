---
sidebar_position: 3
---

# python requests

1. go to account settings and create an API Key for CLI&nbsp; [open](http://google.com)
2. copy the api key somewhere safe, it will be required in subsequent step
3. start sending data using one of the following methods

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
