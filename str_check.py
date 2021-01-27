#Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged. 
def string_given(str):
    if len(str) >=2 and str[ :2] == "Is":
        return str
    else:
        return "Is" + str
print(string_given("Aand"))
print(string_given("IsmyAand"))