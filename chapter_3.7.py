#shrinking guest list because new dinnwer table won't arrive in time, and I've space for only two people.
list = ['max chuard', 'jeff bezos', 'mark zukerburg', 'shoaib makani', 'elon musk', 'archie black']
popa = list.pop()
print(f"Dear {popa.title()}, I'm regret to inform you that due to table unavailbility, I'm cancelling my dinner invitation.") 
pope = list.pop()
print(f"Dear {pope.title()}, I'm regret to inform you that due to table unavailbility, I'm cancelling my dinner invitation.")
pops = list.pop()
print(f"Dear {pops.title()}, I'm regret to inform you that due to table unavailbility, I'm cancelling my dinner invitation.")
popm = list.pop()
print(f"Dear {popm.title()}, I'm regret to inform you that due to table unavailbility, I'm cancelling my dinner invitation.")
print(list)
messag1 = f"Dear {list[0]}, with greatest gratitude, I invite you for the dinner tonight."
messag2 = f"\nDear {list[1]}, with greatest gratitude, I invite you for the dinner tonight."
Full_messag = f"{messag1} {messag2}"
print(Full_messag)

del list[0]
del list[0]

print(list)