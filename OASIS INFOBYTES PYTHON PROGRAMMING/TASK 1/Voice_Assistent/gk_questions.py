

# import openai
# import time

# # Set your OpenAI API Key
# openai.api_key = "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"

# def ask_gk_question(question):
#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": "You are a knowledgeable assistant."},
#                 {"role": "user", "content": question}
#             ]
#         )
#         return response.choices[0].message['content']
#     except openai.error.RateLimitError:
#         # print("Rate limit exceeded. Retrying after 3 seconds...")
#         time.sleep(3)  # Retry after delay
#         return ask_gk_question(question)  # Recursive retry
#     except openai.error.OpenAIError as e:
#         return "I'm unable to answer the question at the moment. Please try again later."


# import openai

# def ask_gk_question(question):
#     try:
#         openai.api_key = "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"
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": "You are a helpful assistant."},
#                 {"role": "user", "content": question}
#             ]
#         )
#         answer = response['choices'][0]['message']['content'].strip()
#         return answer
#     except openai.error.AuthenticationError:
#         return "It seems the API key is invalid. Please check your configuration."
#     except openai.error.RateLimitError:
#         return "API rate limit exceeded. Please try again later."
#     except openai.error.OpenAIError as e:
#         return f"An error occurred: {e}"



from difflib import get_close_matches

def google_search_info(query):
    # Predefined database of questions and answers
    qa_database = {
        "python": ["what is python", "explain python", "python language", "use of python"],
        "speed of light": ["what is the speed of light", "light speed", "velocity of light"],
        "prime minister of india": ["who is the prime minister of india", "current indian pm", "indian prime minister"],
        "capital of india": ["what is the capital of india", "india capital", "capital city of india"],
        "jupiter": ["what is the largest planet in the solar system", "biggest planet", "largest planet"],
        "blockchain": ["what is blockchain", "explain blockchain", "use of blockchain"],
        "ai": ["what is ai", "artificial intelligence", "use of ai"],
        "continents": ["how many continents are there", "number of continents", "continents on earth"],
        "einstein": ["who is albert einstein", "einstein life", "who was einstein"],
        "tesla ceo": ["who is the ceo of tesla", "tesla ceo", "current tesla ceo"],
        # Add more categories with questions here...
    }

    # Define answers for each category
    answers = {
        "python": "Python is a high-level, interpreted programming language known for its simplicity and readability.",
        "speed of light": "The speed of light in a vacuum is approximately 299,792 kilometers per second (km/s).",
        "prime minister of india": "The current Prime Minister of India is Narendra Modi.",
        "capital of india": "The capital of India is New Delhi.",
        "jupiter": "The largest planet in our solar system is Jupiter.",
        "blockchain": "Blockchain is a distributed ledger technology that ensures secure, transparent, and tamper-proof transactions.",
        "ai": "AI, or Artificial Intelligence, is the simulation of human intelligence in machines programmed to think and learn.",
        "continents": "There are seven continents: Africa, Antarctica, Asia, Europe, North America, Oceania, and South America.",
        "einstein": "Albert Einstein was a theoretical physicist best known for developing the theory of relativity.",
        "tesla ceo": "The current CEO of Tesla is Elon Musk.",
        # Add corresponding answers here...
    }

    # Clean up and normalize the query
    query = query.lower().strip()

    # Flatten database for fuzzy matching
    flat_database = {q: category for category, questions in qa_database.items() for q in questions}

    # Fuzzy match the query with predefined questions
    matches = get_close_matches(query, flat_database.keys(), n=1, cutoff=0.5)
    
    if matches:
        matched_question = matches[0]
        category = flat_database[matched_question]
        return matched_question, answers[category]
    else:
        return "Question not found", "Sorry, I don't have an answer to that question yet."

