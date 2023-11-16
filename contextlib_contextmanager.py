from contextlib import contextmanager

@contextmanager
def my_open(caminho, modo):
    try:
        print('abrindo arquivo')
        arquivo = open(caminho, modo)
        yield arquivo
    except Exception as e:
        print('Deu erro', e)
    
    finally:
        print('Fechando arquivo')
        arquivo.close()

    

with my_open('context_lib.txt', 'a') as arquivo:
    arquivo.write('linha1\n')
    arquivo.write('linha2\n')
    arquivo.write('linha3\n')
    arquivo.write('linha4\n')
    arquivo.close()