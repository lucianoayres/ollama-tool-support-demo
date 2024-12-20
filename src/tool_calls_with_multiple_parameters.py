import ollama

response = ollama.chat(
    model='llama3.2',
    messages=[
        {
            'role': 'user',
            'content': 'What is the weather today in Paris?'
        }
    ],
    stream=False,
    tools=[
        {
            'type': 'function',
            'function': {
                'name': 'get_current_weather',
                'description': 'Get the current weather for a location',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'location': {
                            'type': 'string',
                            'description': 'The location to get the weather for, e.g., San Francisco, CA'
                        },
                        'format': {
                            'type': 'string',
                            'description': "The format to return the weather in, e.g., 'celsius' or 'fahrenheit'",
                            'enum': ['celsius', 'fahrenheit']
                        }
                    },
                    'required': ['location', 'format']
                }
            }
        }
    ]
)

print('Response:')
print(response['message'])

print('\nTool Calls Response:')
print(response['message']['tool_calls'])
