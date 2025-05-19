import pandas as pd
from datasets import Dataset
from transformers import AutoTokenizer

MODEL_NAME = "DeepPavlov/rubert-base-cased"


df = pd.read_csv("~/Desktop/CourseWork3Kurs/data/train.csv")  #считываем данные для обучения модели

dataset = Dataset.from_pandas(df)

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)


def tokenize(batch):
	return tokenizer(
		batch["resume_text"], batch["competency"],
		truncation=True, padding="max_length", max_length=512
	)


tokenized = dataset.map(tokenize, batched=True)

tokenized = tokenized.rename_column("level", "labels")
tokenized.set_format("torch", columns=["input_ids", "attention_mask", "labels"])

tokenized.save_to_disk("~/Desktop/CourseWork3Kurs/data/tokenized_dataset") #Optional (save to file)

print("Dataset is ready for training")

