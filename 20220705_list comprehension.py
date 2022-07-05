#1부터 10까지 홀수의 제곱 리스트 만들자
array = []
for n in range(1, 10, 2):
    array.append(n ** 2)    #(n * n)
print(array)

array = [i*i for i in range(1, 10, 2)]
print(array)

array = [i*i for i in range(1, 10, 2) if i*i>30]
print(array)