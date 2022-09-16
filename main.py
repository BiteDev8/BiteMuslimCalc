from colorama import Fore, Back, Style, init
import pyfiglet

T = "BiteMuslimCalc"
ASCII_art_1 = pyfiglet.figlet_format(T)
print(ASCII_art_1)
init()


def muslimCalc(age, sexes):
    point=0
    if sexes == "F" and age > 17 :
        print("porte tu le voile ? y/n")
        reponse = str(input())
        if reponse == "y" :
            point += 1
        else : 
            pass
    elif sexes == "F" and age < 18 :
        print("penses tu porter le voile ? y/n")
        reponse = str(input())
        if reponse == "y" :
            point += 1
        else : 
            pass
    elif sexes == "H" and age > 17 :
        print("as tu une barbe ? y/n")
        reponse = str(input())
        if reponse == "y" :
            point += 1
        else : 
            pass
    elif sexes == "H" and age < 18 :
        print("veux tu une barbe ? y/n")
        reponse = str(input())
        if reponse == "y" :
            point += 1
        else : 
            pass
    #question commune
    print("viens tu d'un pay arabe ? y/n")
    reponse = str(input())
    if reponse == "y" :
        point += 1
    else : 
        pass
    print("mange tu du porc ? y/n")
    reponse = str(input())
    if reponse == "n" :
        point += 1
    else : 
        pass
    print("parles tu arabe ? y/n")
    reponse = str(input())
    if reponse == "y" :
        point += 1
    else : 
        pass
    print("lis tu le Coran souvant ? y/n")
    reponse = str(input())
    if reponse == "y" :
        point += 1
    else : 
        pass
    print("aimes tu les autres religions ? y/n")
    reponse = str(input())
    if reponse == "n" :
        point += 1
    else : 
        pass
    print("Allah as toujours raison ? y/n")
    reponse = str(input())
    if reponse == "y" :
        point += 1
    else : 
        pass
    print("Allah es au dessus de tous ? y/n")
    reponse = str(input())
    if reponse == "y" :
        point += 1
    else : 
        pass
    print("pries-tu souvant  ? y/n")
    reponse = str(input())
    if reponse == "y" :
        point += 1
    else : 
        pass
    print("prie tu en direction de la mecque  ? y/n")
    reponse = str(input())
    if reponse == "y" :
        point += 1
    else : 
        pass
    print("aime tu les homo ? y/n")
    reponse = str(input())
    if reponse == "n" :
        point += 1
    else : 
        pass
    print("aimes tu l'alcool  ? y/n")
    reponse = str(input())
    if reponse == "n" :
        point += 1
    else : 
        pass
    print("la musique ? y/n")
    reponse = str(input())
    if reponse == "n" :
        point += 1
    else : 
        pass
    print("apprecie tu les occidantaux ? y/n")
    reponse = str(input())
    if reponse == "n" :
        point += 1
    else : 
        pass

    point = point * 7
    print(point,"%  <===")



print(Fore.GREEN+"age")
a = int(input())
print("sexe")
s = str(input())
muslimCalc(a,s)

input()
input()
input()
input()
input()
input()
input()
input()
input()
input()
