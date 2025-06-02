from litellm import completion
import os

os.environ["OPENAI_API_KEY"] = "sk-or-v1-d70b43df8e405559329661499661499f30b56f9e2cb9c0a08a710ee9e4dbaeaa099257"
os.environ["GEMINI_API_KEY"] = "AIzaSyB-pyZE8_zs1Vb45ml6456SpQLCRBli-e4"

def openai():
    response = completion(
        model="openai/gpt-4o",
        messages=[{ "content": "Hello, how are you?","role": "user"}]
    )

    print(response)

def gemini():
    response = completion(
        model="gemini/gemini-1.5-flash",
        messages=[{ "content": "Hello, how are you?","role": "user"}]
    )

    print(response)

def gemini2():
    response = completion(
        model="gemini/gemini-2.0-flash-exp",
        messages=[{ "content": "Hello, how are you?","role": "user"}]
    )

    print(response)

