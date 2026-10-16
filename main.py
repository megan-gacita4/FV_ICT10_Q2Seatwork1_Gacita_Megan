from pyscript import document, display

members_name = ['Johanna Ramos', 'Precious Dolormente', 'Isabella Acosta', 'Kailey Gayas', 'Vyelle Bunag']

def check_member(e):
    first_name = document.getElementById("first_name").value
    last_name = document.getElementById("last_name").value
    full_name = first_name + " " + last_name

    if full_name in members_name:
        document.getElementById("result").innerText = "Yayyyy! You are now part of the Rainbow Catering club imnida!, " + full_name
    else:
        document.getElementById("result").innerText = "Mianhae," + full_name + " your name is unfortunately not on the list imnida."

    