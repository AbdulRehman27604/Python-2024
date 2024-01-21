import math
import doctest

def print_longer(word_1,word_2):
    """
    >>> print_longer("hi","hello")
    hello
    >>> print_longer("hello1","byyeee")
    hello1
    >>> print_longer("thing","name")
    thing
    """
    lenght_1 = len(word_1)
    lenght_2 = len(word_2)
    
    if lenght_1 > lenght_2 or lenght_1 == lenght_2:
        print(word_1)
    else:
        print(word_2)


def print_real_roots(a,b,c):
    """
    >>> print_real_roots(2,2,1)
    NO REAL ROOTS
    >>> print_real_roots(0,2,1)
    ERROR
    >>> print_real_roots(2,4,1)
    -0.293 , -1.707
    """
    main_part = (b**2 - 4*a*c)
    if a == 0:
        print("ERROR")
    elif main_part < 0:
        print("NO REAL ROOTS")
    else:  
        main_part = math.sqrt(main_part)
        formulae_1 = (-b + main_part)/(2*a)
        formulae_2 = (-b - main_part)/(2*a)
        print("{:.3f}".format(formulae_1),",","{:.3f}".format(formulae_2))


def print_zodiac_sign(month : str, day : str):
    
    """
    >>> print_zodiac_sign("january",1)
    Capricorn
    >>> print_zodiac_sign("january",19)
    Capricorn
    
    >>> print_zodiac_sign("january",20)
    Aquarius
    >>> print_zodiac_sign("january",31)
    Aquarius
    
    >>> print_zodiac_sign("february",1)
    Aquarius
    >>> print_zodiac_sign("february",18)
    Aquarius
    
    >>> print_zodiac_sign("february",19)
    Pisces
    >>> print_zodiac_sign("february",29)
    Pisces
    
    >>> print_zodiac_sign("march",1)
    Pisces
    >>> print_zodiac_sign("march",20)
    Pisces
    
    >>> print_zodiac_sign("march",21)
    Aries
    >>> print_zodiac_sign("march",31)
    Aries
    
    >>> print_zodiac_sign("april",1)
    Aries
    >>> print_zodiac_sign("april",19)
    Aries
    
    >>> print_zodiac_sign("april",20)
    Taurus
    >>> print_zodiac_sign("april",30)
    Taurus
    
    >>> print_zodiac_sign("may",1)
    Taurus
    >>> print_zodiac_sign("may",20)
    Taurus
    
    >>> print_zodiac_sign("may",21)
    Gemini
    >>> print_zodiac_sign("may",31)
    Gemini
    
    >>> print_zodiac_sign("june",1)
    Gemini
    >>> print_zodiac_sign("june",20)
    Gemini
    
    >>> print_zodiac_sign("june",21)
    Cancer
    >>> print_zodiac_sign("june",30)
    Cancer
    
    >>> print_zodiac_sign("july",1)
    Cancer
    >>> print_zodiac_sign("july",22)
    Cancer
    
    >>> print_zodiac_sign("july",23)
    Leo
    >>> print_zodiac_sign("july",31)
    Leo
    
    >>> print_zodiac_sign("august",1)
    Leo
    >>> print_zodiac_sign("august",22)
    Leo
    
    >>> print_zodiac_sign("august",23)
    Virgo
    >>> print_zodiac_sign("august",31)
    Virgo
    
    >>> print_zodiac_sign("september",1)
    Virgo
    >>> print_zodiac_sign("september",22)
    Virgo
    
    >>> print_zodiac_sign("september",23)
    Libra
    >>> print_zodiac_sign("september",30)
    Libra
    
    >>> print_zodiac_sign("october",1)
    Libra
    >>> print_zodiac_sign("october",22)
    Libra
    
    >>> print_zodiac_sign("october",23)
    Scorpio
    >>> print_zodiac_sign("october",31)
    Scorpio
    
    >>> print_zodiac_sign("november",1)
    Scorpio
    >>> print_zodiac_sign("november",21)
    Scorpio
    
    >>> print_zodiac_sign("november",22)
    Sagittarius
    >>> print_zodiac_sign("november",30)
    Sagittarius
    
    >>> print_zodiac_sign("december",1)
    Sagittarius
    >>> print_zodiac_sign("december",21)
    Sagittarius
    
    >>> print_zodiac_sign("december",22)
    Capricorn
    >>> print_zodiac_sign("december",30)
    Capricorn
    """
    
    month = month.lower()
    if month == "january" and (day >= 20 and day <= 31):
        print("Aquarius")
    elif month == "february" and (day >= 1 and day <= 18):
        print("Aquarius")
    elif month == "february" and (day >= 19 and day <= 29):
        print("Pisces")  
    elif month == "march" and (day >= 1 and day <= 20):
        print("Pisces")  
    elif month == "march" and (day >= 21 and day <= 31):
        print("Aries")
    elif month == "april" and (day >= 1 and day <= 19):
        print("Aries")
    elif month == "april" and (day >= 20 and day <= 30):
        print("Taurus")   
    elif month == "may" and (day >= 1 and day <= 20):
        print("Taurus") 
    elif month == "may" and (day >= 21 and day <= 31):
        print("Gemini")  
    elif month == "june" and (day >= 1 and day <= 20):
        print("Gemini")     
    elif month == "june" and (day >= 21 and day <= 30):
        print("Cancer")   
    elif month == "july" and (day >= 1 and day <= 22):
        print("Cancer")
    elif month == "july" and (day >= 23 and day <= 31):
        print("Leo")
    elif month == "august" and (day >= 1 and day <= 22):
        print("Leo")
    elif month == "august" and (day >= 23 and day <= 31):
        print("Virgo")    
    elif month == "september" and (day >= 1 and day <= 22):
        print("Virgo")     
    elif month == "september" and (day >= 23 and day <= 30):
        print("Libra")
    elif month == "october" and (day >= 1 and day <= 22):
        print("Libra") 
    elif month == "october" and (day >= 23 and day <= 31):
        print("Scorpio")
    elif month == "november" and  (day >= 1 and day <= 21):
        print("Scorpio")
    elif month == "november" and (day >= 22 and day <= 30):
        print("Sagittarius")    
    elif month == "december" and (day >= 1 and day <= 21):
        print("Sagittarius")   
    elif month == "december" and (day >= 22 and day <= 31):
        print("Capricorn")    
    elif month == "january" and (day >= 1 and day <= 19):
        print("Capricorn")