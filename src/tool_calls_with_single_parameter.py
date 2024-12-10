import ollama

response = ollama.chat(
    model='llama3.2',
    messages=[{'role': 'user', 'content':
        'What is the weather in Toronto?'}],
	# provide a weather checking tool to the model
    tools=[{
      'type': 'function',
      'function': {
        'name': 'get_current_weather',
        'description': 'Get the current weather for a city',
        'parameters': {
          'type': 'object',
          'properties': {
            'city': {
              'type': 'string',
              'description': 'The name of the city',
            },
          },
          'required': ['city'],
        },
      },
    },
  ],
)

print('Response:')
print(response['message'])

print('\nTool Calls Response:')
print(response['message']['tool_calls'])
