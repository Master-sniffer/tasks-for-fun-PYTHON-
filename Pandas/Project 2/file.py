import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

fil ="test_p\wildlife.csv"

#col_list=["Precipitation","IndicatedDamage","PilotWarned","CostTotal"]
#col_list=["TimeOfDay", "SpeedKnots","AltitudeFeet", "Sky","PhaseOfFlight","MilesFromAirport", "IndicatedDamage","CostTotal", "CostRepair"]

col_list=["WildlifeSpecies","CostTotal","PhaseOfFlight","PilotWarned", "Precipitation"]
flight= pd.read_csv("test_p\wildlife.csv", usecols=col_list)


# mammal=["American black bear","Armadillo","Black-tailed jackrabbit","Black-tailed prairie dog","Cattle","Common gray fox","Coyote","Deer","Domestic cat","Domestic dog","Foxes","Gunnison's prairie dog","Hares","Lagomorphs","Mink","Moose","Mule deer","Muskrat","North American beaver","North American porcupine","Pocket gophers","Prairie dog","Pronghorn","Rabbits","Raccoon","Red fox","River otter","Skunks","Small Indian mongoose","Striped skunk","Unknown mammal","Virginia opossum","Wapiti","White-tailed deer","White-tailed jackrabbit","Woodrats","Yellow-bellied marmot"]
# reptile=["American alligator","Common snapping turtle","Eastern box turtle","Florida soft shell turtle","Gopher tortoise","Green iguana","Painted turtle","Turtles",""]

Y1=0
Y2=0

N1=0
N2=0


Ysum=0
Nsum=0

Ysum2=0
Nsum2=0

weather=["Fog","Rain","Snow"]

for i in range (len(flight["PilotWarned"])):
    if str(flight["PilotWarned"][i]) == "Y":
        if str(flight["Precipitation"][i]) in weather:
            Y1+=1
            num=(flight["CostTotal"][i])
            num = num.replace(",", "")
            num =int (num)
            Ysum+=num
        elif str(flight["Precipitation"][i]) not in weather :
            Y2+=1
            num=(flight["CostTotal"][i])
            num = num.replace(",", "")
            num =int (num)
            Ysum2+=num

    elif str(flight["PilotWarned"][i]) == "N":
        if str(flight["Precipitation"][i]) in weather:
            N1+=1
            num=(flight["CostTotal"][i])
            num = num.replace(",", "")
            num =int (num)
            Nsum+=num
        elif str(flight["Precipitation"][i]) not in weather :
            N2+=1
            num=(flight["CostTotal"][i])
            num = num.replace(",", "")
            num =int (num)
            Nsum2+=num

print ( "Предупрежден",Y1,"пилот и осадки = ", Ysum ,"\nПредупрежден",Y2," и нет осадков = ", Ysum2,"\n\nНе предупрежден",N1," и осадки = ", Nsum,"\nНе предупрежден",N2,"пилот и нет осадков",Nsum2 )


# y=0
# n=0

# Ysum=0
# Nsum=0


# for i in range (len(flight["PilotWarned"])):
#     if str(flight["PilotWarned"][i]) == "Y":
#         y+=1
#         num=(flight["CostTotal"][i])
#         num = num.replace(",", "")
#         num =int (num)
#         Ysum+=num

#     elif str(flight["PilotWarned"][i]) == "N":
#         n+=1
#         num=(flight["CostTotal"][i])
#         num = num.replace(",", "")
#         num =int (num)
#         Nsum+=num

# print (y , Ysum, n , Nsum)


# Take_off=0
# Climb=0
# Approach=0
# En_Route=0
# Landing_Roll=0
# Descent=0

# for i in range (len(flight["PhaseOfFlight"])):
#     if flight["PhaseOfFlight"][i] == "Descent":
#         if flight["WildlifeSpecies"][i] in mammal or flight["WildlifeSpecies"][i] in reptile:
#             Descent+=1

#     elif flight["PhaseOfFlight"][i] == "Take-off run":
#         if flight["WildlifeSpecies"][i] in mammal or flight["WildlifeSpecies"][i] in reptile:
#             Take_off+=1
    
