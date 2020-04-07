name = "aDA loveLAce"
print(name.title())

# Change a string to all uppercase or all lowercase letters
name = "Ada Lovelace"
print(name.upper())
print(name.lower())

# Combining or Concatenating Strings

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")

# Adding Whitespace to Strings with Tabs or Newlines
print("Languages:\n\tPython\n\tC\n\tJavaScript")
# >>>> Stripping Whitespace
favorite_language = '  python '
print('|' + favorite_language + '|')
print('|' + favorite_language.rstrip() + '|')
print('|' + favorite_language.lstrip() + '|')
print('|' + favorite_language.strip() + '|')
