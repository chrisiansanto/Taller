#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


#ejercicio 1
nombre = input("¿cual es su nombre? ")
print(nombre, ", eres increible :D")


# In[3]:


#ejercicio 2 
numero = int(input("Ingrese un numero "))
print("su numero elevado al cuadrado es:",numero**2)


# In[4]:


#ejercicio 3
numero1 = int(input("Ingrese el primer numero que va a sumar "))
numero2 = int(input("Ingrese el segundo numero que va a sumar "))
print("El resultado de la suma de los dos numeros es:",numero1+numero2)


# In[8]:


#ejercicio 4
numero1 = int(input("Ingrese el primer numero "))
numero2 = int(input("Ingrese el segundo numero "))
print("La suma es :",numero1+numero2)
print("la resta es :",numero1-numero2)
print("la multiplicacion es :",numero1*numero2)
print("la division es :",numero1/numero2)
print("el residuo es :",numero1%numero2)


# In[1]:


#ejercicio 5
x = 5.54
a = int(x)
b = abs(x) - abs(int(x))
print(a)
print(b)


# In[ ]:


#ejercicio 6
cont = 0
p1 = 15
p2 = 20
p3 = 15
p4 = 30
p5 = 50
while cont <= 5:
    i = 0
    try:
        if cont == 1:
            nota1 = float(input("Ingresa la nota numero 1 "))
            i = nota1
        elif cont == 2:
            nota2 = float(input("Ingresa la nota numero 2 "))
            i = nota2
        elif cont == 3:
            nota3 = float(input("Ingresa la nota numero 3 "))
            i = nota3
        elif cont == 4:
            nota4 = float(input("Ingresa la nota numero 4 "))
            i = nota4
        elif cont == 5:
            nota5 = float(input("Ingresa la nota numero 5 "))
            i = nota5
        if i > 0 and i <= 5:
            cont += cont
    except:
        print("***Este valor no es valido***")
resultado = (nota*p1) + (nota2*p2) + (nota3*p3) + (nota4*p4)+ (nota5*p5)
print ("su nota definitiva es:",resultado)
if resultado >=3:
    print("Aprobo la materia con:",resultado,"FELICIDADES :D")
else:
    print("Reprobo su nota es:",resultado,"SIGUE INTENTANDO D:")


# In[10]:


#ejercicio 7
producto = int(input("¿Cual es el valor del producto sin IVA? "))
productoIVA = producto*19/100
print("IVA cantidad:",productoIVA)
print("El valor de su producto con el IVA es:",producto+productoIVA)


# In[11]:


#ejercicio 8
radio = int(input("¿Cual es el radio del circulo? "))
perimetro = 2*3.14*radio
area = 3.14*radio**2
print("El area del circulo es:",area)
print("El perimetro del circulo es:",perimetro)


# In[12]:


#ejercicio 9
lado = int(input("¿Cual es el valor de un lado? "))
apotema = int(input("¿Cual es el valor del apotema? "))
perimetro = 6*lado
area = apotema*perimetro/2
print("el area del hexagono es:",area)


# In[15]:


#ejercicio 10
nuemero1 = int(input("Ingrese el primer dato "))
nuemero2 = int(input("Ingrese el segundo dato "))
nuemero3 = int(input("Ingrese el tercer dato "))
promedio = nuemero1+nuemero2+nuemero3/3
print("Su promedio es:",promedio)


# In[17]:


#ejercicio 11
a = 12
b = 21
print("El valor de a es:",a)
print("El valor de b es:",b)
g = a
a = b
b = g
print("El valor de a es:",a)
print("El valor de b es:",b)


# In[18]:


#ejercicio 12
import math
h = float(input("Ingresa la altura "))
g = 9.8/2
t = h/g
raiz = math.sqrt(t)
t2 = raiz
print("El tiempo de caída de su objeto es:",t2)


# In[19]:


#ejercicio 17
segundos = int(input("Ingrese sus segundos: "))
minutos = segundos/60
horas = minutos/60
print("Sus segundos a horas son:",horas,"Horas")


# In[20]:


#ejercicio 18
segundos = int(input("Ingrese sus segundos: "))
minutos = segundos/60
print("Sus segundos a minutos son:",minutos,"Minutos")


# In[25]:


#ejercicio 19
segundos = int(input("Ingrese sus segundos: "))
minutos = round(segundos/60)
horas = round(minutos/60)
if segundos >=60:
    segundos = 59
