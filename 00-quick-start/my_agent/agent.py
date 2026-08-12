import os
from dotenv import load_dotenv
load_dotenv()

import logging
from strands import Agent, tool
from strands_tools import calculator, current_time

# Enables Strands debug log level
# logging.getLogger("strands").setLevel(logging.DEBUG)

# Sets the logging format and streams logs to stderr
logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler()]
)


# Define a custom tool using the @tool decorator
@tool
def letter_counter(word: str, letter: str) -> int:
    """Count occurrences of a specific letter in a word."""
    if not isinstance(word, str) or not isinstance(letter, str):
        return 0
    if len(letter) != 1:
        raise ValueError("Must be a single character")
    return word.lower().count(letter.lower())

# Create agent with built-in + custom tools
agent = Agent(tools=[calculator, current_time, letter_counter])

message = """
1. What is the time right now?
2. Calculate 3111696 / 74088
3. How many R's in "strawberry"?
"""
agent(message)

# Interactive console loop
print("Agent ready! Type 'quit' or 'exit' to stop.\n")
while True:
    user_input = input("You: ").strip()
    if user_input.lower() in ("quit", "exit"):
        print("Goodbye!")
        break
    if not user_input:
        continue
    print()
    agent(user_input)
    print()
