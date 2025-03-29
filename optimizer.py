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

if __name__ == "_main_":
    sample_code = "for i in range(10000): print(i)"
    optimized = optimize_code(sample_code)
    print("Original Code:\n", sample_code)
    print("\nOptimized Code:\n", optimized)