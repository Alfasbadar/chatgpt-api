import openai
openai.api_key="Your_api_key"
model_engine = "text-davinci-003"
prompt = "Need a help"

completion=openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1042,
    n=1,
    stop=None,
    temperature=0.5,
)
response = completion.choices[0].text
print(response)
