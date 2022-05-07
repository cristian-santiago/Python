'''
Ler nome, sexo e age de várias pessoas
Read the name, gender and age from several people
guardar em um dicionário
keep them in a dictionary
e todos os dicts tem uma lista.
and all dicts must have a list.


A. How many people were registered(cont)
B. Average people's age
C. A list with all women
D. A people's list with age above average.
Ex.
<< name
<< gender
<< age
<< opt
>> The group has x people
>> The average age is y
>> The women registered were: Ana
>> Above average age people's list
>> name = cristian; gender= M; age = 29;
>> name= ana; gender=F; age= 25;

'''
reg = {}
cad = []
age = []
avg = 0
mulheres = []
acima_avg = []
cont_p = 0


while True:

    
    reg['nome'] = str(input('nome: '))

    reg['sexo'] = str(input('sexo M/F: ')).lower()

    reg['age'] = int(input('age: '))
    if reg['age'] > avg :
        acima_avg.append(reg['nome'])
        acima_avg.append(reg['sexo'])
        acima_avg.append(reg['age'])
    
    cont_p +=1
    cad.append(reg.copy())
    age.append(reg['age'])
    avg = sum(age)//len(age)
    if reg['sexo'] == 'f':
        mulheres.append(reg['nome'])
    opt = str(input('Deseja continuar? Y/N  ')).lower()
    if 'n' in opt:
        break


num = acima_avg[2]
acima = acima_avg.copy()
if num < avg:
    for i in range(3):
        acima.pop(0)
        
print(acima_avg)
print(f'Total de pessoas cadastradas: {cont_p}')
print(f'A média de age das pessoas cadastradas: {avg} anos.')
print(f'Mulheres cadastradas: {mulheres}')
print(acima)



