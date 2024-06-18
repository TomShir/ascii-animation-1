from colorama import Fore 
import sys 
import time 
import os
import random
from playsound import playsound
colors=[Fore.RED,Fore.GREEN,Fore.BLUE,Fore.YELLOW,Fore.MAGENTA,Fore.LIGHTRED_EX,Fore.LIGHTMAGENTA_EX,Fore.BLACK,Fore.CYAN,Fore.RESET]
cuboid_frames=['''
                ________________
               /\______________/\ 
               \/______________\/''','''
                _______________
               /\_____________/\ 
               \/_____________\/''','''
                ______________
               /\____________/\ 
               \/____________\/''','''
                ____________
               /\__________/\ 
               \/__________\/''','''
                __________
               /\________/\ 
               \/________\/''','''
                ________
               /\______/\ 
               \/______\/''','''
                ____
               /\__/\ 
               \/__\/''',f'''
                ____
               /\__/\ {Fore.RED+"*"}{colors[-3]} 
               \/__\/'''
              ,f'''
                ____
               /\__/\  {Fore.RED+"*"}{colors[-3]}  
               \/__\/''',f'''
                ____
               /\__/\   {Fore.RED+"*"}{colors[-3]}  
               \/__\/''',f'''
                ____
               /\__/\    {Fore.RED+"*"}{colors[-3]}  
               \/__\/''',f'''
                ____
               /\__/\     {Fore.RED+"*"}{colors[-3]}  
               \/__\/''',f'''
                ____
               /\__/\      {Fore.RED+"*"}{colors[-3]}  
               \/__\/''',f'''
                ____
               /\__/\       {Fore.RED+"*"}{colors[-3]}  
               \/__\/''',f'''
                ____
               /\__/\        {Fore.RED+"*"}{colors[-3]}  
               \/__\/''',f'''
                ____
               /\__/\         {Fore.RED+"*"}{colors[-3]}  
               \/__\/''',f'''
                ____
               /\__/\          {Fore.RED+"*"}{colors[-3]}  
               \/__\/''',f'''
                ____
               /\__/\           {Fore.RED+"*"}{colors[-3]}  
               \/__\/''',f'''
                ____
               /\__/\            {Fore.RED+"*"}{colors[-3]}  
               \/__\/''',f'''
                ____
               /\__/\             {Fore.RED+"*"}{colors[-3]}  
               \/__\/''',f'''
                ____
               /\__/\              {Fore.RED+"*"}{colors[-3]}  
               \/__\/''',f'''
                ____
               /\__/\               {Fore.RED+"*"}{colors[-3]}  
               \/__\/''',f'''
                ____
               /\__/\                {Fore.RED+"*"}{colors[-3]}  
               \/__\/''',f'''
                ____
               /\__/\                 {Fore.RED+"*"}{colors[-3]}  
               \/__\/''',f'''
                ____
               /\__/\                  {Fore.RED+"*"}{colors[-3]}  
               \/__\/''',f'''
                ____
               /\__/\                   {Fore.RED+"*"}{colors[-3]}  
               \/__\/''',f'''
                ____
               /\__/\                    {Fore.RED+"*"}{colors[-3]}  
               \/__\/''',f'''
                ____
               /\__/\                      {Fore.RED+"*"}{colors[-3]}  
               \/__\/''',f'''
                ____
               /\__/\                        {Fore.RED+"*"}{colors[-3]}  
               \/__\/''',f'''
                ____
               /\__/\                         {Fore.RED+"*"}{colors[-3]}  
               \/__\/''',f'''
                ____
               /\__/\                           {Fore.RED+"*"}{colors[-3]}  
               \/__\/''',f'''
                ____
               /\__/\                             {Fore.RED+"*"}{colors[-3]}  
               \/__\/''',f'''
                ____
               /\__/\                               {Fore.RED+"*"}{colors[-3]}  
               \/__\/''']
def create_ascii_animation(frames,delay_time,color):
    for frame in frames:
        #Flushing the output buffer,so that the text appears as soon as possible 
        sys.stdout.flush()
        time.sleep(delay_time)
        os.system('cls')
        if color==None:
         print(f'{frame}')
        else:
            print(f'{color}{frame}')

    else:
        print(f'{colors[-1]}')
        
for n in range(100):
 create_ascii_animation(frames=cuboid_frames,delay_time=0.01,color=colors[-3])
 if cuboid_frames:
     create_ascii_animation(frames=cuboid_frames[0:7:1][::-1],delay_time=0.01,color=colors[-3])