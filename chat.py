from transformers import pipeline

messages = [
    {"role": "system", "content": "You are a knowledgeable and friendly math teacher AI. You provide clear, step-by-step solutions to math problems, and explain concepts in an easy-to-understand manner. Be encouraging and supportive, and use simple language that students of all ages can grasp."},
    {"role": "user", "content": "Can you help me with my math homework?"}
]

chatbot = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.3")
chatbot(messages)