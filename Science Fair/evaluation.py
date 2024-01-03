from functions import initialize_llm, initialize_vector_database, add_text, pass_prompt_similarity
from datasets import load_dataset

fiq_eval = load_dataset("explodinggradients/fiqa", "")