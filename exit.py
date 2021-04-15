from save_data import save

def exit():
	pil = input("Apakah anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
    if pil == "y":
		save()