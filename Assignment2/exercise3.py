def check_hemoglobin():
    sex = input("Enter your biological sex (female/male): ")
    hemoglobin = float(input("Enter your hemoglobin value (g/l): "))

    if sex == "female":
        if hemoglobin < 117:
            print("Your hemoglobin value is low.")
        elif hemoglobin <= 155:
            print("Your hemoglobin value is normal.")
        else:
            print("Your hemoglobin value is high.")

    elif sex == "male":
        if hemoglobin < 134:
            print("Your hemoglobin value is low.")
        elif hemoglobin <= 167:
            print("Your hemoglobin value is normal.")
        else:
            print("Your hemoglobin value is high.")

check_hemoglobin()