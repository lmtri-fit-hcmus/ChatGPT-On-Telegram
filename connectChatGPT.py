import openai

openai.api_key = "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"

def generate_text(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message
