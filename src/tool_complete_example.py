import ollama
import json
import time as time_module

# ----------------------------
# Mock Implementations of Tools
# ----------------------------

def get_current_weather(city, format):
    """
    Mock function to get current weather for a city.
    """
    weather_data = {
        'Sydney': {
            'temperature_celsius': 22,
            'temperature_fahrenheit': 72,
            'will_rain': False
        },
        'Paris': {
            'temperature_celsius': 18,
            'temperature_fahrenheit': 64,
            'will_rain': True
        }
        # Add more cities as needed
    }

    city_weather = weather_data.get(city, {
        'temperature_celsius': 20,
        'temperature_fahrenheit': 68,
        'will_rain': False
    })

    temperature = (
        city_weather['temperature_celsius']
        if format == 'celsius'
        else city_weather['temperature_fahrenheit']
    )
    return {
        'temperature': temperature,
        'will_rain': city_weather['will_rain']
    }

def find_popular_attractions(city, category):
    """
    Mock function to find popular tourist attractions in a city.
    """
    attractions = {
        'Sydney': {
            'museums': ['Australian Museum', 'Museum of Contemporary Art'],
            'parks': ['Hyde Park', 'Royal Botanic Garden'],
            'historical sites': ['The Rocks', 'Sydney Opera House'],
            'restaurants': ['Quay', 'Bennelong'],
            'shopping': ['Pitt Street Mall', 'Queen Victoria Building']
        },
        'Paris': {
            'museums': ['Louvre Museum', 'Musée d\'Orsay'],
            'parks': ['Luxembourg Gardens', 'Tuileries Garden'],
            'historical sites': ['Eiffel Tower', 'Notre-Dame Cathedral'],
            'restaurants': ['Le Meurice', 'L’Ambroisie'],
            'shopping': ['Champs-Élysées', 'Le Marais']
        }
        # Add more cities as needed
    }

    city_attractions = attractions.get(city, {})
    return city_attractions.get(category, [])

def book_restaurant(city, restaurant_name, time_str, number_of_people):
    """
    Mock function to book a restaurant.
    """
    confirmation = {
        'restaurant_name': restaurant_name,
        'time': time_str,
        'number_of_people': number_of_people,
        'confirmation_number': 'CONF' + str(int(time_module.time()))
    }
    return confirmation

# ----------------------------
# Define the Tools for Ollama
# ----------------------------

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
                        'description': "Category of attractions, e.g., 'museums', 'parks', 'historical sites', 'restaurants', 'shopping'",
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

# ----------------------------
# Helper Function to Generate Assistant Messages
# ----------------------------

def generate_assistant_message(tool_outputs):
    """
    Generates a natural assistant message based on tool outputs.
    """
    weather = tool_outputs.get('get_current_weather')
    attractions = tool_outputs.get('find_popular_attractions')
    reservation = tool_outputs.get('book_restaurant')
    
    messages = []
    
    if weather and 'error' not in weather:
        temp = weather['temperature']
        rain = "it will rain today." if weather['will_rain'] else "it won't rain today."
        messages.append(f"The current temperature in Sydney is {temp}°C and {rain}")
    
    if attractions and isinstance(attractions, list) and attractions:
        attractions_list = ' and '.join(attractions)
        messages.append(f"A great tourist attraction to visit is the {attractions_list}.")
    
    if reservation and 'error' not in reservation:
        restaurant = reservation['restaurant_name']
        time_res = reservation['time']
        people = reservation['number_of_people']
        confirmation = reservation['confirmation_number']
        messages.append(f"Your reservation at {restaurant} for {people} people at {time_res} has been confirmed. The confirmation number is {confirmation}.")
    
    return ' '.join(messages)

# ----------------------------
# User's Initial Message
# ----------------------------

user_message = (
    "I'm planning a day trip in Sydney and need your assistance with the details. "
    "Can you check the temperature and if it will rain today, suggest a popular tourist attraction to visit, "
    "recommend a good restaurant by name, and book a reservation for 4 people at 7 PM at that restaurant?"
)

# ----------------------------
# Initialize Conversation History
# ----------------------------

conversation_history = [
    {
        'role': 'user',
        'content': user_message
    }
]

