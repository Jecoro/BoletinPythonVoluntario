class Peers(object):
    
# Atributo de Clase.
    list_Numbers = [-25, -10, -7, -3, 2, 4, 8, 10]

# Constructor.
    def __init__(self, int_Obj):
        self.int_Obj = int_Obj

# Método de Instancia.
    def findPeers(self):
        for i in range(len(self.list_Numbers)):
            if (self.list_Numbers[i] + self.list_Numbers[i - 1]) == self.int_Obj:
                self.i = i
                self.i_1 = (i-1)

            def __str__(self):
                    return ("Los Indices que Suman {0} son ({2}, {1}).".format(self.int_Obj, self.i, self.i_1))

if __name__ == '__main__':
    peers = Peers(0)
    peers.findPeers()
    print(str(peers))