if minutos>=60:
    minutos = 59
if horas>24:
    horas = 23
print(str(horas)+":"+str(minutos)+":"+str(segundos))


# In[28]:


#ejercicio 20
dinero1 = 0
dinero2 = 0 
dinero3 = 0
mil = int(input("¿Cuantos billetes de 1000 pesos tines? "))
cincoMil = int(input("¿Cuantos billetes de 5000 pesos tienes? "))
diezMil = int(input("¿Cuantos billetes de 10000 pesos tienes? "))
if mil == 0:
    print("***Ninguno de mil***")
else:
    dinero1 = mil
if cincoMil == 0:
    print("***Ninguno de cinco mil***")
else:
    dinero2 = cincoMil
if diezMil == 0:
    print("***Ninguno de diez mil***")
else:
    dinero3 = diezMil
cantidadMil = dinero1
cantidadCincoMil = dinero2*5
cantidadDiezMil = dinero3*10
print("cantidad total de mil son:",cantidadMil,"Mil")
print("canridad total de cinco mil son:",cantidadCincoMil,"Mil")
print("cantidad total de diez mil son:",cantidadDiezMil,"Mil")
cantidadTotal = cantidaMil + cantidadCincoMil + cantidadDiezMil
print("El dinero total es:",cantidadTotal,"Mil")


# In[45]:


#ejercicio 21
numero = list(input("Ingresa un número de 4 cifras: "))
numero.reverse()
numero_al_reves = ''
for elemento in numero:
     numero_al_reves += elemento 
print("***su numero invertido es***",numero_al_reves)


# In[49]:


#ejercicio 22
cantidad = int(input("Cantidad de numeros : "))
numeros = list(map(int,input("Digita los numeros  : ").strip().split()))#strip Elimine los espacios al principio y al final de la cadena y 
#split Divida una cadena en una lista donde cada palabra es un elemento de lista
def separar_numeros(lista):
    numeros.sort()#sort ordena la lista 
    pares = []#nueva lista
    impares = []#nueva lista 
    for i in lista: #verificar uno por uno par o impar
        if i % 2 == 0: 
            pares.append(i)#si es par se almacena gracias a append
        else:
            impares.append(i)#si es impar se almacena gracias a append
    return pares,impares
pares,impares = separar_numeros(numeros)
print ("Los numeros pares son: ", pares)
print ("Los numeros impares son: ", impares)
print("La cantidad de numeros son: ",len(numeros))#len cuanta cuanta es la cantidad elementos en una lista
print ("La lista es:",numeros)


# In[47]:


#ejercicio 23
numero = int(input("Ingrese su numero "))
if numero>0:
    print("su numero es positivo")
else:
    print("su numero es negativo")


# In[5]:


#ejercicio 24
numeros = list(map(int,input("Digita los numeros  : ").strip().split()))
def separar_numeros(lista):
    numeros.sort()#sort ordena la lista 
    pares = []#nueva lista
    impares = []#nueva lista 
    for i in lista: #verificar uno por uno par o impar
        if i % 2 == 0: 
            pares.append(i)#si es par se almacena gracias a append
        else:
            impares.append(i)#si es impar se almacena gracias a append
    return pares,impares
def positivos_negativos(lista):
    numeros.sort()#sort ordena la lista 
    positivo = []#nueva lista
    negativo = []#nueva lista 
    for n in lista:
        if n>0:
            positivo.append(n)
        else:
            negativo.append(n)
    return negativo,positivo
pares,impares = separar_numeros(numeros)
print ("Los numeros pares son: ", pares)
print ("Los numeros impares son: ", impares)
print("La cantidad de numeros son: ",len(numeros))#len cuanta cuanta es la cantidad elementos en una lista
print ("La lista es:",numeros)
print("Los negativos son:",negativo)
print("Los positivos son:",positivo)


# In[9]:


#ejercicio 25
producto = int(input("¿Cual es el valor del producto sin IVA? "))
productoIVA = producto*19/100
IVA = producto+productoIVA
if IVA >= 15000:
    descuento = IVA*5/100
    IVA = IVA-descuento
    print("TIENES DESCUENTO AHORA VALE:",descuento,":D")
print("IVA cantidad:",productoIVA)
print("El valor de su producto con el IVA es:",IVA)


