---
sidebar_position: 1
---

# Typescript/Javascript

1. go to account settings and create an API Key for CLI&nbsp; [open](http://google.com)
2. copy the api key somewhere safe, it will be required in subsequent step
3. start sending data using one of the following methods

## Setup using typescript/javascript

```tsx title="setup.ts"
const BASE_URL = 'https://api.xleaplabs.com';
const API_KEY = '<********* private key from dashboard>'; // should be private

const response = await fetch(`${BASE_URL}/v1/api/data`, {
  method: 'POST',
  headers: {
    'Authorization': `API_KEY ${API_KEY}`,
    'content-type': 'application/json',
  },
  body: JSON.stringify({
    question: '<Your question or prompt template with {context_var}>',
    answer: '<llm response as text or stringified json>',
    contexts: ['<array of strings sent to the llm model as key value pair>', 'context_var: this is sample context'],
    ground_truths: [],
    tags: {
      key: 'value',
      version: 1,
      env: 'prod',
      client: 'cli/web/runner',
    },
  }),
});

console.log(response);
```
