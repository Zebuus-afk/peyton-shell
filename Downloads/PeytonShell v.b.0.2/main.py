#coding: utf-8


""" ----- IMPORTATIONS ----- """
import os

import webbrowser
import socket

import hashlib
import base64
import uuid





""" ----- VARIABLES ----- """

make_a_pause = ""
command = ""
title = "PEYTON SHELL"
version = "v.b.0.2"

#GRP
grp_name = ""





""" ----- FUNCTIONS ----- """

def connexion(grp_name, grp_name_in_past) :
    print("Connexion...")
    try :
        path = "data/.sys.grp"
        file = open(path, "w")
        file.write(grp_name)
        file.close()
        return grp_name
    except :
        print("ERROR 3003")
        return grp_name_in_past

def onSudo(grp_name) :
    try :
        path = "data/" + grp_name + "/.info.grp"
        file = open(path, "r")
        text = file.read()
        file.close()
        grp_list = text.split("\n")
        if (grp_list[1] == "on") :
            return True
        else :
            return False
    except :
        return False





""" ----- GRP ----- """
a = False
try :
    path = "data/.sys.grp"
    file = open(path, "r")
    grp_name = file.read()
    file.close()
    try :
        try :
            path = "data/" + grp_name + "/.info.grp"
            file = open(path, "r")
            text = file.read()
            grp_list = text.split("\n")
            if (grp_list[0] == grp_name) :
                print("Welcome " + grp_list[0] + ".")
                if (grp_list[4] == "on") :
                    grp_password = grp_list[5]
                    password = input("Paswword : ")
                    if grp_password == password :
                        print("Connexion...")
                        grp_name = grp_name
                        a = True
                    else :
                        print("ERROR 3001 : Bad password.")
                if (grp_list[4] == "off") :
                    print("Connexion...")
                    grp_name = grp_name
                    a = True
                else :
                    print("ERROR 3003.")
            else :
                print("ERROR 3003.")
        except :
            print("ERROR 3003.")
    except :
        print("ERROR 3003.")
except :
    print("You want create a group with manual tools.")
 




""" ----- MAIN ----- """

print(title + " - " + version)
make_a_pause = input("Press a key for get access to program.\n")

while (a == True) :
    


    if (grp_name != "") :
        command = input(grp_name + ">>> ")
    else :
        command = input(">>> ")
    
    command_list = command.split(" ")



    if (command_list[0] == "exit") or (command_list[0] == "EXIT"):
        a = False
        break

    if (command_list[0] == "getip") or (command_list[0] == "GETIP") :
        try :
            if (command_list[1] == "-g") or (command_list[1] == "--getip") or (command_list[1] == "--GETIP") :
                try :
                    print(socket.gethostbyname(command_list[2]))
                except :
                    print("ERROR 5001 : USAGE : getip -g [URL]")
            if (command_list[1] == "-l") or (command_list[1] == "--location") or (command_list[1] == "--LOCATION") :
                try :
                    webbrowser.open("https://fr.geoipview.com/?q=" + socket.gethostbyname(command_list[2]))
                except :
                    print("ERROR 5001 : USAGE : getip -l [URL]")
        except :
            print("-g or --getip    : Allows you to obtain the IP address of a website using a URL.")
            print("-l or --location : Used to locate an IP.")
        continue

    if (command_list[0] == "grp") or (command_list[0] == "GRP") :
        try :
            if (command_list[1] == "-c") or (command_list[1] == "--create") or (command_list[1] == "--CREATE") :
                try :
                    x = grp_name
                    grp_name = command_list[2]
                    grp_on_sudo = command_list[3]
                    grp_on_edit = command_list[4]
                    grp_on_read = command_list[5]
                    grp_on_password = command_list[6]
                    os.mkdir("data/" + grp_name)
                    path = "data/" + grp_name + "/.info.grp"
                    file = open(path, "w")
                    file.write(grp_name + "\n" + grp_on_sudo + "\n" + grp_on_edit + "\n" + grp_on_read + "\n" + grp_on_password)
                    if (grp_on_password == "on") or (grp_on_password == "ON") :
                        grp_password = command_list[7]
                        file.write("\n" + grp_password)
                    file.close()
                    path = "data/.info.grp"
                    file = open(path, "a")
                    file.write("\n" + grp_name)
                    file.close()
                    print("This group has created.")
                    grp_name = x
                    continue
                except :
                    print("ERROR 5001 : USAGE : grp -c [name] [sudo=on/off] [edit_perms=on/off] [read_perms=on/off] [password=on/off] [password]")
                continue
            if (command_list[1] == "-L") or (command_list[1] == "--lognin") or (command_list[1] == "--LOGNIN") :
                try :
                    try :
                        path = "data/" + command_list[2] + "/.info.grp"
                        file = open(path, "r")
                        text = file.read()
                        file.close()
                        grp_list = text.split("\n")
                        if (grp_list[0] == command_list[2]) : 
                            if (grp_list[4] == "on") :
                                grp_password = grp_list[5]
                                password = input("Paswword : ")
                                if grp_password == password :
                                    grp_name = connexion(command_list[2], grp_name)
                                else :
                                    print("ERROR 3001 : Bad password.")
                            if (grp_list[4] == "off") :
                                grp_name = connexion(command_list[2], grp_name)
                            else :
                                print("ERROR 3003.")
                        else :
                            print("ERROR 3002 : This group doesn't exist.")
                    except :
                        print("ERROR 3002 : This group doesn't exist.")
                    continue
                except :
                    print("ERROR 5001 : USAGE : grp -L [name]")
                continue
            if (command_list[1] == "-l") or (command_list[1] == "--list") or (command_list[1] == "--LIST") :
                path = "data/.info.grp"
                file = open(path, "r")
                print (file.read())
                file.close()
                continue
            else :
                print("-c or --create   : Create a group.")
                print("-L or --lognin   : Create a group.")
                print("-l or --list     : List the groups.")
                continue
        except :
            print("-c or --create   : Create a group.")
            print("-L or --lognin   : Create a group.")
            print("-l or --list     : List the groups.")
        continue

    if (command_list[0] == "help") or (command_list[0] == "HELP") :
        print("-----+++++ HELP +++++-----")
        print("exit       : Exit the program.")
        print("getip      : Display the getip commands.")
        print("grp        : Display the grp commands.")
        print("help       : Display a command-list.")
        print("webbrowser : Display the webbrowser commands.")
        continue

    if (command_list[0] == "os") or (command_list[0] == "OS") :     
        if onSudo(grp_name) :
            i = True
            while i :
                command_os = input(grp_name + "/os>>> ")
                if command_os == "exit" :
                    break
                else :
                    os.system(command_os)
        else :
            print("ERROR 6001.")

    if (command_list[0] == "webbrowser") or (command_list[0] == "WEBBROWSER") :
        try :
            if (command_list[1] == "-o") or (command_list[1] == "--open") or (command_list[1] == "--OPEN") :
                try :
                    webbrowser.open(command_list[2])
                except :
                    print("ERROR 5001 : USAGE : getip -o [URL]")
            if (command_list[1] == "-h") or (command_list[1] == "--host") or (command_list[1] == "--HOST") :
                try :
                    webbrowser.open("https://github.com/Zebuus-afk/peyton-shell/")
                except :
                    print("ERROR 5001 : USAGE : getip -h")
        except :
            print("-o or --open    : Open a internet page with an URL.")
            print("-h or --host    : Open our website on a internet page.")
        continue

    else :
        print("ERROR 1001 : Command not found.")
