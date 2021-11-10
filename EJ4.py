class Subconjs():
    def subs(self, lista):
        l = len(lista)
        pl = (1<<l)
        ans = []
        for mask in range(0, pl):
            cmb = []
            for i in range(0, l):
                if (mask&(1<<i)) > 0:
                    cmb.append(lista[i])
            ans.append(cmb)
        return ans
 
prueba = Subconjs()
print(prueba.subs([4, 5, 6])) 