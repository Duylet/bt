# Dap an De 01 - NCPYTHON

def camel_case(s):
    words=s.split(); return (words[0].lower()+''.join(w[:1].upper()+w[1:] for w in words[1:])) if words else ''
def longest_word(s):
    words=s.split(); return max(words,key=len) if words else ''
def operations(s1,s2): return (s1|s2,s1&s2,s1-s2)
def unique(s): return set(s)
def odd_elements(tpl): return tuple(x for x in tpl if x%2)
def tuple_stats(tpl): return (sum(tpl)/len(tpl),sum(tpl)) if tpl else (0,0)
if __name__ == "__main__":
    print(camel_case("hello world python"))
    print(longest_word("I am learning Python programming"))
    print(operations({1,2,3,4},{3,4,5,6}))
    print(unique("banana"))
    print(odd_elements((2,3,5,8,9,12,13)))
    print(tuple_stats((2.5,3.5,7.0,6.0)))
