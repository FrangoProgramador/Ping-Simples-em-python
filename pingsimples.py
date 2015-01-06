import os #importação da biblioteca


host = input("Digite o endereço ou IP: ") #Variavel para armazenar o Endereço ou IP
cmd='ping '+host #O comando é executador a partir do CMD do Windows
ping="".join(os.popen(cmd).readlines())
print (ping)
