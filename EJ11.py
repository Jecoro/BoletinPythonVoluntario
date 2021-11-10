class Circulo: #<-- Clase
  def __init__(self, radio, diametro): #<-- Constructor
    self.radio=radio
    self.diametro=diametro
  def calcularArea(self): #<-- 1er Metodo
    pi = 3.14
    return (self.radio**2)*pi #<-- Operacion ** significa elevado
  def calcularPeri(self): #<-- 2do Metodo
    pi = 3.14
    return self.diametro*pi
  radio=float(input("Ingrese el valor del radio: "))
  diametro=float(input("Ingrese el valor del diámetro: "))
  cir=Circulo(radio,diametro) # objeto cir llamando a la clase
  area=cir.calcularArea() # objeto area que llama al 1er metodo
  perimetro=cir.calcularPeri() #objeto perimetro que llama al 2do metodo
  print("El area del círculo es: ",area)
  print("El perimetro del círculo es: ",perimetro)
