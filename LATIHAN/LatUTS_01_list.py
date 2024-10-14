def derajat(operator):
    if operator == '+' or operator == '-':
        return 1
    if operator == '*' or operator == '/':
        return 2
    elif operator == '^':
        return 3
    return 0

def infiks_to_prefiks(infiks):
    stack = []
    prefiks = ''
    for char in infiks[::-1]: 
        if char.isalnum():  
            prefiks += char
        else:  
            if char != ' ':
                if char == ')':
                    stack.append(char)
                elif char == '(':
                    while len(stack) > 0 and stack[-1] != ')':
                        prefiks += stack.pop()
                    stack.pop()
                else:
                    while len(stack) > 0 and derajat(stack[-1]) > derajat(char):
                        prefiks += stack.pop()
                    stack.append(char)
             
    while len(stack) > 0:
        prefiks += stack.pop()
    return prefiks[::-1]

# Contoh penggunaan
infiks = "A - B ^ C / (D * (E + F))"
prefiks = infiks_to_prefiks(infiks)
print("Infiks: ", infiks)
print("Prefiks: ", prefiks)