---
sidebar_position: 2
---

# xLeap's python sdk

1. Navigate to [_**Account Settings**_](http://app.xleaplabs.com/settings/api_keys) and generate an API Key for CLI
   usage.
2. Securely store your API Key. You'll need it for future steps.
3. Start sending data using python SDK as documented next

## install python sdk

```shell
pip install xLeap
```

## start using sdk

```python title="setup.py"
from xleap.client import DataPointCreate, XleapApi

API_KEY = "<********* private key from dashboard>"  # should be private

client = XleapApi(api_key=API_KEY)

response = client.create_data_point_create(
    DataPointCreate(
        **{
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
    )
)


print(response)
```
