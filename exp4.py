from itertools import permutations
exp1=input("Enter expression 1 : ").upper()
exp2=input("Enter expression 2 : ").upper()
result=input("Enter the result : ").upper()

letters=set(exp1+exp2+result)


for permutation in permutations("0123456789",len(letters)):
    perm=dict(zip(letters,permutation))
    exp1_map=exp1
    exp2_map=exp2
    result_map=result

    for key,value in perm.items():
        exp1_map=exp1_map.replace(key,value)
        exp2_map=exp2_map.replace(key,value)
        result_map=result_map.replace(key,value)

    

    if exp2_map.startswith("0") or exp1_map.startswith("0") or result_map.startswith("0"):
        continue
    if int(exp1_map)+int(exp2_map)==int(result_map):
        print(f"{exp1} = {exp1_map}\n{exp2} = {exp2_map} \n{result} = {result_map} \n{perm}")
           


