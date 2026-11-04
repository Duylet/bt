# Dap an De 01 - CBPYTHON
# Chay tung cau doc lap; nhung cau co input() se nhan du lieu tu ban phim.

def cau1a():
    x = float(input("Nhap x: "))
    print("Chan" if x.is_integer() and int(x) % 2 == 0 else "Le")

def cau1b():
    ten = input("Nhap ten: "); tuoi = input("Nhap tuoi: ")
    print(f"Xin chào {ten}, bạn {tuoi} tuổi.")

def cau2a():
    x = int(input("Nhap x: ")); y = int(input("Nhap y: "))
    print(sum(n for n in range(x, y + 1) if n % 2 == 0))

def cau2b():
    s = input("Nhap chuoi: "); x = int(input("Nhap x: ")); y = int(input("Nhap y: "))
    print(sum(ch.isdigit() for ch in s[x-1:y]))

def cau3a():
    lst = [100, "apple", 3.14, "banana", 200, None]
    print([v for v in lst if isinstance(v, str)])

def cau3b():
    lst = [100, "apple", 3.14, "banana", 200, None]
    lst.append("orange"); print(lst)
    lst.remove(3.14); print(lst)
    lst.reverse(); print(lst)

def cau4a():
    t = ("apple", "banana", "cherry", "date", "coc")
    print(t[0]); print(t[2]); print(t[-1])

def cau4b():
    t1 = (1, 2); t2 = (3, 4)
    print(t1 + t2); print(t1 * 3)

def cau5a():
    s = "hello world"; d = {}
    for ch in s: d[ch] = d.get(ch, 0) + 1
    print(d)

def cau5b():
    scores = {"An": 8, "Binh": 6, "Cuong": 9, "Dung": 5, "Hoa": 8}
    print([name for name, score in scores.items() if score >= 8])

if __name__ == "__main__":
    for name in ("cau1a","cau1b","cau2a","cau2b","cau3a","cau3b","cau4a","cau4b","cau5a","cau5b"):
        print("\\n---", name.upper(), "---"); globals()[name]()
