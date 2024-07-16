import os
from langchain_community.llms.ctransformers import CTransformers
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

model_id = 'mistralai/Mistral-7B-Instruct-v0.3'
os.environ['XDG_CACHE_HOME'] = './model/cache'
os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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' 

config = {'temperature': 0.00, 'context_length': 4000}
print("test1")

llm = CTransformers(model=model_id, model_type="mistral", config=config, callbacks=[StreamingStdOutCallbackHandler()])
print("test2")

llm("Hello I'm kaif, write an article on internet")

print("Hugging Face Token:", os.getenv('HUGGINGFACEHUB_API_TOKEN'))
print("Hugging Face Token:", os.getenv('XDG_CACHE_HOME'))
