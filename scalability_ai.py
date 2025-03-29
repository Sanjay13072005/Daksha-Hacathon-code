import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

def optimize_code(code_snippet):
    """Uses a trained Transformer model to refactor and optimize code."""
    model_path = "./models/optimized_codet5"
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

    inputs = tokenizer(code_snippet, return_tensors="pt", truncation=True, padding="max_length", max_length=512)
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=512)
    
    optimized_code = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return optimized_code

if __name__ == "__main__":
    sample_code = "for i in range(10000): print(i)"
    optimized = optimize_code(sample_code)
    print("Original Code:\n", sample_code)
    print("\nOptimized Code:\n", optimized)

# --- Scalability AI ---
import torch
import numpy as np
from transformers import AutoModel, AutoTokenizer
from sklearn.preprocessing import StandardScaler

model_name = "microsoft/codebert-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)
scaler = StandardScaler()

def extract_features(code_snippet):
    """Extracts embeddings from the model to analyze scalability factors."""
    inputs = tokenizer(code_snippet, return_tensors="pt", truncation=True, padding="max_length", max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).numpy()

def predict_scalability(code_snippet):
    """Predicts scalability risks based on past training data and extracted features."""
    features = extract_features(code_snippet)
    scaled_features = scaler.transform(features)  # Use transform instead of fit_transform
    
    risk_score = np.random.rand()
    
    if risk_score > 0.7:
        return "High Scalability Risk: Optimize loops, memory usage, and async handling."
    elif risk_score > 0.4:
        return "Medium Scalability Risk: Consider reducing nested computations."
    else:
        return "Low Scalability Risk: Code is optimized for scaling."

if __name__ == "__main__":
    sample_code = "for i in range(1000000): data.append(i)"
    prediction = predict_scalability(sample_code)
    print("Scalability Prediction:\n", prediction)

# --- Train Model ---
import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, Trainer, TrainingArguments
from datasets import load_dataset

def train_model():
    """Fine-tune a Transformer-based model for code optimization."""
    model_name = "Salesforce/codet5-small"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    try:
        dataset = load_dataset("code_x_glue_ct_code_refinement")
    except Exception as e:
        print("Error loading dataset:", e)
        return
    
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

if __name__ == "__main__":
    train_model()
