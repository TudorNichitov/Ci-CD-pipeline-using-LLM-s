import openai
import yaml

# Set your OpenAI API key
openai.api_key = "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"

def generate_response(prompt):
    # Call the OpenAI API to generate a response based on the prompt
    response = openai.Completion.create(
        engine="text-davinci-003",  # Choose the language model
        prompt=prompt,
        max_tokens=100  # Adjust as needed
    )
    return response.choices[0].text.strip()

def modify_yaml(input_yaml, chatgpt_prompt):
    with open(input_yaml, 'r') as file:
        yaml_content = yaml.safe_load(file)

    # Send prompt to ChatGPT and get the response
    chatgpt_response = generate_response(chatgpt_prompt)

    # Modify YAML content based on ChatGPT response
    # Here, we simply add a new key-value pair to the YAML content
    new_key = "additional_key"
    new_value = chatgpt_response
    yaml_content[new_key] = new_value

    # Write the modified YAML content back to the file
    with open(input_yaml, 'w') as file:
        yaml.dump(yaml_content, file)

if __name__ == "__main__":
    input_yaml_file = "wordpress-deployment.yaml"  # Replace with your YAML file
    chatgpt_prompt = "BLABLABLA:\n"

    # Get user input to include in the prompt
    user_input = input("Scale up the application")
    chatgpt_prompt += user_input

    # Modify the YAML file based on user input and ChatGPT response
    modify_yaml(input_yaml_file, chatgpt_prompt)

    print("YAML file modified successfully.")