# ----------------------------
# Function to Execute Tool Calls
# ----------------------------

def execute_tool_calls(tool_calls):
    """
    Executes the tool calls and returns their outputs.
    """
    tool_outputs = {}
    
    for tool_call in tool_calls:
        tool_name = tool_call.function.name
        parameters = tool_call.function.arguments

        print(f"\n---\nCalling tool: {tool_name} with parameters {parameters}")

        # Execute the corresponding tool
        if tool_name == 'get_current_weather':
            city = parameters.get('city')
            format = parameters.get('format')
            if not city or not format:
                tool_output = {'error': 'Missing required parameters for get_current_weather.'}
            else:
                tool_output = get_current_weather(city, format)
        
        elif tool_name == 'find_popular_attractions':
            city = parameters.get('city')
            category = parameters.get('category')
            if not city or not category:
                tool_output = {'error': 'Missing required parameters for find_popular_attractions.'}
            else:
                tool_output = find_popular_attractions(city, category)
        
        elif tool_name == 'book_restaurant':
            city = parameters.get('city')
            restaurant_name = parameters.get('restaurant_name')
            time_str = parameters.get('time')
            number_of_people = parameters.get('number_of_people')

            # Handle missing 'restaurant_name' by selecting a default
            if not restaurant_name:
                popular_restaurants = find_popular_attractions(city, 'restaurants')
                restaurant_name = popular_restaurants[0] if popular_restaurants else 'Default Restaurant'

            # Handle missing 'time' by setting a default
            if not time_str:
                time_str = '7:00 PM'

            # Ensure 'number_of_people' is an integer
            if isinstance(number_of_people, str):
                try:
                    number_of_people = int(number_of_people)
                except ValueError:
                    number_of_people = 4  # Default value

            if not city:
                tool_output = {'error': 'Missing required parameters for book_restaurant.'}
            else:
                tool_output = book_restaurant(city, restaurant_name, time_str, number_of_people)
        
        else:
            tool_output = {'error': f"Unknown tool: {tool_name}"}

        print(f"Tool output: {tool_output}")

        # Store the tool output
        tool_outputs[tool_name] = tool_output
    
    return tool_outputs

# ----------------------------
# Step 1: Send Initial Message to AI
# ----------------------------

response = ollama.chat(
    model='llama3.2',
    messages=conversation_history,
    stream=False,
    tools=tools,
)

# Extract the assistant's message and tool calls
assistant_message = response['message']['content']
print("Assistant:", assistant_message)

tool_calls = response['message'].get('tool_calls', [])

# ----------------------------
# Step 2: Execute Tool Calls and Collect Outputs
# ----------------------------

if tool_calls:
    tool_outputs = execute_tool_calls(tool_calls)

    # Generate assistant response based on tool outputs
    assistant_response = generate_assistant_message(tool_outputs)
    print("\nAssistant:", assistant_response)
    
    # Append the assistant response to the conversation history
    conversation_history.append({
        'role': 'assistant',
        'content': assistant_response
    })

    # ----------------------------
    # Step 3: Send Updated Conversation to AI
    # ----------------------------

    response = ollama.chat(
        model='llama3.2',
        messages=conversation_history,
        stream=False,
        tools=tools,
    )

    # Extract the new assistant message and tool calls
    new_assistant_message = response['message']['content']
    print("\nAssistant:", new_assistant_message)

    additional_tool_calls = response['message'].get('tool_calls', [])

    if additional_tool_calls:
        additional_tool_outputs = execute_tool_calls(additional_tool_calls)

        # Generate final assistant response
        final_assistant_response = generate_assistant_message(additional_tool_outputs)
        print("\nAssistant:", final_assistant_response)

        # Append the final assistant response to the conversation history
        conversation_history.append({
            'role': 'assistant',
            'content': final_assistant_response
        })
    elif new_assistant_message.strip():
        # If there is a new assistant message without tool calls, append it
        conversation_history.append({
            'role': 'assistant',
            'content': new_assistant_message
        })

# ----------------------------
# Final Conversation History
# ----------------------------

print("\n---\nConversation Complete.")
print(json.dumps(conversation_history, indent=2))
