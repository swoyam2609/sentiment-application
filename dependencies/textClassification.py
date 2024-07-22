# importing the necessary dependencies
from transformers import pipeline

#invoking the sentiment analysis model from hugging face
classifier = pipeline(
    model="lxyuan/distilbert-base-multilingual-cased-sentiments-student", 
    return_all_scores=True
)


# function from carrying out sentiment analysis
def predict(input: str):
    return classifier(input)