from userdefinedExp import AshuException
try:
    age = int(input("Enter the Age: "))
    if age<18:
        raise AshuException("Not Eligible")

except ValueError as e:
    print(e)
except AshuException as e:
    print(e)
print("Age check completed...")            