# Write a program to generate all possible subsets of a given set of numbers.

def generate_subset(nums):
    result = []

    def backtrack(index,current):
        # if we reached the end,save the subset
        if index == len(nums):
            result.append(current[:])
            return
        
        # choice 1: exclude the current number
        backtrack(index+ 1,current)

        #choice 2: include the current number
        current.append(nums[index])
        backtrack(index+ 1,current)

        # undo choice (backtrack)
        current.pop()
    backtrack(0,[]) 
    return result

numbers = list(map(int,input("enter number: ").split()))  
subsets = generate_subset(numbers) 

print("All Subsets: ")
for s in subsets:
    print(s)