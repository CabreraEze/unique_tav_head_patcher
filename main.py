from tkinter import filedialog, messagebox, Tk, Button
import os

unique_tav = False

master = Tk()
master.title('UNIQUE_TAV_HEAD_PATCHER')
folder_b = Button(master=master, text='unique tav compatch', command=lambda: set_mode(True))
folder_b.pack()
file_b = Button(master=master, text='vanilla', command=lambda: set_mode(False))
file_b.pack()

def set_mode(mode):
    global unique_tav, master
    unique_tav = mode
    master.destroy()

master.mainloop()



# Load lsx files
folder = filedialog.askdirectory()
merged_files = []
for (root, dirs, files) in os.walk(folder):
    for file in files:
        if 'merged' in file and file.endswith('.lsx'):
            file_path = os.path.join(root, file)
            merged_files.append(file_path)



if unique_tav:
    makeup_enable = 'True'
    makeup_id = '2f72fffe-7602-05c4-b005-ieatpaste666'

    tattoo_enable = 'True'
    tattoo_id = '505e82ee-ed64-05cc-aa31-ieatpaste666'

else:
    makeup_enable = 'False'
    makeup_id = '2f72fffe-7602-05c4-b005-14bd527391f1'

    tattoo_enable = 'False'
    tattoo_id = '505e82ee-ed64-05cc-aa31-6b7057a5b75f'


# Just to make my life easier
def change_value(node_str,value):
    start_index = node_str.find('value="') + len('value="')
    end_index = node_str.find('"', start_index)

    return node_str[:start_index] + value + node_str[end_index:]


for merged_file in merged_files:
    with open(merged_file, 'r') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if 'TattooAtlas' in line:
                # Change ID
                lines[i-1] = change_value(lines[i-1], tattoo_id)

                # Change Enable
                lines[i-4] = change_value(lines[i-4], tattoo_enable)
                
        elif 'MakeUpAtlas' in line:
                # Change ID
                lines[i-1] = change_value(lines[i-1], makeup_id)

                # Change Enable
                lines[i-4] = change_value(lines[i-4], makeup_enable)

    with open(merged_file, 'w') as f:
        f.writelines(lines)


messagebox.showinfo(title='Important Info',message='Yipee!!')