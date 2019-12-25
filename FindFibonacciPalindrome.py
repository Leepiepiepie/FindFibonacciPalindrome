def FindFibonacciPalindrome(sequence):
    total_length=len(sequence)
    length=-1
    start_index=-1
    for buttom in range(total_length-1,-1,-1):
        for top in range(total_length):
            if sequence[top] ==sequence[buttom]:
                for i in range((buttom-top+1)//2):
                    if sequence[top+i]!=sequence[buttom-i]:
                        break
                else:
                    if buttom!=top:
                        if buttom-top+1>length:
                            length= buttom-top+1
                            start_index=top
    if length!=-1 and start_index!=-1:
        return length,start_index
    else:
        return False
if __name__ == '__main__':
    lst=[8,9,4,2,1,2,3,4,4,3,2,1,4,4,2,1,2,1,7,4]
    res = FindFibonacciPalindrome(lst)

    if res:

        print('length:%d start_index:%d' %(res[0], res[1]))
    else:
        print('No Found!')
