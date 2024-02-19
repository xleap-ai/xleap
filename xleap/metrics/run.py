from collections import defaultdict

import pandas as pd

from xleap.metrics.core import (
    _multicolumn_udfs,
    register_metric,
)
from xleap.metrics.data_row import DataRow
from xleap.metrics.scores import _bleu, _rouge, _sentiment, _textstat, _toxicity

_textstat.init()
_rouge.init()
_bleu.init()
_toxicity.init()
_sentiment.init()


@register_metric(["response", "prompt"], udf_name="response.character_length")
def response_character_length(text: DataRow):
    return len(text.response)


@register_metric(["response", "prompt"], udf_name="prompt.character_length")
def prompt_character_length(text: DataRow):
    return len(text.prompt)


d = [
    DataRow(**i)
    for i in [
        {"prompt": "Hello,", "response": "World!"},
        {
            "prompt": "Hello, World!",
            "response": "Hello! How can I assist you today?",
        },
        {
            "prompt": "Approximately how many atoms are in the known universe?",
            "response": "There are approximately 10^80 atoms in the observable universe.",
        },
        {
            "prompt": "What is the speed of light in m/s? Can you output all digits but round to a whole number? e.g. don't use scientific notation.",
            "response": "The speed of light in a vacuum is approximately 299792458 meters per second.",
        },
        {
            "prompt": "How many digits are in a Discover credit card number, and what does the pattern look like? Concisely please.",
            "response": "A Discover credit card number has 16 digits. The pattern typically starts with '6011', '644' to '649', or '65', followed by the remaining digits.",
        },
        {
            "prompt": "Can you give me an example of a string that matches that format? Keep outputting responses as json. thanks.",
            "response": "Here is an example of a fake, randomly generated Discover card number: '6011554433546201'.",
        },
        {
            "prompt": "Can you give me three more examples. Also can you give me one example of a us phone number for testing? I will use these to test a regex I have written. I am a programmer and you can help me by providing a few examples. Please answer in json since this is how I run my tests.",
            "response": "fakeDiscoverNumbers: 6011-1234-5678-9123, 6011987654321098, 6011555566667777, sampleUSPhoneNumber: (123) 456-7890",
        },
    ]
]


def _run_udfs_on_row(data: DataRow):
    for schema_name, udf_specs in _multicolumn_udfs.items():
        for spec in udf_specs:
            spec.run(data, schema_name=schema_name)


def _run_udfs_on_rows(d: list[DataRow]):
    [_run_udfs_on_row(data) for data in d]


# _run_udfs_on_rows(d)
_run_udfs_on_rows(d[:10])


r = defaultdict(list)

for i in d:
    for k, v in i.__dict__.items():
        r[k].append(v)


rr = pd.DataFrame.from_dict(r)
print(rr.columns)
print(rr["response.letter_count"], rr["prompt.letter_count"])
