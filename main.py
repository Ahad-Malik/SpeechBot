import json
from difflib import get_close_matches
import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()

def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data


def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)


def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]

def chat_bot():
    knowledge_base : dict = load_knowledge_base('knowledge_base.json')

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source, duration=0.2)  #     Adjust for ambient noise
                audio = recognizer.listen(source)  # Listen for the user's input
    
                text = recognizer.recognize_google(audio)
                text = text.lower()
    
            print(f"You: {text}")
    
            if text.lower() == 'quit':
                print("Exiting the program.")
                break
    
            best_match: str | None = find_best_match(text, [q["question"]     for q in knowledge_base["questions"]])
    
            if best_match:
                answer: str = get_answer_for_question(best_match,     knowledge_base)
                print(f'Bot: {answer}')
            else:
                print('Bot : I don\'t know the answer. Can you teach me?')
                new_answer: str = input('Type the answer or "skip" to skip: ')
    
                if new_answer.lower() != 'skip':
                    knowledge_base["questions"].append({"question": text,     "answer": new_answer})
                    save_knowledge_base('knowledge_base.json', knowledge_base)
                    print('Bot: Thank you! I learnt a new response!')

        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            continue


if __name__ == '__main__':
    chat_bot()