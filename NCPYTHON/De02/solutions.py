# Dap an De 02 - NCPYTHON

def reverse(s): return " ".join(s.split()[::-1])
def palindrome(s):
    t="".join(ch.casefold() for ch in s if not ch.isspace()); return t==t[::-1]
def subset(s1,s2): return s1.issubset(s2)
def squared(s): return {x*x for x in s}
def flatten_tuple(tpl):
    out=[]
    for x in tpl: out.extend(flatten_tuple(x) if isinstance(x,tuple) else (x,))
    return tuple(out)
def first_str(tpl): return next((x for x in tpl if isinstance(x,str)),None)
if __name__ == "__main__":
    print(reverse("I love Python")); print(palindrome("A man a plan a canal Panama"))
    print(subset({1,2},{1,2,3})); print(squared({1,3,4}))
    print(flatten_tuple(((1,2),(3,4,5),(6,)))); print(first_str((5,2.5,"abc",True,"xyz")))
