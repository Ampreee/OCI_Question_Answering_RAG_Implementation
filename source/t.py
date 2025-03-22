import openai
import os
GROQ_API_KEY = os.getenv("GROQ_API_KEY")  

openai.api_key = GROQ_API_KEY
openai.api_base = "https://api.groq.com/openai/v1"

def test_groq():
    """Tests if the Groq API is working by sending a basic request."""
    try:
        response = openai.chat.completions.create(
            model="llama3-8b-8192",  # ✅ Use Groq's LLaMA 3 model
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": "Hello, how are you?"}],
            max_tokens=50,
        )
        print("✅ Groq API is working!")
        print("🤖 AI Response:", response["choices"][0]["message"]["content"])
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_groq()
