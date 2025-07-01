from summariser import summarise_text_local

if __name__ == "__main__":
    input_text = """
    Large Language Models (LLMs) have revolutionized natural language processing by enabling
    tasks such as summarisation, question answering, and generation with high accuracy. They
    are built upon transformer architectures and trained on extensive datasets, making them
    versatile for industry and research use-cases in Generative AI.
    """

    summary = summarise_text_local(input_text)
    print(summary)
