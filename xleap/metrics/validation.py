"""
Q - question
A - answer: generated_text from RAG pipeline
C - contexts: context used for generation
G - ground_truths: ground truth answer
"""
from enum import Enum

EvaluationMode = Enum("EvaluationMode", "q a qa qc gc ga qac qga qcg")
