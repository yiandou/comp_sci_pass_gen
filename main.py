import random
import string
import requests

# Generate single random char
def rand_char():
    choices = string.ascii_letters + string.digits + string.punctuation
    
    return random.choice(choices)

password_length = int(input("Please enter the length you want your password to be:\n"))

# Generate a password of random chars
def gen_strong_pass():
    password = ""

    for i in range(password_length):
        password = password + rand_char()
    
    print(password)

gen_strong_pass()

# GET a rand word from dictionary API
def fetch_word():
    url = "https://random-word-api.herokuapp.com/word?length=4"

    response = requests.get(url)
    word = response.json()[0]

    return word

def gen_weaker_pass():
    word1 = fetch_word()
    word2 = fetch_word()
    password = word1 + word2
    return password

print(gen_weaker_pass())
