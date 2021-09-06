
arquivo=open('CursoUdemyPython/exercicios/Lista6/arq.txt')
linhas=arquivo.readlines()   
cidade=[]
cidade.append(linhas[0].split(','))
print(int(cidade[0][1]))