#     elif flight["PhaseOfFlight"][i] == "Climb":
#         if flight["WildlifeSpecies"][i] in mammal or flight["WildlifeSpecies"][i] in reptile:
#             Climb+=1
    
#     elif flight["PhaseOfFlight"][i] == "Approach":
#         if flight["WildlifeSpecies"][i] in mammal or flight["WildlifeSpecies"][i] in reptile:
#             Approach+=1

#     elif flight["PhaseOfFlight"][i] == "En Route":
#         if flight["WildlifeSpecies"][i] in mammal or flight["WildlifeSpecies"][i] in reptile:
#             En_Route+=1

#     elif flight["PhaseOfFlight"][i] == "Landing Roll":
#         if flight["WildlifeSpecies"][i] in mammal or flight["WildlifeSpecies"][i] in reptile:
#             Landing_Roll+=1

# print (Take_off , Climb, Approach, En_Route, Landing_Roll , Descent)



# un=0
# maU=0
# n=0
# nU=0
# k=0



# for i in range (len(flight["WildlifeSpecies"])):
#     if "Unknown bird" in str(flight["WildlifeSpecies"][i]) :
#         num=(flight["CostTotal"][i])
#         num = num.replace(",", "")
#         num =int (num)
#         maU+=num
#         un+=1
#     elif str(flight["WildlifeSpecies"][i]) != 'nan' :
#         n+=1
#         num=(flight["CostTotal"][i])
#         num = num.replace(",", "")
#         num =int (num)
#         nU+=1
#     else :
#         k+=1

# print (un ,maU, n, nU , k)




# R=0
# NR=0
# MSK=0

# for i in range (len(flight["SpeedKnots"])):
#     if str(flight["AltitudeFeet"][i]) != 'nan' and str(flight["CostRepair"][i]) != "NaN" and str(flight["SpeedKnots"][i]) != 'nan':
#         R+=1
#         num=(flight["CostRepair"][i])
#         num = num.replace(",", "")
#         num =int (num)
#         if num >MSK:
#             MSK=num
    
#     else:
#         NR+=1

# print (R)
# print (NR)
# print (MSK)


# TD=0
# MTD=0

# SK=0
# MSK=0

# AF=0
# MAF=0

# S=0
# MS=0

# PF=0
# MPF=0

# MA=0
# MMA=0

# for i in range (len(flight["TimeOfDay"])):
#     if str(flight["TimeOfDay"][i]) != 'nan' and str(flight["IndicatedDamage"][i]) == "Caused damage":
#         TD+=1
#         num=(flight["CostTotal"][i])
#         num = num.replace(",", "")
#         num =int (num)
#         if num >MTD:
#             MTD=num


# for i in range (len(flight["SpeedKnots"])):
#     if str(flight["SpeedKnots"][i]) != 'nan' and str(flight["IndicatedDamage"][i]) == "Caused damage":
#         SK+=1
#         num=(flight["CostTotal"][i])
#         num = num.replace(",", "")
#         num =int (num)
#         if num >MSK:
#             MSK=num
        

# for i in range (len(flight["AltitudeFeet"])):
#     if str(flight["AltitudeFeet"][i]) != 'nan' and str(flight["IndicatedDamage"][i]) == "Caused damage":
#         AF+=1
#         num=(flight["CostTotal"][i])
#         num = num.replace(",", "")
#         num =int (num)
#         print (MAF ,"MAF")
#         if num >MAF:
#             MAF=num


# for i in range (len(flight["Sky"])):
#     if str(flight["Sky"][i]) != 'nan' and str(flight["IndicatedDamage"][i]) == "Caused damage" and str(flight["Sky"][i]) != 'No Cloud':
#         S+=1
#         num=(flight["CostTotal"][i])
#         num = num.replace(",", "")
#         num =int (num)
#         print (MS , "MS")
#         if num >MS:
#             MS=num


# for i in range (len(flight["PhaseOfFlight"])):
#     if str(flight["PhaseOfFlight"][i]) != 'nan' and str(flight["IndicatedDamage"][i]) == "Caused damage":
#         PF+=1
#         num=(flight["CostTotal"][i])
#         num = num.replace(",", "")
#         num =int (num)
#         print (MPF ," MPF")
#         if num >MPF:
#             MPF=num 
        

