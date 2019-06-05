f = open("newfile.txt", "a")
lines = ["Hello", "World", "Python", "File IO"]
text = "\n".join(lines)
f.writelines(text)
f.close()