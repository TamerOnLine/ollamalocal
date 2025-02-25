from langchain_ollama import OllamaLLM

def explain_question_mark(question):
    llm = OllamaLLM(model="mistral")
    try:
        response = llm.invoke(question)
        return response
    except Exception as e:
        return f"Fehler beim Abrufen der Antwort: {e}"

def main():
    print("Willkommen! Geben Sie Ihre Frage ein (oder 'exit' zum Beenden):")
    
    while True:
        user_input = input("\nIhre Frage: ").strip()
        
        if user_input.lower() in ["exit", "quit"]:
            print("\nProgramm beendet. Auf Wiedersehen!")
            break

        explanation = explain_question_mark(user_input)
        
        print("\nAntwort des Modells:\n")
        print(explanation)

if __name__ == "__main__":
    main()
