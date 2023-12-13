import openai
import os
import requests
# 只需要在python里设置代理即可
# os.environ['HTTP_PROXY'] = 'http://ip:port'
# os.environ['HTTPS_PROXY'] = 'http://ip:port'
openai.api_key = "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"

"""
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
     "model": "gpt-3.5-turbo",
     "messages": [{"role": "user", "content": "Say this is a test!"}],
     "temperature": 0.7
   }'
"""
model_engine = "davinci"
prompt = "In generate, what people is Joker"

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "what is zhihu?"},
    ]
)

print(completion)






