# for i in range (len(flight["MilesFromAirport"])):
#     if str(flight["MilesFromAirport"][i]) != 'nan' and str(flight["IndicatedDamage"][i]) == "Caused damage":
#         MA+=1
#         num=(flight["CostTotal"][i])
#         num = num.replace(",", "")
#         num =int (num)
#         if num >MMA:
#             MMA=num


# print ( TD , MTD , SK , MSK , AF , MAF, S, MS , PF,MPF, MA, MMA)

        

# N=0
# W=0
# C=0
# Sn=0

# Warn=0
# NotWarn=0
# Na=0

# N1=0
# N2=0
# N3=0

# RF1=0
# RF2=0
# RF3=0

# SN1=0
# SN2=0
# SN3=0

# EL=0
#money=0.0

#print (flight["Precipitation"])
#for i in range (len(flight["CostTotal"])):




#     if flight["CostTotal"][i] !="0" and str(flight["CostTotal"][i]) != 'nan':
#         num=(flight["CostTotal"][i])
#         print(type(num))
#         num = num.replace(",", "")
#         print(num)
#         num =float (num)
#         money+=num
#         print (money)









    #if flight["Precipitation"][i] != "NaN" or flight["Precipitation"][i] != "nan" or flight["Precipitation"][i] != nan and (flight["IndicatedDamage"][i]=="Caused damage"):
        #flights.append(flight["Precipitation"][i])

#     if (flight["IndicatedDamage"][i]=="Caused damage"):
# #         if flight["PilotWarned"][i]=="Y":
# #             Warn+=1

# #         elif flight["PilotWarned"][i]=="N":
# #             NotWarn+=1
        
# #         else:
# #             Na+=1

# # print(Warn) # 1422
# # print (NotWarn) # 2728
# # print(Na) # 3391




#         if flight["Precipitation"][i] == "NaN" or flight["Precipitation"][i] == "None":
#             if flight["PilotWarned"][i]=="Y":
#                 N1+=1

#             elif flight["PilotWarned"][i]=="N":
#                 N2+=1

#             else:
#                 N3+=1    

#         elif  flight["Precipitation"][i] == ('Rain'):
#             if flight["PilotWarned"][i]=="Y":
#                 RF1+=1

#             elif flight["PilotWarned"][i]=="N":
#                 RF2+=1

#             else:
#                 RF3+=1

#         elif  flight["Precipitation"][i] == ('Fog'):
#             if flight["PilotWarned"][i]=="Y":
#                 RF1+=1

#             elif flight["PilotWarned"][i]=="N":
#                 RF2+=1

#             else:
#                 RF3+=1


#         elif  flight["Precipitation"][i] == ('Snow'):
#             if flight["PilotWarned"][i]=="Y":
#                 SN1+=1

#             elif flight["PilotWarned"][i]=="N":
#                 SN2+=1

#             else:
#                 SN3+=1  

#         else: 
#             EL+=1

# print ("No Precipitation , but pilot was warned", N1 , "\nNo Precipitation, but pilot wasn't warned", N2, "\nNo Precipitation " , N3, "\nNext")
# print ("Precipitation , but pilot was warned", RF1 , "\nPrecipitation, but pilot wasn't warned", RF2, "\nOther" , RF3, "\nNext")
# print ("Snow , but pilot was warned", SN1 , "\Snow, but pilot wasn't warned", SN2, "\nOther" , SN3, "\nNext")
# print ("There is a damaged ship, but there was No Precipitation ", EL)

# print (N+C) #7061
# print (W) # 449
# print (Sn) # 31
            

    

# print (flights)
# for i in range (len(flights)):
#     if fligths[i]


#Читаем данные по рейсам
# flights = pd.read_csv('flights.csv',
#                      parse_dates=['time_hour'], # разобрать дату
#                      dtype={'carrier' : 'str' # код перевозчика - текст
#                            })  

# #Читаем список авиакомпаний
# airlines = pd.read_csv('airlines.csv', 
#                       dtype={'carrier':'str'}) # код перевозчика - текст
# airlines.rename({'name':'airline'}, axis='columns', inplace=True)
