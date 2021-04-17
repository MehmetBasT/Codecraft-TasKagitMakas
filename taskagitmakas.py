import random
import PySimpleGUI as Arayuz

buttons =[Arayuz.Button('Tas',key='Button1',pad=(25,0), size=(10,5), button_color=('white', 'green')),Arayuz.Button('Kağıt',key='Button2', pad=(25,0),size=(10,5), button_color=('white', 'green')),Arayuz.Button('Makas',key='Button3',pad=(25,0), size=(10,5), button_color=('white', 'green')),[Arayuz.Text("Sonuç : "), Arayuz.Text(size=(25,1), key="-OUTPUT-")]]

Arayuz.theme('DarkAmber')
pencere = Arayuz.Window(title="Tas Kagıt Makas Oyunu", layout=[[buttons]], size=(500, 200))


while True:
    event, values = pencere.read()
    if event == "Exit" or event == Arayuz.WIN_CLOSED:
        break

    if event == 'Button1':
        kuc = 'tas'
    if event == 'Button2':
        kuc = 'kagıt'
    if event == 'Button3':
        kuc = 'makas'

    bilgisayar = ["Makas","Kagıt","Tas"]

    pc = (random.choice(bilgisayar))

    if kuc == "tas" and pc == "Tas":
        sonuc ="Pc:"+pc+" Berabere"
        pencere["-OUTPUT-"].update(sonuc)

    elif kuc == "tas" and pc == "Kagıt":
        sonuc ="Pc:"+ pc +" Bilgisayar Kazandı"
        pencere["-OUTPUT-"].update(sonuc)

    elif kuc == "tas" and pc == "Makas":
        sonuc ="Pc:"+pc+" Kullanıcı Kazandı"
        pencere["-OUTPUT-"].update(sonuc)

    elif kuc == "kagıt" and pc == "Kagıt":
        sonuc ="Pc:"+pc+" Berabere"
        pencere["-OUTPUT-"].update(sonuc)

    elif kuc == "kagıt" and pc == "Makas":
        sonuc ="Pc:"+pc+" Bilgisayar Kazandı"
        pencere["-OUTPUT-"].update(sonuc)

    elif kuc == "kagıt" and pc == "Tas":
        sonuc ="Pc:"+pc+" Kullanıcı Kazandı"
        pencere["-OUTPUT-"].update(sonuc)

    elif kuc == "makas" and pc == "Makas":
        sonuc ="Pc:"+pc+" Berabere"
        pencere["-OUTPUT-"].update(sonuc)

    elif kuc == "makas" and pc == "Tas":
        sonuc ="Pc:"+pc+" Bilgisayar Kazandı"
        pencere["-OUTPUT-"].update(sonuc)

    elif kuc == "makas" and pc == "Kagıt":
        sonuc ="Pc:"+pc+" Kullanıcı Kazandı"
        pencere["-OUTPUT-"].update(sonuc)









