import winreg
import time
import sys
import os
import json

def clear():
	os.system('cls')

INC_MODS_FOLDER = os.getenv('APPDATA') + "\\inc_mod_finder"
config_path = INC_MODS_FOLDER + '\\config.json'
global_steam_path = ''

set_title = 'title Where TF is that mod!?!? by frankielivada22'
os.system(set_title)

def read_json():
	config_file = open(config_path, 'r')
	config = json.load(config_file)
	config_file.close()

	done_setup = str(config["done_setup"])
	global steam_path
	steam_path = str(config["steam_path"])

	return done_setup

def setup():
	print(f'Initialising setup on: {INC_MODS_FOLDER}')
	file_exists = os.path.exists(INC_MODS_FOLDER)
	if file_exists == False:
		print("File not found, creating file...")
		os.system(f'mkdir {INC_MODS_FOLDER}')
		time.sleep(0.2)
	else:
		print("File found!")

	file_exists = os.path.exists(config_path)
	if file_exists == False:
		print("File not found, creating file...")
		with open(config_path, 'w', encoding='utf-8') as f:
			f.write("""
{
	
}
				""")
		time.sleep(0.2)
	else:
		print("Config file found!")


	print('Done')
	print('Regdit:')

	#Get steam install path:
	key64 = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\WOW6432Node\\Valve\\Steam'
	key32 = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Valve\\Steam'
	
	try:
		hkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\WOW6432Node\Valve\Steam')
	except:
		try:
			hkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'HKEY_LOCAL_MACHINE\SOFTWARE\Valve\Steam')
		except:
			hkey = None

	#print(hkey)
	steam_path = winreg.QueryValueEx(hkey, 'InstallPath')
	print(steam_path[0])

	#Append json to path in appdata
	with open(config_path, 'r', encoding='utf-8') as fp:
		listobj = json.load(fp)
	bruhmoment = {'done_setup': True}
	listobj.update(bruhmoment)
	with open(config_path, 'w', encoding='utf-8') as json_file:
		json.dump(listobj, json_file, indent=4)
	time.sleep(3)

	with open(config_path, 'r', encoding='utf-8') as fp:
		listobj = json.load(fp)
	bruhmoment = {'steam_path': f'{steam_path[0]}'}
	listobj.update(bruhmoment)
	with open(config_path, 'w', encoding='utf-8') as json_file:
		json.dump(listobj, json_file, indent=4)
	time.sleep(3)


