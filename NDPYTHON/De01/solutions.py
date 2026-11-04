# Dap an De 01 - NDPYTHON

def max_num(lst):
    nums=[x for x in lst if isinstance(x,(int,float)) and not isinstance(x,bool)]; return max(nums) if nums else None
def is_prime(n):
    return n>=2 and all(n%i for i in range(2,int(n**0.5)+1))
if __name__ == "__main__":
    lst=[100,"apple",3.14,"banana",200,None]
    print(max_num(lst)); print([str(x) for x in lst])
    s=input("Nhap chuoi so: "); print(sum(int(c) for c in s if c.isdigit() and int(c)%2==1))
    s=input("Nhap chuoi so: "); print(sum(1 for a,b in zip(s,s[1:]) if a.isdigit() and b.isdigit() and int(a)+int(b)==10))
    person=("Binh",23,"Hanoi"); ten,tuoi,que=person; print(f"{ten} - {tuoi} - {que}")
    matrix=((1,2,3),(4,5,6),(7,8,9)); print(sum(sum(row) for row in matrix))
