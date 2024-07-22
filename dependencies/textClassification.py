from transformers import pipeline

classifier = pipeline(
    model="lxyuan/distilbert-base-multilingual-cased-sentiments-student", 
    return_all_scores=True
)

def predict(input: str):
    return classifier(input)