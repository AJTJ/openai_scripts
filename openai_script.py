import instructor
from pydantic import BaseModel
from openai import OpenAI



class UserInfo(BaseModel):
  name: str
  age: int

# we create the schema
# to be able to validate the response

# print(UserInfo.model_json_schema())

# Patch the OpenAI client
client = instructor.from_openai(OpenAI(api_key=OPENAI_API_KEY))

# help(OpenAI)

# All this does is format the data for me
user_info = client.chat.completions.create(
  model="gpt-3.5-turbo",
  response_model=UserInfo,
  messages=[{"role": "user", "content": "John Doe is 30 years old."}],
)

print(user_info)