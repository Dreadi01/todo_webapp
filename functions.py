FILEPATH = 'todos.txt'


def remove_first_word(sentence):
    # Split the sentence into words using whitespace as the delimiter
    words = sentence.split()

    # Remove the first word (if any)
    if words:
        del words[0]

    # Join the remaining words back into a sentence
    return ' '.join(words)


def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def set_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
