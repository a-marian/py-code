def is_palindrome(sentence):
    # Compare characters from both ends
    left, right = 0, len(sentence)-1
    while left <= right:
        if sentence[left] != sentence[right]:
            return False
        left += 1
        right -= 1
    return True


def is_palindrome(sentence):
    if not isinstance(sentence, str):
        return False
    # Keep only alphanumeric characters and ignore case
    cleaned = ''.join(c.lower() for c in sentence if c.isalnum())
    return cleaned == cleaned[::-1]
