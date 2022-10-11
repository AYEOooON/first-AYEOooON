n = int(input('합(시그마)을 구할 숫자 n을 입력하세요.:'))

sigma = 0
for i in range(1,n+1):
    sigma += i
    
print('1부터', n, '까지의 합은', sigma, '입니다.')