import openai
import yaml
from openai import OpenAI


# Set your OpenAI API key
openai.api_key = "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"

api_key= "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"

#def generate_response(prompt):
#    # Call the OpenAI API to generate a response based on the prompt
#    response = openai.Completion.create(
#        model="text-davinci-003",  # Choose the language model
#        prompt=prompt,
#        max_tokens=1024,
#        n=1 # Adjust as needed
#    )
#    return response.choices[0].text
client = OpenAI(
    # This is the default and can be omitted
    api_key= api_key,
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)



text = f"""
You should express what you want a model to do by \ 
providing instructions that are as clear and \ 
specific as you can possibly make them. \ 
This will guide the model towards the desired output, \ 
and reduce the chances of receiving irrelevant \ 
or incorrect responses. Don't confuse writing a \ 
clear prompt with writing a short prompt. \ 
In many cases, longer prompts provide more clarity \ 
and context for the model, which can lead to \ 
more detailed and relevant outputs.
"""
prompt = f"""
Summarize the text delimited by triple backticks \ 
into a single sentence.
```{text}```
"""
#response = generate_response(prompt)
#print(response)
