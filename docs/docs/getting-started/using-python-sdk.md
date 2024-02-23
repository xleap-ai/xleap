---
sidebar_position: 2
---

# xleap's python sdk

1. go to account settings and create an API Key for CLI&nbsp; [open](http://google.com)
2. copy the api key somewhere safe, it will be required in subsequent step
3. start sending data using one of the following methods

## install python sdk

```shell
pip install xleap
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
