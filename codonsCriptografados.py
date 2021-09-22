d = { 'GCA':'A', 'UAA':'B', 'UGC':'C', 'GAU':'D', 'GAG':'E', 'UUU':'F', 'GGC':'G', 'CAU':'H', 'AUA':'I', 'UUC':'J', 'AAA':'K', 'UUG':'L','AUG':'M', 'AAC':'N', 'UAG':'O', 'CCA':'P', 'CAA':'Q', 'CGU':'R', 'AGC':'S', 'ACA':'T', 'UGA':'U', 'GUA':'V', 'UGG':'W', 'GGU':'X', 'UAU':'Y', 'GGA':'Z', 'GGG':' '}

q = int(input())
for i in range(q):
    f = input()
    fi = [f[i:i+3] for i in range(0, len(f), 3)]
    output= []
    
    for j in fi:
        output.append(d[j])
    output.append('.')
    print(''.join(output).capitalize())
