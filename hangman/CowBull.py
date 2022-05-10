import random
user_name=input("Enter Your Name:-\n")
print("**********--","Hello",user_name,"--**********")
print("Welcome to Cows And Bulls Game")
def fun():
    list1=[0,1,2,3,4,5,6,7,8,9]
    bull_list=[0,0,0,0,0]
    cows_list=[0,0,0,0,0]
    list2=random.sample(list1,k=5)
    print("list2=",list2)
    chances=10
    print("You have",chances,"chances")
    j=0
    while j<+chances:
        user_choice=int(input("Guess Any Number:-"))
        if user_choice in list2:
            guess_position=int(input("Please Enter Position:-"))
            Index=list2.index(user_choice)
            if Index==guess_position:
                bull_list[guess_position]=user_choice
                print("bull list :-",bull_list)
            else:
                cows_list[guess_position]=user_choice
                print("cow list :-",cows_list)
        else:
            print("Sorry, You entered wrong number please try again")
        j+=1
        if list2==bull_list:
            print("Congratulation",user_name,"You are the winner")
            break
    else:
        print("Opps You are the looser")
fun()
while True:
    Play_again=input("Do you want to Play again\n1.Yes\n2.No\n")
    if Play_again=="Yes":
        fun()
    else:
        break