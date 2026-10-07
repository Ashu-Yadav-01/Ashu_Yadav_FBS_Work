from userdefinedExp import FbsException

try:
    age = int(input("Enter the AGE "))

    if age < 18:
        raise FbsException("Not Eligible")

except ValueError as e:
    print(e)

except Exception as e:
    print(e)

print("Ayse hi teri age check kar Rahe the...")      