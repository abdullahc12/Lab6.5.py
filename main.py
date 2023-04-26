#Q1
def common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common = list(set1.intersection(set2))
    return common
#Q2
def find_palindromes(strings):
    palindromes = []
    for string in strings:
        if string == string[::-1]:
            palindromes.append(string)
    return palindromes
#Q3
def find_primes(numbers):
    primes = []
    is_prime = [True] * (max(numbers) + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, len(is_prime)):
        if is_prime[i]:
            for j in range(i * i, len(is_prime), i):
                is_prime[j] = False
    for number in numbers:
        if is_prime[number]:
            primes.append(number)
    return primes
#Q4
def anagrams(word, word_list):
    word_chars = sorted(word.lower().replace(" ", ""))
    final_list = []
    for x in word_list:
        x_chars = sorted(x.lower().replace(" ", ""))
        if x_chars == word_chars:
            final_list.append(x)
    return final_list