import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, Trainer, TrainingArguments
from datasets import load_dataset

def train_model():
    """Fine-tune a Transformer-based model for code optimization."""
    model_name = "Salesforce/codet5-small"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    dataset = load_dataset("code_x_glue_ct_code_refinement")
    train_data = dataset["train"].map(lambda x: tokenizer(x["source"], truncation=True, padding="max_length", max_length=512), batched=True)
    eval_data = dataset["validation"].map(lambda x: tokenizer(x["source"], truncation=True, padding="max_length", max_length=512), batched=True)

    training_args = TrainingArguments(
        output_dir="./models/optimized_codet5",
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        num_train_epochs=3,
        evaluation_strategy="epoch",
        save_strategy="epoch",
        logging_dir="./logs",
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_data,
        eval_dataset=eval_data,
    )

    trainer.train()
    model.save_pretrained("./models/optimized_codet5")
    tokenizer.save_pretrained("./models/optimized_codet5")
    print("Model fine-tuning completed!")

if __name__ == "_main_":
    train_model()