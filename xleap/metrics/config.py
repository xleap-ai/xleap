from dataclasses import dataclass


@dataclass(frozen=True)
class XleapMetricConfig:
    batch_size = 16

    prompt_column: str = "prompt"

    response_column: str = "response"

    reference_corpus: str = "abc"

    rouge_type = "rouge1"

    sentiment_lexicon: str = "vader_lexicon"
    topic_model_path: str = "MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7"
    topic_classifier: str = "zero-shot-classification"
    toxicity_model_path: str = "martin-ha/toxic-comment-model"
    transformer_name: str = "sentence-transformers/all-MiniLM-L6-v2"


config = XleapMetricConfig()
