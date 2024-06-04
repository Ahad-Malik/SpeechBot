# A Simple Self-learning AI Voice Chatbot with Knowledge Base Learning

## Description

This Python script implements a basic AI chatbot capable of interacting with users through voice commands.
Have fun teaching it new responses to the questions it doesn't know and make it personalized! All yours to play around with

*Speech recognition* is used to convert spoken audio into text, while *text-to-speech* generates audio responses. 
The chatbot utilizes a *knowledge base* stored in a JSON file (`knowledge_base.json`) containing pre-defined questions and answers. 
It also incorporates *fuzzy matching* to handle slight variations in user-phrased questions.

## Key Features

* **Conversational Interface:** Enables natural interaction with users via voice and text.
* **Learning Capability:** Allows the chatbot to learn new questions and answers during user interactions.
* **Fuzzy Matching:** Handles slight variations in user-phrased questions, improving responsiveness.
* **User-Friendliness:** Guides users through the learning process and provides feedback.

## Getting Started

1. Install required libraries: `speech_recognition`, `pyttsx3`
2. Create a JSON file (`knowledge_base.json`) with example questions and answers.
3. Run the script: `python chat_bot.py`
4. Start a conversation! The chatbot will listen for your questions and provide responses.

## Further Enhancements

* Expand the knowledge base with more diverse questions and answers.
* Implement natural language processing (NLP) techniques for more sophisticated conversation handling which is my next project.
* Integrate with external APIs or data sources for broader information access.
* Improve the speech recognition and text-to-speech engine accuracy for better user experience.
