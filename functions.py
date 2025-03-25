#def emriFunksionit(parametri1, parametri2):
#   print("hello funksion")

def helloworld():
    print("Hello world")

helloworld()

def mbledhja(a,b):
    rezultati = a + b

    return rezultati

print(mbledhja(3,5))

def pjesetimi(a,b):
    result = a/b

    return result

print(pjesetimi(56,7))


def prezentimi(name):
    return f"Pershendje per {name}" #f string

print(prezentimi("Besartin"))



def numriMeIMadh(lista):
    largest_number = 0
    for number in lista:
        if number > largest_number:
            largest_number = number

    return largest_number

lista = [1,445,8362,7573] 

print(numriMeIMadh(lista))

#default arguments

def emri_mbiemri(emri, mbiemri="Berisha"):
    return f"Hello {emri} {mbiemri}"

print(emri_mbiemri("Besart"))



