import sys
# import fileinput

# Selection Sort

def selectionsort( aList ):
  for i in range( len( aList ) ):
    menor = i
    for k in range( i + 1 , len( aList ) ):
      if aList[k] < aList[menor]:
        menor = k
 
    swap( aList, menor, i )
 
def swap( A, x, y ):
  tmp = A[x]
  A[x] = A[y]
  A[y] = tmp

# InsertionSort

def insertionSort(alist):
   for index in range(1,len(alist)):

     valoratual = alist[index]
     posicao = index

     while posicao>0 and alist[posicao-1]>valoratual:
         alist[posicao]=alist[posicao-1]
         posicao = posicao-1

     alist[posicao]=valoratual

#Merge Sort

def mergeSort(alist):
    if len(alist)>1:
        meio = len(alist)//2
        metadeEsquerda = alist[:meio]
        metadeDireita = alist[meio:]

        mergeSort(metadeEsquerda)
        mergeSort(metadeDireita)

        i=0
        j=0
        k=0

        while i < len(metadeEsquerda) and j < len(metadeDireita):
            if metadeEsquerda[i] < metadeDireita[j]:
                alist[k]=metadeEsquerda[i]
                i=i+1
            else:
                alist[k]=metadeDireita[j]
                j=j+1
            k=k+1

        while i < len(metadeEsquerda):
            alist[k]=metadeEsquerda[i]
            i=i+1
            k=k+1

        while j < len(metadeDireita):
            alist[k]=metadeDireita[j]
            j=j+1
            k=k+1
    

# Quicksort

def quickSort(alist):
   quickSortAjuda(alist,0,len(alist)-1)

def quickSortAjuda(alist,primeiro,ultimo):
   if primeiro<ultimo:

       pontoDivisao = particao(alist,primeiro,ultimo)

       quickSortAjuda(alist,primeiro,pontoDivisao-1)
       quickSortAjuda(alist,pontoDivisao+1,ultimo)


def particao(alist,primeiro,ultimo):
   pivo = alist[primeiro]

   marcaEsquerda = primeiro+1
   marcaDireita = ultimo

   done = False
   while not done:

       while marcaEsquerda <= marcaDireita and alist[marcaEsquerda] <= pivo:
           marcaEsquerda = marcaEsquerda + 1

       while alist[marcaDireita] >= pivo and marcaDireita >= marcaEsquerda:
           marcaDireita = marcaDireita -1

       if marcaDireita < marcaEsquerda:
           done = True
       else:
           temp = alist[marcaEsquerda]
           alist[marcaEsquerda] = alist[marcaDireita]
           alist[marcaDireita] = temp

   temp = alist[primeiro]
   alist[primeiro] = alist[marcaDireita]
   alist[marcaDireita] = temp


   return marcaDireita

#Heapsort

def heapsort( aList ):
  # converte lista pra heap
  comprimento = len( aList ) - 1
  ultimoPai = comprimento // 2
  for i in range ( ultimoPai, -1, -1 ):
    moveBaixo( aList, i, comprimento )
 
  # transformando heap em um array ordenado
  for i in range ( comprimento, 0, -1 ):
    if aList[0] > aList[i]:
      troca( aList, 0, i )
      moveBaixo( aList, 0, i - 1 )
 
 
def moveBaixo( aList, primeiro, ultimo ):
  maior = 2 * primeiro + 1
  while maior <= ultimo:
    # a criança da direita exite e é maior que a da esquerda 
    if ( maior < ultimo ) and ( aList[maior] < aList[maior + 1] ):
      maior += 1
 
    # a criança da direita é maior que o pai
    if aList[maior] > aList[primeiro]:
      troca( aList, maior, primeiro )
      # mover para baixo, para a maior criança
      primeiro = maior;
      maior = 2 * primeiro + 1
    else:
      return # forçar saída
 
 
def troca( A, x, y ):
  tmp = A[x]
  A[x] = A[y]
  A[y] = tmp


def main():

	tipo = sys.argv[1]

	numeroDeEntradas = input()

	numeroDeEntradas = int(numeroDeEntradas)

	lista = []

	for x in range(numeroDeEntradas):
		y = input()
		lista.append(int(y))


	if tipo=="1":
		selectionsort(lista)
	elif tipo=="2":
		insertionSort(lista)
	elif tipo=="3":
		mergeSort(lista)
	elif tipo=="4":
		quickSort(lista)
	elif tipo=="5":
		heapsort(lista)

	else:
		print("Numero errado")

	for x in lista:
		print(x)

main()
  

