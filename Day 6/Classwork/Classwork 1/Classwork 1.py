#-----------------------------------------------------------------------------


"""აქ ჩვენ 6-ე, 7-ე, და 8-ე  ხაზზე დავადეკლარირეთ სტრინგ ტიპის 
ცვლადები: num, num1, num3, რომელებსაც მივანიჭეთ input ფუნქცია.

Input ფუნქცია მაგალითად, აქ 7-ე ხაზზე არის დაწერილი: 
Insert your second number for action და გვერდით გამოტოვებულია ადგილი
რიცხვის ჩასაწერად.

ამ შემთხვევაში Inster your second number for action  არის მითითება
თუ რა უნდა ჩაწეროს მომხმარებელმა და ადგილი რომელიც არის Space-ით
გამოტოვებული არის იმისთვის რომ ჩაწეროს რიცხვი და ამ ჩაწერის საშუალებას გვაძლევს 
input ფუნქცია"""



num = int(input("Instert your second number for action "))
num2 = int(input("Instert Your Second Number For action! "))
num3 = int(input("Insert Your Third And Last Number For Action! "))

#-------------------------------------------------------------------------------

"""აქ ჩვენ ისევ დავადეკლარირეთ სტრინგ ტიპის ცვლადი სახელად result
და მივანიჭეთ მაღლა მოცემული სტრინგ ტიპის ცვლადებზე ერთმანეთზე გამრავლება"""

result = num * num2 * num3

#-------------------------------------------------------------------------------
"""ხოლო საბოლოოდ ჩვენ ვიყენებთ print ფუნქციას რომელსაც ეს ყველაფერი გამოაქ 
ეკრანზე/ტერმინალზე რომ ჩვენ შეგვეძლოს კოდის შედეგის დანახვა"""

print(result)