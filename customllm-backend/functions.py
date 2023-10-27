from dotenv import dotenv_values
import openai

config = dotenv_values(".env")
openai.api_key = config["CHATGPT_KEY"]

messages = [ {"role": "system", "content": "You are a intelligent assistant."} ]

messages.append( 
    {"role": "user", "content": "explain derivatives like I'm five"}, 
) 

chat = openai.ChatCompletion.create( 
    model="gpt-3.5-turbo", messages=messages 
)
      
reply = chat.choices[0].message.content 
print(f"ChatGPT: {reply}") 
