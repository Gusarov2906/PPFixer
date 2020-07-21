#prog to fix Pick and place files
import shutil
import pathlib
import os
import time
print("-----------------Программа для исправления PickAndPlace файлов----------------------")
print("---Замена символа ',' внутри двойных ковычек вместе с удалением самих ковычек-------")
print("------------------------------------Инструкция:-------------------------------------")
print("1) Пишем имя файла, который хотим исправить(предварительно положив его в папку work)")
print("2) Программа создаст копию файла и сделает исправления в ней------------------------")
print("3) На экран будут выведены номера исправленных строчек(если таковые присутствуют)---")
print("4) Программа напишет об успешном выполнении(или выведет ошибку)---------------------")
print("5) В папке work будет лежать готовый файл(к названию добавлена строка _fixed)-------")
print("------------------------------------------------------------------------------------")
#while(True):
print()
home = os.getcwd()
os.chdir(f'{os.getcwd()}\work')
filename = input("Напишите имя файла: ")
try:
	new_file_text = []
	#read txt and write to buffer
	with open(filename,'r') as f:
		i = 0
		for line in f:
			new_file_text.append(line)
	name_without_type = filename.rstrip('.rtp')
	new_file= f'{name_without_type}'+'_fixed.rpt'
	path = pathlib.Path(new_file)
	shutil.copyfile(filename,new_file)
	#if path.exists():
	#	print("Невозможно создать резервную копию файла т.к. она уже существует")
	#else:
	#	shutil.copyfile(filename,f'{name_without_type}'+'_old.rpt')
	#	print("Резервная копия создана успешно")
	#rewrite file to fix errors
	with open(new_file,'w') as f:
		#fix in buffer
		for line in new_file_text:
			i += 1
			#print(line)
			if '"' in line:
				tmp = line[line.find('"')+1:line.rfind('"')]
				tmp = tmp.replace(',','.')
				tmp = tmp.replace('"','')
				print('Старая строка: '+ line[line.find('"'):line.rfind('"')+1])
				line = line.replace(line[line.find('"'):line.rfind('"')+1],tmp)
				print(f"Замена в {i} строке прошла успешно")
				print('Новая строка: '+ tmp)
				print()
			#write to file
			f.write(line)
	print("Завершено без ошибок!")
except Exception as e:
	print(e)
os.chdir(home)
input("Напишите любой символ чтобы выйти:")
