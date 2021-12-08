import random
minusculas=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
mayusculas=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
longitud=len(mayusculas)
long_negativa=longitud-longitud*2
for i in range(5):
    print(random.randint(long_negativa, longitud))
preparado=[]
word=[]
def encriptador(texto):
    text=texto.split()
    print(text)
    for i in range(len(text)):
        text[i]=list(text[i])
        preparado.append(text[i])
    for i in range(len(text)):
        for u in range(len(text[i])):



    print(text)
    print("\n \n \n")
    print(preparado)
encriptador("It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using Content here, content here, making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for lorem ipsum will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose injected humour and the like")
