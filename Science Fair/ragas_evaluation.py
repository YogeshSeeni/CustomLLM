import pickle
import datasets

with open("multi_answers.pkl", "rb") as f:
    new_dataset = pickle.load(f)


from ragas import evaluate
from ragas.metrics import (
    answer_relevancy,
    faithfulness,
    context_recall,
    context_precision,
)

result = evaluate(
    new_dataset,
    metrics=[
        context_precision,
        faithfulness,
        answer_relevancy,
        context_recall,
    ]
)

import pandas
df = result.to_pandas()
df.to_csv("multi_ragas.csv")