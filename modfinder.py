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

		menu = """
 /$$      /$$           /$$                                            
| $$  /$ | $$          | $$                                            
| $$ /$$$| $$  /$$$$$$ | $$  /$$$$$$$  /$$$$$$  /$$$$$$/$$$$   /$$$$$$ 
| $$/$$ $$ $$ /$$__  $$| $$ /$$_____/ /$$__  $$| $$_  $$_  $$ /$$__  $$
| $$$$_  $$$$| $$$$$$$$| $$| $$      | $$  \\ $$| $$ \\ $$ \\ $$| $$$$$$$$
| $$$/ \\  $$$| $$_____/| $$| $$      | $$  | $$| $$ | $$ | $$| $$_____/
| $$/   \\  $$|  $$$$$$$| $$|  $$$$$$$|  $$$$$$/| $$ | $$ | $$|  $$$$$$$
|__/     \\__/ \\_______/|__/ \\_______/ \\______/ |__/ |__/ |__/ \\_______/
-------------------------------------------------------------------------------
made by frankielivada22
		"""
		faded_text, colorerer = redgreenblue(menu)
		print(faded_text)

		ask = input('Enter name of the mod: ')
		print("")

		# r=root, d=directories, f = files
		for r, d, f in os.walk(incergency_mods_path):
			for file in f:
				if file.endswith(".json"):
					file_name = os.path.join(r, file)
					with open(file_name, 'r') as f:
						file_lines = f.read()
					if ask in file_lines:
						print(f"{ask} was found inside")
						print(f"Path: {file_name.rstrip('State.json')}")
						file_number = d[0]
						print(f"Mod number: {file_number}\n")
					else:
						pass
		print("")
		os.system('pause')
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


