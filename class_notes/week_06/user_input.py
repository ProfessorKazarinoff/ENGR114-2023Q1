# user_input.py

def user_input():
    wt = input("Which weather type (temperature, humidity, rainfall or pressure)?")
    nd = input("How many data points (maximum of 8000)?")
    a = [wt,nd]
    
    return a
