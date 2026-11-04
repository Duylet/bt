# Dap an De 02 - NDPYTHON

def get_strs(lst): return [x for x in lst if isinstance(x,str)]
def total_chars(lst): return sum(len(x) for x in lst if isinstance(x,str))
def is_prime(n): return n>=2 and all(n%i for i in range(2,int(n**0.5)+1))
if __name__ == "__main__":
    lst=[100,"apple",3.14,"banana",200,None]; print(get_strs(lst)); print(total_chars(lst))
    s=input("Nhap chuoi so: "); print("".join(c for i,c in enumerate(s,1) if i%2==0))
    s=input("Nhap chuoi so: "); print(s==s[::-1])
    nums=(5,12,7,18,21,9,4); print(tuple(x for x in nums if x%3==0)); print(sum(is_prime(x) for x in nums))
