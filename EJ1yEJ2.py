class Romans():
    """docstring for Romanos"""
    def __init__(self):
        self.eq = [("M",1000), ("CM", 900), ("D", 500), ("CD", 400), ("C", 100), ("XC", 90),
        ("L", 50), ("XL", 40), ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)]
        self.dic = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I": 1}
 
    def to_roman(self, n):
        ans = ""
        for r,d in self.eq:
            for i in range(0,3):
                if n >= d:
                    ans += r
                    n -= d
                else: break
        return ans
 
    def to_decimal(self, rom):
        ans = 0
        last = 0
        for c in rom:
            if (last > 0) and (last < self.dic[c]):
                ans += self.dic[c] - last
                last = 0
            else:
                ans += last
                last = self.dic[c]
        return ans+last
 

 

 
prueba = Romans()
print(prueba.to_roman(39))
print(prueba.to_decimal('XXXIX'))

