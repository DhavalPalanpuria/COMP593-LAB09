from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from pokeapi import get_pokemon_info

#creating a window
root = Tk()
root.title("Pokemon Information Viewer.")
root.resizable(False,False)

#adding frames to window
from_top = ttk.Frame(root)
from_top.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

from_bottom_left = ttk.LabelFrame(root, text="Information.")
from_bottom_left.grid(row=1, column=0)

from_bottom_right = ttk.LabelFrame(root, text="Stats.")
from_bottom_right.grid(row=1, column=1)

#adding widgets to top frame
label_name = ttk.Label(from_top, text="Pokemon Name:")
label_name.grid(row=0, column=0, padx=5)

enter_name = ttk.Entry(from_top)
enter_name.grid(row=0,column=1, padx=5)

def handle_get_info_button():
    #getting name of the pokemon
    poke_name= enter_name.get()

    #getting pokemon information
    poke_information = get_pokemon_info(poke_name)
    if poke_information is None:
        error_msg = f"Unable to get information from PokeAPI for {poke_name}."
        messagebox.showinfo(title="Error", message= error_msg)
        return
    
    #info 
    label_height_value['text'] = f"{poke_information['height']} dm"
    label_weight_value['text'] = f"{poke_information['weight']} hg"
    label_type_value['text'] = [type['type']['name'] for type in poke_information['types']]

    #stas
    hp_bar['value'] = poke_information['stats'][0]['base_stat']
    attack_bar['value'] = poke_information['stats'][1]['base_stat']
    defense_bar['value'] = poke_information['stats'][2]['base_stat']
    specialattack_bar['value'] = poke_information['stats'][3]['base_stat']
    specialdefense_bar['value'] = poke_information['stats'][4]['base_stat']
    speed_bar['value'] = poke_information['stats'][5]['base_stat']


    return

button_get_info = ttk.Button(from_top, text="Get Information", command=handle_get_info_button)
button_get_info.grid(row=0, column=2, padx=5)

#adding widgets to bottom left
label_name = ttk.Label(from_top, text="Pokemon Name:")
label_name.grid(row=0,column=0)

label_height = ttk.Label(from_bottom_left, text='Height:')
label_height.grid(row=0,column=0)
label_height_value = ttk.Label(from_bottom_left, text='TBD')
label_height_value.grid(row=0,column=1)

label_weight = ttk.Label(from_bottom_left, text='Weight:')
label_weight.grid(row=1,column=0)
label_weight_value = ttk.Label(from_bottom_left, text='TBD')
label_weight_value.grid(row=1,column=1)

label_type = ttk.Label(from_bottom_left, text='Type:')
label_type.grid(row=2,column=0)
label_type_value = ttk.Label(from_bottom_left, text='TBD')
label_type_value.grid(row=2,column=1)

#adding widgets to bottom right
label_hp = ttk.Label(from_bottom_right, text="HP")
label_hp.grid(row=0, column=0)
hp_bar = ttk.Progressbar(from_bottom_right,orient=HORIZONTAL, length=175, maximum=200 )
hp_bar.grid(row=0,column=1)

label_attack = ttk.Label(from_bottom_right, text="Attack")
label_attack.grid(row=1, column=0)
attack_bar = ttk.Progressbar(from_bottom_right,orient=HORIZONTAL, length=175, maximum=200 )
attack_bar.grid(row=1,column=1)

label_defense = ttk.Label(from_bottom_right, text="Defense")
label_defense.grid(row=2, column=0)
defense_bar = ttk.Progressbar(from_bottom_right,orient=HORIZONTAL, length=175, maximum=200 )
defense_bar.grid(row=2,column=1)

label_specialattack = ttk.Label(from_bottom_right, text="Special Attack")
label_specialattack.grid(row=3, column=0)
specialattack_bar = ttk.Progressbar(from_bottom_right,orient=HORIZONTAL, length=175, maximum=200 )
specialattack_bar.grid(row=3,column=1)

label_specialdefense = ttk.Label(from_bottom_right, text="Special Defense")
label_specialdefense.grid(row=4, column=0)
specialdefense_bar = ttk.Progressbar(from_bottom_right,orient=HORIZONTAL, length=175, maximum=200 )
specialdefense_bar.grid(row=4,column=1)

label_speed = ttk.Label(from_bottom_right, text="Speed")
label_speed.grid(row=5, column=0)
speed_bar = ttk.Progressbar(from_bottom_right,orient=HORIZONTAL, length=175, maximum=200 )
speed_bar.grid(row=5,column=1)
#loop untill closed
root.mainloop()