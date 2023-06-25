import openai

from config.config import settings

# Set up OpenAI API credentials
openai.api_key = settings.OPENAI_API_KEY

def compare_text_similarity(text1, text2):
     # Prepare the prompt
     prompt = f"Text 1: {text1}\nText 2: {text2}\nSimilarity percentage:"

     # Make an API request
     response = openai.Completion.create(
          engine='text-davinci-003',
          prompt=prompt,
          max_tokens=200,
          n=1,
          stop=None,
          temperature=0,
     )
     # Print the response
     #print(response)

     # Retrieve and process the response
     completion_text = response['choices'][0]['text'].strip()
     return completion_text


# Example usage
marking_scheme = "A router is a networking device that connects multiple computer networks together and directs data traffic between them by determining the optimal path for data packets"
answer_sheet = " A router is a device that links different networks, such as a home network and the internet, and manages the flow of data between them, ensuring efficient communication."

similarity_percentage = compare_text_similarity(marking_scheme, answer_sheet)

print(f"Similarity percentage: {similarity_percentage}")
