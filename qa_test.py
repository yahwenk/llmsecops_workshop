from transformers import pipeline

# Initialize the question-answering pipeline
print("Loading model... (this may take a minute on first run)")
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")
print("Model loaded successfully!\n")

# Define your context and question
context = "Hugging Face is a technology company that provides open-source NLP libraries and tools for machine learning."
question = "What does Hugging Face provide?"

# Get the answer
answer = qa_pipeline(question=question, context=context)

print(f"Question: {question}")
print(f"Answer: {answer['answer']}")
print(f"Confidence Score: {answer['score']:.4f}")