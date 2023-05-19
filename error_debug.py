# Define a new function to encode the prompt
def generate_prompt(repository: str, pulls: str, readme: str, commits: str, release_notes: str) -> str:
  prompt = f"Below is the repository name, pull request messages, commit messages, and release notes.\n\n### Product and Description:\n{repository}: {pulls}: {commits}: {release_notes}\n\n### Readme:\n{readme}"
  return prompt

def encode_prompt(prompt, max_length=256):
    encoded = tokenizer.encode_plus(prompt, truncation=True, padding=True, max_length=max_length)
    return {'input_ids': encoded['input_ids'], 'attention_mask': encoded['attention_mask']}

# Map the dataset using the new function
dataset = dataset.map(lambda samples: encode_prompt(generate_prompt(samples['repository'], samples['pulls'], samples['readme'], samples['commits'], samples['release_notes']), max_length=256))

# Train the model using the Trainer class
trainer = transformers.Trainer(
    model=model, 
    train_dataset=dataset,
    args=transformers.TrainingArguments(
        per_device_train_batch_size=4, 
        gradient_accumulation_steps=4,
        warmup_steps=100, 
        max_steps=100, 
        learning_rate=1e-3, 
        fp16=True,
        logging_steps=1, 
        output_dir='outputs'
    ),
    data_collator=transformers.DataCollatorForLanguageModeling(tokenizer, mlm=False)
)
model.config.use_cache = False  # silence the warnings. Please re-enable for inference!
trainer.train()



nn
# Define a new function to encode the prompt
def generate_prompt(repository: str, pulls: str, readme: str, commits: str, release_notes: str) -> str:
  prompt = f"Below is the repository name,pull request messages, commit messages and release notes.\n\n### Product and Description:\n{repository}: {pulls}: {commits}: {release_notes}\n\n### Readme:\n{readme}"
  return prompt

# def encode_prompt(prompt, max_length=512):
#   # print(encoded)
#   # encoded = tokenizer.encode(prompt, truncation=True, padding=True, max_length=max_length)
#   return {'input_ids': tokenizer.encode(prompt, truncation=True, padding=True, max_length=max_length), 'attention_mask': [1] * len(prompt)}
#   # return {'input_ids': encoded['input_ids'], 'attention_mask': encoded['attention_mask']}

def encode_prompt(prompt, max_length=512):
    encoded = tokenizer.encode_plus(prompt, truncation=True, padding=True, max_length=max_length)
    print(type(encoded))
    print(encoded)
    return {'input_ids': encoded['input_ids'], 'attention_mask': encoded['attention_mask']}



# Map the dataset using the new function
dataset = dataset.map(lambda samples: encode_prompt(generate_prompt(samples['repository'], samples['pulls'], samples['readme'], samples['commits'], samples['release_notes']), max_length=512))

# Train the model using the Trainer class
trainer = transformers.Trainer(
    model=model, 
    train_dataset=dataset,
    args=transformers.TrainingArguments(
        per_device_train_batch_size=4, 
        gradient_accumulation_steps=4,
        warmup_steps=100, 
        max_steps=100, 
        learning_rate=1e-3, 
        fp16=True,
        logging_steps=1, 
        output_dir='outputs',
        # max_length=512
        max_split_size_mb=512
    ),
    data_collator=transformers.DataCollatorForLanguageModeling(tokenizer, mlm=False)
)
model.config.use_cache = False  # silence the warnings. Please re-enable for inference!
trainer.train()