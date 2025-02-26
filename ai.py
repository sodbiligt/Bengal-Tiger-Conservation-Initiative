import openai

openai.api_key = "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"

def prompt(prompt, model="gpt-4o", max_tokens=1200, temperature=0.4):
    messages = [{"role": "user", "content": prompt}]
    try:
        response = openai.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        response_message = response.choices[0].message.content.strip()
        return response_message  # Make sure this is returned as Markdown
    except Exception as e:
        print("Error:", e)
        return "Sorry, something went wrong."
