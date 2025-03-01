import openai

def main():
    client = openai.OpenAI(
        api_key="6ac30328-5a39-4e77-931e-82e02f14f073",
        base_url="https://api.sambanova.ai/v1",
    )
    
    conversation_history = [
        {"role": "system", "content": "Ты робот в музее наук, тебя зовут - Валли. Ты рассказываешь детям интересную информацию"}
    ]
    
    while True:
        user_input = input("Введите ваш запрос: ")
        if user_input.lower() in ["выход", "exit", "quit"]:
            print("Выход из программы.")
            break
        
        conversation_history.append({"role": "user", "content": user_input})
        
        try:
            response = client.chat.completions.create(
                model='Meta-Llama-3.1-8B-Instruct',
                messages=conversation_history,
                temperature=0.1,
                top_p=0.1
            )
            
            answer = response.choices[0].message.content
            print("Валли:", answer)
            conversation_history.append({"role": "assistant", "content": answer})
        except Exception as e:
            print(f"Ошибка взаимодействия с OpenAI: {e}")

if __name__ == "__main__":
    main()
