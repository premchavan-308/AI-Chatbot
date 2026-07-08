from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0.9
)

print("Choose your AI mode")
print("Press 1 for Angry mode")
print("Press 2 for Funny mode")
print("Press 3 for Sad mode")

choice = int(input("Enter your choice: "))

if choice == 1:
    mode = "You are an angry AI agent. You respond aggressively and impatiently."
elif choice == 2:
    mode = "You are a very funny AI agent. You respond with humor and jokes."
elif choice == 3:
    mode = "You are a very sad AI agent. You respond in a depressed and emotional tone."
else:
    print("Invalid choice. Defaulting to Funny mode.")
    mode = "You are a very funny AI agent. You respond with humor and jokes."

messages = [
    SystemMessage(content=mode)
]

print("\n----------- Welcome! Type 0 to exit -----------")

while True:

    prompt = input("You: ")

    if prompt == "0":
        print("Goodbye!")
        break

    messages.append(HumanMessage(content=prompt))

    try:
        response = model.invoke(messages)

        messages.append(AIMessage(content=response.content))

        print("Bot:", response.content)

    except Exception as e:
        print("Error:", e)