def main():
	while True:
		#D:\Program Files (x86)\Steam\steamapps\common\sandstorm\Insurgency\Mods\modio
		incergency_mods_path = f'{steam_path}\\steamapps\\common\\sandstorm\\Insurgency\\Mods\\modio'

		def redgreenblue(text):
			os.system(""); faded = ""

			red, green, blue = 102, 255, 255

			for line in text.splitlines():
				faded += (f"\033[38;2;{red};{green};{blue}m{line}\033[0m\n")
				if not blue == 0:
					blue -= 20
					if blue < 0:
						blue = 0

			colorerer = f'\033[38;2;{red};{green};{blue}m'
			return faded, colorerer

		menu = f"""
 /$$      /$$           /$$                                            
| $$  /$ | $$          | $$                                            
| $$ /$$$| $$  /$$$$$$ | $$  /$$$$$$$  /$$$$$$  /$$$$$$/$$$$   /$$$$$$ 
| $$/$$ $$ $$ /$$__  $$| $$ /$$_____/ /$$__  $$| $$_  $$_  $$ /$$__  $$
| $$$$_  $$$$| $$$$$$$$| $$| $$      | $$  \\ $$| $$ \\ $$ \\ $$| $$$$$$$$
| $$$/ \\  $$$| $$_____/| $$| $$      | $$  | $$| $$ | $$ | $$| $$_____/
| $$/   \\  $$|  $$$$$$$| $$|  $$$$$$$|  $$$$$$/| $$ | $$ | $$|  $$$$$$$
|__/     \\__/ \\_______/|__/ \\_______/ \\______/ |__/ |__/ |__/ \\_______/
-------------------------------------------------------------------------------
ISMF - made by frankielivada22

Steam Path: {steam_path}
ModIO Path: {steam_path}steamapps\\common\\sandstorm\\Insurgency\\Mods\\modio

[1] List all mods     
[2] Find a mod        
[3] Delete all mods   
[4] Show config file content 

		"""
		faded_text, colorerer = redgreenblue(menu)
		print(faded_text)

		ask = input('Enter option: ')
		if ask == "1":
			print("")
			string = ''
			# r=root, d=directories, f = files
			for r, d, f in os.walk(incergency_mods_path):
				for file in f:
					if file.endswith(".json"):
						file_name = os.path.join(r, file)
						file_number = d[0]
						#print(file_name)

						with open(file_name, "rb") as read_file:
							#print(read_file)
							json_object = json.load(read_file)
						anothervalue = f"""
(
	Mod Name: {json_object['name']}
	Path: {file_name.rstrip('State.json')}
	Mod Number: {file_number}
)
						"""
						string = string + anothervalue
						print(anothervalue)

			print("")
			while True:
				ask = input('Would you like to save this? (y / n): ')
				if ask == "y":
					with open('ModOut.txt', 'w', encoding='utf-8') as f:
						f.write(string)
					print("Saved to ModOut.txt")
					time.sleep(1)
					break
				elif ask == "n":
					break
				else:
					pass
			os.system('pause')
		elif ask == "2":
			ask = input('Enter the mod number: ')
			print("")
			# r=root, d=directories, f = files
			for r, d, f in os.walk(incergency_mods_path):
				for file in f:
					if file.endswith(".json"):
						file_name = os.path.join(r, file)
						file_number = d[0]
						#print(file_name)

						with open(file_name, "rb") as read_file:
							#print(read_file)
							json_object = json.load(read_file)
							mod_name = json_object['name']

						if ask.lower() == mod_name.lower():
							print("Found")
							anothervalue = f"""
(
	Mod Name: {mod_name}
	Path: {file_name.rstrip('State.json')}
	Mod Number: {file_number}
)
							"""
							print(anothervalue)
						else:
							pass

			print("")
			os.system('pause')
		elif ask == "3":
			while True:
				ask = input('Are you sure (y / n)?: ')
				if ask == 'y':
					for r, d, f in os.walk(incergency_mods_path):
						for file in f:
							if file.endswith(".json"):
								file_name = os.path.join(r, file)
								with open(file_name, "rb") as read_file:
									json_object = json.load(read_file)
								print(f'Deleting: {json_object["name"]}')
								os.system(f'del {file_name.rstrip("State.json")}')

					print("Deleted all mods...")
					os.system('pause')
					break
				elif ask == 'n':
					break
				else:
					pass
		elif ask == "4":
			mod_list = []
			for r, d, f in os.walk(incergency_mods_path):
				for file in f:
					if file.endswith(".json"):
						file_name = os.path.join(r, file)
						with open(file_name, "rb") as read_file:
							json_object = json.load(read_file)
						mod_list.append(json_object["name"])
			c = 0
			for mod in mod_list:
				print(f'[{c}]: {mod}')
				c += 1
			while True:
				ask = input('Number of mod: ')
				if int(ask) > len(mod_list):
					print("Invalid mod selected...")
				elif int(ask) < -1:
					print("Invalid mod selected...")
				else:
					c = 0
					done = False
					for r, d, f in os.walk(incergency_mods_path):
						if done == True:
							break
						for file in f:
							if done == True:
								break
							if file.endswith(".json"):
								file_name = os.path.join(r, file)
								if c == int(ask):
									with open(file_name, "rb") as read_file:
										json_object = json.load(read_file)
									print(json_object)
									done = True
									break
								else:
									c += 1
		else:
			print("Invalid input.")
			time.sleep(1)
		
		clear()
				



if __name__ == '__main__':
	try:
		done_setup = read_json()
	except:
		setup()
	done_setup = read_json()
	if done_setup == False or done_setup == None:
		setup()
	
	print("Done setup!")
	clear()

	main()


