import string


def generate_hashtag(input_string):

    input_string = ''.join(char for char in input_string if char not in string.punctuation)
    words = input_string.split()


    words = [word.capitalize() for word in words]


    hashtag = '#' + ''.join(words)


    if len(hashtag) > 140:
        hashtag = hashtag[:140]

    return hashtag

user_input = input("Введіть рядок: ")

result = generate_hashtag(user_input)

print(result)