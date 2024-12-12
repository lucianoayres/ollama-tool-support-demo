import ollama


def simplify_tool_call_response(response):
    """
    Simplifies the Ollama tool call response by extracting relevant information.

    Args:
        response: The Ollama model response dictionary.

    Returns:
        None. Prints the simplified tool call responses.
    """

    if "tool_calls" in response["message"]:
        for tool_call in response["message"]["tool_calls"]:
            function_name = tool_call["function"]["name"]
            arguments = tool_call["function"]["arguments"]

            if function_name == "get_current_weather":
                if "city" in arguments:
                    city = arguments["city"]
                    print(f"Weather for {city} has been requested via tool call!")
                else:
                    print(f"Error: Missing 'city' parameter in {function_name} call")
            else:
                print(f"Unexpected function call: {function_name}")
    else:
        print("Error: No 'tool_calls' found in the Ollama response")


response = ollama.chat(
    model="llama3.2",
    messages=[{"role": "user", "content": "What is the weather in Toronto?"}],
    tools=[
        {
            "type": "function",
            "function": {
                "name": "get_current_weather",
                "description": "Get the current weather for a city",
                "parameters": {
                    "type": "object",
                    "properties": {"city": {"type": "string", "description": "The name of the city"}},
                    "required": ["city"],
                },
            },
        },
    ],
)

print("Response:")
print(response["message"])

print("\nTool Call Response:")
simplify_tool_call_response(response)