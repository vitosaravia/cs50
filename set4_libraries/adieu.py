"""
implement a program that prompts the user for names, one per line, until the 
user inputs control-d. Assume that the user will input at least one name. Then 
bid adieu to those names, separating two names with one and, three names with 
two commas and one and, and n names with n-1 commas and one and, as in the below:

Adieu, adieu, to Liesl
Adieu, adieu, to Liesl and Friedrich
Adieu, adieu, to Liesl, Friedrich, and Louisa
Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl
"""

def main():
    names = []
    while True:
        try: 
            name = input("Name: ").strip().capitalize()
            names.append(name)
        except EOFError:
            print("")
            return print(f"Adieu, adieu, to {improve(names)}")

def improve(names):
    phrase = ""
    if len(names) > 1:
        for name in names[:-1]:
            name = name + ", "

            phrase = phrase + name
        names[-1] = "and " + names[-1]

        phrase = phrase + names[-1]

    return phrase

if __name__ == "__main__":
    main()