# Algos
## 1. Bubble Sort
Write a program to sort a list of numbers in ascending order, comparing and swapping two numbers at a time.
```python
[3,1,4,2]
[1,3,4,2]
[1,3,2,4]
[1,2,3,4]
```
## 2. Candies
Given the list `candies` and the integer `extra_candies`, where `candies[i]` represents the number of candies that the `ith` kid has.
For each kid, check if there is a way to distribute the `extra_candies` amount to the kids such that they can have the greatest numhber of candies among them. Notice that multiple kids can have the greatest number of candies.
```python
candies = [2,3,5,1,3]
extra_candies = 3
expected output: [True,True,True,False,True]
```
## 3. Shuffle
Given a string `s` and an integer list of `indices` of the same length, shuffle the string such that the character at the `ith` position moves to `incices[i]`.
Return the shuffled string.
```python
s = "odce"
indices = [1,2,0,3]
return "code"
```
## 4. Primes
Write a program that returns a list of all prime numbers up to a given max(inclusive).
A prime is a number that only has two factors; itself and 1.
```python
n=12
[2,3,5,7,11]
```
## 5. FizzBuzz
A classic; write a program that prints out a sequential string of numbers.
If divisible by 3, output `"Fizz`.
If divisible by 5, output `"Buzz`.
If divisible by both 3 and 5, output `FizzBuzz`.
Otherwise, print out the string.
```python
Between 1 and 5, output:
"1"
"2"
"Fizz"
"4"
"Buzz"
```
