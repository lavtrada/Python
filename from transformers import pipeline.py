from transformers import pipeline

# Load a summarization pipeline
summarizer = pipeline("summarization")

# Function to read text from a file
def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

# Summarization function
def summarize_text(file_path, max_length=100, min_length=25):
    text = read_file(file_path)  # Read the file content
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']

# File path to your text file
file_path = "Increase_the Number_of_Trees"  # Replace with the path to your text file

# Generate the summary
summary = summarize_text(file_path)

# Print the summary
print("Summarized Text:\n", summary)
