---
sidebar_position: 1
---

# Typescript/Javascript

1. Navigate to [_**Account Settings**_](http://app.xleaplabs.com/settings/api_keys) and generate an API Key for CLI
   usage.
2. Securely store your API Key. You'll need it for future steps.
3. Start sending data using JS/TS as documented next

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
