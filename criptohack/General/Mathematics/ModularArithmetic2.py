print("3^17 % 17: " + str(pow(3,17,17)))
print("5^17 % 17: " + str(pow(5,17,17)))
print("7^17 % 17: " + str(pow(7,17,17)))
for x in range(17, 0, -1):
    print(f'7^{x} % 17: ' + str(pow(7,x,17)))
