candidate1 = input("Enter 1st candidate name:")
candidate2 = input("Enter 2st candidate name:")
candidate3 = input("Enter 3st candidate name:")
candidate4 = input("Enter 4st candidate name:")
cand1_votes = 0
cand2_votes = 0
cand3_votes = 0
cand4_votes = 0

voters_id = [380, 381, 382, 383, 384, 385, 386, 387]
no_of_voters = len(voters_id)
print("number of voters:", no_of_voters)
voted = []

while True:
    if voters_id == []:
        print("voting is over")
        if cand1_votes > cand2_votes and cand1_votes > cand3_votes and cand1_votes > cand4_votes:
            print(f"{candidate1} won the election with {cand1_votes}")
        elif cand2_votes > cand1_votes and cand2_votes > cand3_votes and cand2_votes > cand4_votes:
            print(f"{candidate2} won the election with {cand2_votes}")
        elif cand3_votes > cand1_votes and cand3_votes > cand2_votes and cand3_votes > cand4_votes:
            print(f"{candidate3} won the election with {cand3_votes}")
        elif cand4_votes > cand1_votes and cand4_votes > cand2_votes and cand4_votes > cand4_votes:
            print(f"{candidate4} won the election with {cand4_votes}")
        else:
            print("Tie!!")
        break
    else:
        voter = int(input("Enter the id"))
        if voter in voted:
            print("you already voted")
        else:
            if voter in voters_id:
                print(f"1.{candidate1}\n2.{candidate2}\n3.{candidate3}\n4.{candidate4}")
                choice = int(input("enter your choice"))
                if choice == 1:
                    cand1_votes += 1
                    print(f" you voted {candidate1}")
                elif choice == 2:
                    cand2_votes += 1
                    print(f" you voted {candidate2}")
                elif choice == 3:
                    cand3_votes += 1
                    print(f" you voted {candidate3}")
                elif choice == 4:
                    cand4_votes += 1
                    print(f" you voted {candidate4}")

                voters_id.remove(voter)
                voted.append(voter)
            else:
                print("you are not allowed to vote")