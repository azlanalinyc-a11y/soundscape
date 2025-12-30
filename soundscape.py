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
            option = input("Choose between hi-hats, 808s, synth, kick, piano, bass, or break out")
            if option == "snare":
                print("snare")
            elif option == "kick":
                print("kick")
            elif option == "synth":
                print("synth")
            elif option == "808s":
                print("808s")
            elif option == "hi-hats":
                print("hi-hats")
            elif option == "bass":
                print("bass")
            elif option == "piano":
                print("piano")
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
