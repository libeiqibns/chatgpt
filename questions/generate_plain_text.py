def generate_prompts():
    questions = [    
        {"role": "user", "content": "log base 4 of 1024 = ? Answer with only numbers"},
        {"role": "user", "content": "Are you sure about the answer?"}
    ]
    return questions