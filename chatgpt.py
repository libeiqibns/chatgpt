from openai import OpenAI
import questions
import questions.generate_plain_text
import questions.generate_text_and_vision

client = OpenAI()

messages = [
    {"role": "system", "content": "You are a kind helpful assistant."}
]

prompts = list(dict())
prompts.extend(questions.generate_plain_text.generate_prompts())
prompts.extend(questions.generate_text_and_vision.generate_prompts('images', 'image_texts'))

i=0

while i < len(prompts):
    messages.append(prompts[i])
    chat = client.chat.completions.create(
        model="gpt-4o",
        messages = messages
    )
    reply = chat.choices[0].message.content
    # print(f"User: {prompts[i]['content']}")
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})
    i = i + 1
