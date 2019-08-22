
noun_list = input("Enter 5x noun separated by comma: ")
list_n = [str(i) for i in noun_list.split(',')]

plural_noun_list = input("Enter 5x plural noun separated by comma: ")
list_pn = [str(i) for i in plural_noun_list.split(',')]

adjective_list = input("Enter 5x adjective separated by comma: ")
list_a = [str(i) for i in adjective_list.split(',')]

adverb = input("Enter a adverb: ")

plural_body_part_list = input("Enter 4x body part(plural) separated by comma: ")
list_pbp = [str(i) for i in plural_body_part_list.split(',')]


print("Our dining ",list_n[0]," used to be a war ",list_n[1],"\nI thought the battles about correct table ",list_pn[0]," would\n ")
print("never end. It was us kids versus Mom, and it seemed like a fight\nthat would last to the ",list_a[0]," end. But tonight Dad finally ")
print("declared a/an ",list_a[1]," truce, and we negotiated\n",list_a[2],"peace ",list_n[2],". Mom promised to no ")
print("longer get ",adverb," upset the dirty ",list_pn[1],"\nand make ",list_a[3]," remarks when we do ",list_a[4])
print("things she doesn't like. We in turn agreed to: ")
print(" 1) Use napkins to wipe our ",list_pbp[0],"and not\nour ",list_pn[2])
print(" 2) Keep our ",list_pbp[1]," off the table.")
print(" 3) Not use our ",list_pbp[2]," to pick up ",list_pn[3],"\nfrom our plates--except for sandwitches or pieces of ",list_n[3])
print(" 4) Never talk with food in our ",list_pbp[3])
