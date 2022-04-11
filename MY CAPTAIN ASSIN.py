Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = "aabbc"
{i: a.count(i) for i in set(a)}
{'a': 2, 'b': 2, 'c': 1}
a = "aaabbbbcccc"
{i: a.count(i) for i in set(a)}
{'a': 3, 'b': 4, 'c': 4}
