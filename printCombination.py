keypad = ["","","abc","del","ghi","jki","nno","pqrs","tuv","wxzy"]

def printCombiration(combination, curr, output, n):
    if(curr == n):
        print(*output,sep=",")
        return
    for i in range(len(keypad[combination[curr]])):
        output.append(keypad[combination[curr]][i])
        
        printCombiration(combination,curr + 1,output, n)
        
        output.pop()
        
        if (combination[curr] == 0 or combination[curr] == 1):
            return
combination = [4,3,4]
n = len(combination)   
printCombiration(combination, 0, [], n)    