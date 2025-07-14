import re

def is_palindrome(s):
  """Checks if a string is a palindrome."""
  s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
  return s == s[::-1]
