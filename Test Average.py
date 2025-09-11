m1 = int(input("Enter marks for Test1:"))
m2 = int(input("Enter marks for Test2:"))
m3 = int(input("Enter marks for Test3:"))

if m1 <= m2 and m1 <= m3:
    avg_marks = (m2 + m3) / 2
    chosen = ("Test2", m2, "Test3", m3)
elif m2 <= m1 and m2 <= m3:
    avg_marks = (m1 + m3) / 2
    chosen = ("Test1", m1, "Test3", m3)
elif m3 <= m1 and m3 <= m2:
    avg_marks = (m1 + m2) / 2
    chosen = ("Test1",m1,"Test2",m2)

print(f"Best two tests: {chosen[0]} ({chosen[1]}), {chosen[2]} ({chosen[3]})")
print(f"Average of best two test marks out of three test marks is:",avg_marks)