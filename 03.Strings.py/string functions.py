story="once there was a student named Aqeel Abbas Khan"
print(len(story))

print(story.endswith("Khan"))# it tells true falls about ending word
print(story.endswith("Aqeel"))

print(story.count("A"))# it counts the char/word in the given string but it is case sensetive
print(story.count("Aqeel"))

print(story.capitalize()) #it capitalize the starting char of sentence

print(story.find("was")) #it tells the index of char/word entered
print(story.find("niazi"))# -1 mean not available

print(story.replace("Khan","Niazi"))#it replace the char/word with new given
print(story.replace("A","B"))