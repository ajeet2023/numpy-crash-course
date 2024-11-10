#invite 3 people to dinner and message to each person inviting for dinner.
list = ['jeff bezos', 'mark zukerburg', 'bill gates']
message1 = f"Dear {list[0].title()}, with greatest gratitude, I invite you for the dinner tonight."
message2 = f"\nDear {list[1].title()}, with greatest gratitude, I invite you for the dinner tonight."
message3 = f"\nDear {list[2].title()}, with greatest gratitude, I invite you for the dinner tonight."
full_message = f"{message1} {message2} {message3}"
print(full_message)
#One of the guests is unavailable so made a print call that he can't attend.
unavailable = 'bill gates'
list.remove(unavailable)
print(list)
print(f"{unavailable.title()} is not unavailable, so he can't attend the invitation.")
#Replacing the name with a person who can attend it and sending a new set of messages
list.insert(2, 'elon musk')
print(list)
message5 = f"\nDear {list[2].title()}, with greatest gratitude, I invite you for the dinner tonight."
nmessage = f"{message1} {message2} {message5}"
print(nmessage)
message5 = f"Dear attendies, I've found a bigger table for the dinner; hence, I'm requesting a few more people to join us tonight."
print(message5)
list.insert(0, 'max chuard') 
list.insert(3, 'shoaib makani')
list.append('archie black')
print(list)
message_n1 = f"Dear {list[0].title()}, with greatest gratitude, I invite you for the dinner tonight."
message_n2 = f"\nDear {list[1].title()}, with greatest gratitude, I invite you for the dinner tonight."
message_n3 = f"\nDear {list[2].title()}, with greatest gratitude, I invite you for the dinner tonight."
message_n4 = f"\nDear {list[3].title()}, with greatest gratitude, I invite you for the dinner tonight."
message_n5 = f"\nDear {list[4].title()}, with greatest gratitude, I invite you for the dinner tonight."
message_n6 = f"\nDear {list[5].title()}, with greatest gratitude, I invite you for the dinner tonight."
message_n = f"{message_n1} {message_n2} {message_n3} {message_n4} {message_n5} {message_n6}"
print(message_n)
