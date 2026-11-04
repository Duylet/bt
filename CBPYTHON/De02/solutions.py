# Dap an De 02 - CBPYTHON

def cau1a():
    y = int(input("Nhap y: ")); print("Duong" if y > 0 else "Am" if y < 0 else "Khong")
def cau1b():
    tinh = input("Nhap ten tinh: "); ma = input("Nhap ma vung: "); print(f"{tinh} có mã vùng {ma}.")
def cau2a():
    x = int(input("Nhap x: ")); y = int(input("Nhap y: ")); print(sum(n for n in range(x,y+1) if n < 0))
def cau2b():
    s = input("Nhap chuoi: "); x = int(input("Nhap x: ")); y = int(input("Nhap y: ")); print(sum(ch in "aeiouAEIOU" for ch in s[x-1:y]))
def cau3a():
    lst=[100,"apple",3.14,"banana",200,None]; print([v for v in lst if isinstance(v,(int,float)) and not isinstance(v,bool)])
def cau3b():
    lst=[100,"apple",3.14,"banana",200,None]; print(lst.count(200)); print(lst.index("banana")); lst.insert(2,"grape"); print(lst)
def cau4a():
    empty_tuple=(); single_tuple=(5,); mixed_tuple=(10,"apple",3.14); print(empty_tuple); print(single_tuple); print(mixed_tuple)
def cau4b():
    t=(1,2,3)
    try: t[1]=9
    except TypeError as e: print(type(e).__name__)
def cau5a():
    prices={"apple":20,"banana":10,"orange":15}; print(sum(prices.values()))
def cau5b():
    prices={"apple":20,"banana":10,"orange":15}; print(max(prices,key=prices.get))
if __name__ == "__main__":
    for name in ("cau1a","cau1b","cau2a","cau2b","cau3a","cau3b","cau4a","cau4b","cau5a","cau5b"):
        print("\\n---",name.upper(),"---"); globals()[name]()
