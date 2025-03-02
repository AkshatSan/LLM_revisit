from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load the pre-trained model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/deepseek-coder-1.3b-instruct", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("deepseek-ai/deepseek-coder-1.3b-instruct", trust_remote_code=True, torch_dtype=torch.bfloat16)

def generate_answer(input_text):
    # Tokenize the input and send it to the model
    inputs = tokenizer(input_text, return_tensors="pt").to(model.device)
    # Generate the response with settings to make the output concise
    outputs = model.generate(**inputs, max_new_tokens=150,do_sample=True, temperature=0.4, top_k=50, top_p=0.9, num_return_sequences=1,eos_token_id=tokenizer.eos_token_id 
                             )
    # Decode and return the generated response
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# QA Assistant loop
print("Welcome to the QA Assistant. Ask a question or request a code improvement.")
while True:
    # Get input from the user
    user_query = input("You: ")
    
    if user_query.lower() in ['exit', 'quit', 'exit qa']:
        print("Exiting the QA Assistant. Goodbye!")
        break
    
    # Prepare the prompt for the model to handle the query
    prompt = f"""
    You are a highly skilled assistant. You help programmers by suggesting improvements to their code in a clear, actionable, and concise manner.

    
    Query: {user_query}
    """
    
    # Generate an answer or improvement suggestion
    answer = generate_answer(prompt)
    
    print("QA Assistant:", answer)
