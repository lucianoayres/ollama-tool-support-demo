import ollama

# Define the tools available to the model
tools = [
    {
        'type': 'function',
        'function': {
            'name': 'get_current_weather',
            'description': 'Get the current weather for a city',
            'parameters': {
                'type': 'object',
                'properties': {
                    'city': {
                        'type': 'string',
                        'description': 'The name of the city, e.g., Paris'
                    },
                    'format': {
                        'type': 'string',
                        'description': "The format to return the weather in, e.g., 'celsius' or 'fahrenheit'",
                        'enum': ['celsius', 'fahrenheit']
                    }
                },
                'required': ['city', 'format']
            }
        }
    },
    {
        'type': 'function',
        'function': {
            'name': 'find_popular_attractions',
            'description': 'Find popular tourist attractions in a city',
            'parameters': {
                'type': 'object',
                'properties': {
                    'city': {
                        'type': 'string',
                        'description': 'The name of the city, e.g., Paris'
                    },
                    'category': {
                        'type': 'string',
                        'description': "Category of attractions, e.g., 'museums', 'parks', 'historical sites'",
                        'enum': ['museums', 'parks', 'historical sites', 'restaurants', 'shopping']
                    }
                },
                'required': ['city', 'category']
            }
        }
    },
    {
        'type': 'function',
        'function': {
            'name': 'book_restaurant',
            'description': 'Book a reservation at a restaurant in a city',
            'parameters': {
                'type': 'object',
                'properties': {
                    'city': {
                        'type': 'string',
                        'description': 'The name of the city, e.g., Paris'
                    },
                    'restaurant_name': {
                        'type': 'string',
                        'description': 'The name of the restaurant to book'
                    },
                    'time': {
                        'type': 'string',
                        'description': 'The time for the reservation, e.g., "7:00 PM"'
                    },
                    'number_of_people': {
                        'type': 'integer',
                        'description': 'Number of people for the reservation'
                    }
                },
                'required': ['city', 'restaurant_name', 'time', 'number_of_people']
            }
        }
    }
]

user_message = (
    "I'm planning a day trip in Sydney and need your assistance with the details. "
    "Can you check the temperature and if it will rain today, suggest a popular tourist attraction to visit, "
    "recommend a good restaurant by name, and book a reservation for 4 people at 7 PM at that restaurant?"
)

# Initialize the Ollama chat with multiple tools for planning a day trip
response = ollama.chat(
    model='llama3.2',
    messages=[
        {
            'role': 'user',
            'content': user_message
        }
    ],
    stream=False,
    tools=tools,
)

print('Response:')
print(response['message'])

print('\nTool Calls Response:')
print(response['message']['tool_calls'])
