def main():
    sName = input("Enter your first and last name: ")
    divNames = sName.split()

    isPwdValid = False

    while isPwdValid == False:
        errors = 0
        sPassword = input("Enter your desired password: ")

        sInitials = ""
        for str in divNames:
            sInitials = sInitials + str[0]

        if not (8 <= len(sPassword) <= 12):
            print("Password must be between 8 and 12 characters")
            errors += 1

        if sPassword.upper().startswith("PASS"):
            print("Password can't start with Pass")
            errors += 1

        upper = False

        for char in sPassword:
            if char.isupper():
                upper = True
                break
        
        if not upper == True:
            print("Password must contain at least 1 uppercase letter")
            errors += 1

        lower = False
        
        for char in sPassword:
            if char.islower():
                lower = True
                break
        
        if not lower == True:
            print("Password must contain at least 1 lowercase letter")
            errors += 1

        digit = False
        
        for char in sPassword:
            if char.isdigit():
                digit = True
                break

        if not digit == True:
            print("Password must contain at least 1 number")
            errors += 1

        special_chars = "!@#$%^"
        special = False

        for char in sPassword:
            if char in special_chars:
                special = True
                break
        
        if not special == True:
            print("Password must contain at least 1 of these special characters: ! @ # $ % ^")
            errors += 1

        if sInitials.upper() in sPassword.upper():
            print("Password must not contain user initials.")
            errors += 1
        
        characters = []
        charCount = []
        duplicates = False
        for char in sPassword.lower():
            if char in characters:
                index = characters.index(char)

                charCount[index] += 1
                
                if charCount[index] > 1:
                    duplicates = True

            else:
                characters.append(char)
                charCount.append(1)

        if duplicates:
            print("These characters appear more than once:")
            for i in range(len(characters)):
                if charCount[i] > 1:
                    print(f"{characters[i]}: {charCount[i]} times")
            errors += 1
            continue

        if errors == 0:
            print("Password is valid and OK to use.")
            isPwdValid = True

if __name__ == "__main__":
    main()