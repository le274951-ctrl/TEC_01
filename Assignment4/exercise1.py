def is_valid_course_code(code):
    if len(code) != 6:
        return False

    if not code[:3].isalpha():
        return False

    if not code[:3].isupper():
        return False

    if not code[3:].isdigit():
        return False

    return True


code = input("Enter course code: ")
print(is_valid_course_code(code))