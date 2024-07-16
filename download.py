import os
from huggingface_hub import snapshot_download,login
from pathlib import Path

hf_token = "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"
login(token = hf_token)

mistral_models_path = Path('D:/mistral_models/7B-Instruct-v0.3')
mistral_models_path.mkdir(parents=True, exist_ok=True)
os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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' 

snapshot_download(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    repo_type="model",
    allow_patterns=["params.json", "consolidated.safetensors", "tokenizer.model.v3"],
    local_dir=mistral_models_path,
    force_download=True 
)