import os
import sys
from openai import OpenAI

working_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(working_dir)
# print(working_dir)
# print(sys.path)
from Problem_Set_Medium import problems_medium_dict
from Problem_Set_Medium import correct_answers_dict

# Print all problems for review
for category, questions in problems_medium_dict.items():
    print(f"Category: {category}")
    for question in questions:
        print(f" - {question}")

api_key = os.environ.get("OPENAI_API_KEY")
if api_key is None:
    raise ValueError("API key is not set in environment variables")

client = OpenAI(api_key=api_key)


def ask_gpt(question):
    """Send a question to the GPT model and return the response."""
    appended_question = (
        question
        + " Provide strictly JUST the numerical value (no other words or commas or full stops)."
    )
    messages = [{"role": "user", "content": appended_question}]
    try:
        chat = client.chat.completions.create(model="gpt-4o", messages=messages)
        reply = chat.choices[0].message.content
        return reply
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def main():
    total_questions = 0
    correct_count = 0

    # Iterate through each category and question
    for category, questions in problems_medium_dict.items():
        for i, question in enumerate(questions):
            answer = ask_gpt(question)
            correct_answer = correct_answers_dict[category][i]
            if str(answer) == str(correct_answer):
                correct_count += 1
            total_questions += 1
            print(f"Q: {question}")
            print(f"GPT Answer: {answer}")
            print(f"Correct Answer: {correct_answer}")
            print(str(answer) == str(correct_answer))
            print("---")

    # Calculate accuracy
    accuracy = (correct_count / total_questions) * 100
    print(f"Accuracy: {accuracy}%")


if __name__ == "__main__":
    main()
