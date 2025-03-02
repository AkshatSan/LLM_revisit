from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/deepseek-coder-1.3b-instruct", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("deepseek-ai/deepseek-coder-1.3b-instruct", trust_remote_code=True, torch_dtype=torch.bfloat16)

input_text = """#utils.py
import pandas as pd

def preprocess_data(df):
    # Step 1: Drop missing values
    df = df.dropna()
    
    # Step 2: Convert 'Name' column to lowercase
    df['Name'] = df['Name'].str.lower()
    
    # Step 3: Cap outliers in the 'Age' column
    df['Age'][df['Age'] > 100] = 100
    
    return df
Please improve this function and make it more optimized and suggest some good changes
"""
inputs = tokenizer(input_text, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=140)
print(tokenizer.decode(outputs[0]))