# In[2]:


#ejercicio 26
numero = int(input("Escriba un numero: "))
if numero <=10:
    numero =numero*3
    print("el triple del numero es:",numero)
else:
    numero = numero/4
    print("La cuarta parte es:",numero)


# In[ ]:


#ejercicio 27
cont = 0
p1 = 15
p2 = 20
p3 = 15
p4 = 30
p5 = 50
while cont <= 5:
    i = 0
    try:
        if cont == 1:
            nota1 = float(input("Ingresa la nota numero 1 "))
            i = nota1
        elif cont == 2:
            nota2 = float(input("Ingresa la nota numero 2 "))
            i = nota2
        elif cont == 3:
            nota3 = float(input("Ingresa la nota numero 3 "))
            i = nota3
        elif cont == 4:
            nota4 = float(input("Ingresa la nota numero 4 "))
            i = nota4
        elif cont == 5:
            nota5 = float(input("Ingresa la nota numero 5 "))
            i = nota5
        if i > 0 and i <= 5:
            cont += cont
    except:
        print("***Este valor no es valido***")
resultado = (nota*p1) + (nota2*p2) + (nota3*p3) + (nota4*p4)+ (nota5*p5)
print ("su nota definitiva es:",resultado)
if resultado <=2:
    print("Reprobaste y no puedes habilitar :(",resultado) 
elif resultado <=3:
    print("reprobaste pero puedes habilitar",resultado)
elif resultado >=3:
    print("aprobaste :D",resultado)
elif resultado >=4:
    print("**EXCELENTE :D**",resultado)


# In[8]:


#ejercicio 28
lista = []
numero1 = int(input("escribe el primer numero "))
numero2 = int(input("escribe el segundo nuemro "))
lista.append(numero1)
lista.append(numero2)
print("El mayor es:",max(lista))
print("El menor es:",min(lista))


# In[3]:


#ejercicio 29
x = float(input("Escriba el numero"))
a = int(x)
b = abs(x) - abs(int(x))
print(a)
print(b)


# In[ ]:


#ejercicio 30
lista = []
numero1 = int(input("escribe el primer numero "))
numero2 = int(input("escribe el segundo nuemro "))
numero3 = int(input("escribe el tercer nuemro "))
lista.append(numero1)
lista.append(numero2)
lista.append(numero3)
print("El mayor es:",max(lista))
print("El menor es:",min(lista))


# In[ ]:


#ejercicio 33
año = int(input("Ingrese el año que quiere saber si es bisiesto o no: "))
if año % 4 != 0: 
    print("No es bisiesto")
elif año % 4 == 0 and año % 100 != 0: 
    print("Es bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0: 
    print("No es bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0: 
    print("Es bisiesto")


# In[2]:


#ejercicio 35
print("***REGISTRÁNDOSE***")
nombre = input("Escriba su nombre de usuario: ")
contraseña = int(input("Escriba su contraseña (solo numeros): "))
print("***INICIANDO SESIÓN***")
nombre2 = input("Escriba su nombre de usuario: ")
contraseña2 = int(input("Escriba su contraseña: "))
if nombre2 == nombre:
    print("Nombre valido")
else:
    print("NOMBRE NO VALIDO")
if contraseña2 == contraseña:
    print("Contraseña valida :D")
else:
    print("CONTRASEÑA NO VALIDA")


# In[7]:


#ejercicio 36
numero = int(input("escriba un numero (entre 1 y 10) "))
if numero == 1:
    print("uno")
elif numero == 2:
    print("dos")
elif numero == 3:
    print("tres")
elif numero == 4:
    print("cuatro")
elif numero == 5:
    print("cinco")
elif numero == 6:
    print("seis")
elif numero == 7:
    print("siete")
elif numero == 8:
    print("ocho")
elif numero == 9:
    print("nueve")
elif numero == 10:
    print("diez")
else:
    print("VALOR NO VALIDO")


# In[8]:


#ejercicio 40
numero = int(input("escriba un numero de los dias de la semana "))
if numero == 1:
    print("lunes")
elif numero == 2:
    print("martes")
elif numero == 3:
    print("miercoles")
elif numero == 4:
    print("jueves")
elif numero == 5:
    print("viernes")
elif numero == 6:
    print("sabado")
elif numero == 7:
    print("domingo")
else:
    print("VALOR NO VALIDO")


# In[ ]:




