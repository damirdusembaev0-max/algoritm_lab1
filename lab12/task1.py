#Задание 1
def average(a, b, c):
    return (a + b + c) / 3

#Задание 2
def is_even(n):
    return n % 2 == 0

#Задание 3
def power(a, n=2):
    return a ** n

#Задание 4
def sum_all(*args):
    return sum(args)

#Задание 5
def print_desc(n):
    if n == 0:
        return
    print(n)
    print_desc(n - 1)

print_desc(5)

#Задание 6
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

print(sum_digits(1234))  

#Задание 7
def is_palindrome(text):
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])

print(is_palindrome("level"))  

#Задание 8
def max_element(arr, index=0):
    if index == len(arr) - 1:
        return arr[index]
    
    max_rest = max_element(arr, index + 1)
    return arr[index] if arr[index] > max_rest else max_rest


print(max_element([3, 7, 2, 9, 5]))  

#Задание 9
def fast_power(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        half = fast_power(a, n // 2)
        return half * half
    else:
        return a * fast_power(a, n - 1)

print(fast_power(2, 10)) 

#Задание 10
def count_depth(n):
    if n == 0:
        return 1
    return 1 + count_depth(n - 1)

print(count_depth(5))  
