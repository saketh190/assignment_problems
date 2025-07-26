# convert into western numeric
def convert_into_wester(num):
    num=num.replace(",","")
    for i,j in enumerate(num):
        if j ==".":
            first = num[:i]
            first = first[::-1]
            result = ""
            for k in range(0,len(first),3):
                result +=first[k:k+3]+","
            result = result[::-1]
            return (result[1:]+num[i:])
num = input()
output = convert_into_wester(num)
print(output)