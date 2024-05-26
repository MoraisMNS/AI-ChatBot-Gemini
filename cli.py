import sys
from configparser import ConfigParser
from chatbot import ChatBot

def main():
    config = ConfigParser()
    config.read('credentials.ini')
    api_key = config['gemini_ai']['API_KEY']

    chatbot = ChatBot(api_key=api_key)
    chatbot.start_conversation()
    # chatbot.clear_conversation()

    print("Welcome to the JJ Gemini Chatbot CLI.Type 'quit' to exit.")

    # print('{0}:{1}'.format(chatbot.CHATBOT_NAME,chatbot.history[-1]['text']))
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
          #  print("Existing ChatBot CLI...")
            sys.exit("Existing ChatBot CLI...")

        try:
            response = chatbot.send_prompt(user_input)
            print(f"{chatbot.CHATBOT_NAME}:{response}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()          