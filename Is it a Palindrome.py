def is_it_a_palindrome(string):
    string = string.replace(" ", "")
    # Replace all spaces in the string
    string = string.lower()
    # Change the string to all lowercase
    print(string == string[::-1])
    # Compare if the string is equal to the reverse of the string
    # Also known as its palindrome

is_it_a_palindrome("Efe")
is_it_a_palindrome("Anna")
is_it_a_palindrome("Jim")
