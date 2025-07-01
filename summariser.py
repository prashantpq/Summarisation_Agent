from transformers import pipeline

def summarise_text_local(text):
    summariser = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", device=0)  # Uses GPU if available
    summary = summariser(text, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
    
    formatted_summary = f"**Summary:**\n{summary}"
    return formatted_summary
