"""
Name: ************
Due Date: 12/8/25
Description:
Write an application called ‘HumanTemp14’ that will help a person
decide what medical treatment they should seek
based on their temperature.
This is a continuous run until told to stop. (not ‘one and done’)
The app will ask the patient’s temperature (in Fahrenheit)
There will be 7 possible outcomes.
- less than 90° Emergency Room
- 90°-95° degree hypothermia
    * The patient potentially has hypothermia!
    * Cover with Blankets.
    * Monitor Breathing.
    * Provide warm Beverages!
- 95°-97.7° observation necessary
- 97.7° - 99.5 normal
- 99.5°-100.9° observation necessary
- 100.9°-105° fever
    * The patient has a fever!
    * Rest and drink plenty of fluids. Medication is not needed.
    * Call the doctor if the fever is accompanied by a severe headache,
     stiff neck, shortness of breath, or other unusual signs or symptoms.
_ over 105° Emergency Room

The application will also convert the degrees to Celsius(rounded to one
decimal place). (in case it would like to be used in a country other
than the US)
"""

#lower temp in range is inclusive, upper is not inclusive

#celsius = (fahrenheit - 32) * (5/9)

choice = "yes"
while choice.lower() == "yes":
    patientTemp = float(input("\n\n\nWhat is the patient's temperature (in Fahrenheit)? "))

    if patientTemp < 90:
        print("\n**********************************************************")
        print("***Take the patient to the Emergency Room Immediately!!***")
        print("**********************************************************\n")
    elif 90 <= patientTemp < 95:
        print("The patient potentially has hypothermia!")
        print("Cover with blankets.")
        print("Monitor breathing.")
        print("Provide warm beverages!")
    elif 95 <= patientTemp < 97.7:
        print("Observation necessary")
    elif 97.7 <= patientTemp < 99.5:
        print("Normal")
    elif 99.5 <= patientTemp < 100.9:
        print("Observation necessary")
    elif 100.9 <= patientTemp < 105.5:
        print("The patient has a fever!")
        print("Rest and drink plenty of fluids. Medication is not needed.")
        print("Call the doctor if the fever is accompanied by a severe headache,")
        print("stiff neck, shortness of breath, or other unusual signs.")
    else:
        print("\n**********************************************************")
        print("***Take the patient to the Emergency Room Immediately!!***")
        print("**********************************************************\n")

    print("\nThe patient's temperature in Cel is", round((patientTemp -32) * (5/9), 1), "C")

    choice = input("Type yes to continue: ")
print("The end")
