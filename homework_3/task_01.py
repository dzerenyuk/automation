user_string = "a text is divided by two parts"
# we assume that word is ended if space is entered, last word is entered
# without space thus we add 1 to the total
print(f"Total number words in string '{user_string}' is "
      f"{user_string.count(' ') + 1}")

