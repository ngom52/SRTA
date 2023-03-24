import openai
import os

#Solution for SSL Certificate Error caused by Zscaler VPN
os.environ['REQUESTS_CA_BUNDLE'] = 'Zscaler Root CA.crt'

openai.api_key = "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"

model_engine = "text-davinci-003"
prompt = "Generate list of root causes for high condenser vacuum pressure and high vacuum pump motor current in a power plant"

completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5
)

response = completion.choices[0].text
print(prompt)
print(response)