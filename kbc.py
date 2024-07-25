print("Welcome to kbc , lets start with first question")
questions = [["who is the prime minister of india", "Droupadi Murmu", "payal", "rahul gandhi", "narendra modi", 4],
 ["who is the president of india", "Droupadi Murmu", "payal", "rahul gandhi", "narendra modi", 1],
 ["who is the finance minister of india", "Droupadi Murmu", "nirmala sitharaman", "rahul gandhi", "narendra modi", 2],
 ["who is the home minister of india", "Droupadi Murmu", "payal", "amit shah", "narendra modi", 3],
 ["who is the chief minister of uttar pradesh", "Droupadi Murmu", "adityanath yogi", "rahul gandhi", "narendra modi", 2]]
levels =[1000, 2000, 3000, 4000, 5000]
money = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"Answer for Rs. {levels[i]}")
    print(f"{question[0]}")
    print(f"a. {question[1]}   b. {question[2]}")
    print(f"c. {question[3]}   d. {question[4]}")
    reply = int(input("Enter no. between 1 to 4: or 0 to quit"))
    if(reply == 0):
        money = levels[i-1]
        break
    if(reply == question[-1]):
        print(f"correct answer you have won rs. {levels[i]}")
        if(i==2):
            money = levels[i]
        elif(i==4):
            money = levels[i]
    else:
        print("wrong answer")
        break
print(f"your take home money is {money}")