#introduction
username = "soundscape1"
password = "soundscape2"

ask1 = input("enter your username")
ask2 = input("enter your password")

if ask1 == username and ask2 == password:
    print("correct")

while ask1 == username and ask2 == password: 
    question = input("soundstudio or playlist or break out?")
    
    #studio
    if question == "soundstudio":
        print("studio")
        while True:
            try: 
                bpm = int(input("what do you want the bpm to be:"))
                print("success")
                break
            except:
                print("invalid answer. bpm must be a number")
              
        while True:
            time = str(input("what do you want the time signature to be?"))
            if "." in time:
                print("invalid time signature, there cannot be a decimal")
            elif len(time) == 3:
                if time[1] != "/":
                    print("invalid")
                elif int(time[2]) % 2 == 1:
                    print("invalid answer")
                else: 
                    break
            elif len(time) == 4: #must fix
                if time[2] == "/":
                    if int(time[3]) % 2 == 1:
                        print("invalid answer")
                    elif int(time[0:2]) > 16:
                        print("value too high. try again with a diferent number.")
                elif time[1] == "/": #x/xx #0123 #xx/x
                    if int(time[2:4]) % 2 == 1:
                        print("invalid answer")
                    elif int(time[2:4]) > 16:
                        print("value too high. try again with a diferent number.")
                else:
                    print("invalid")
            elif len(time) == 5:
                if time[2] != "/":
                    print("invalid")
                elif int(time[3:5]) % 2 == 1:
                    print("invalid answer")
                elif int(time[3:5]) > 16:
                    print("value too high. try again with a diferent number.")
                elif int(time[0:2]) > 16:
                    print("value too high. try again with a different number.")
            else: 
                print("success")
                break

        beats = int(time.split("/")[0]) 
        steps = beats * 4
        base_pattern = ["-"] * steps
        for i in range (0, steps,  4): 
            base_pattern[i] = "X" 

        while True: #(XXXX) time[] print("*" , time[x]) 3/8 (XXX) *8 split? (xxxxxx) (xxXxx) X = time[] X = 8 x = 16 X = 4 x = 8 y = 16 x = int(time[])*2 xx = int(time[])*4
            option = input("Choose between hihats, 808s, synth, kick, piano, bass, or break out")
            if option == "snare":
                print("snare (" + "".join(base_pattern) + ")")
            elif option == "kick":
               print("kick (" + "".join(base_pattern) + ")")
            elif option == "synth":
                print("synth (" + "".join(base_pattern) + ")")
            elif option == "808s":
                print("808s (" + "".join(base_pattern) + ")")
            elif option == "hihats":
                print("hihats (" + "".join(base_pattern) + ")")
            elif option == "bass":
                print("bass (" + "".join(base_pattern) + ")")
            elif option == "piano":
                print("piano (" + "".join(base_pattern) + ")")
            elif option == "break out":
                print("thanks")
                break
            else:
                print("invalid answer")
   
   #playlist
    elif question == "playlist":
        print("playlist")
    elif question == "break out":
        print("thanks")
        break
    else:
       print("invalid answer")
    
    #fail
else:
    print("fail")
