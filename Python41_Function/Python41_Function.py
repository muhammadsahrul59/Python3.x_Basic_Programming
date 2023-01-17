'''Membuat fungsi'''

def hello_world():
    '''fungsi menampilkan hello world'''
    print("hello world")
    print("Kepada Ucup Surucup")
    print("Dan juga kepada Otong Surotong")

hello_world()
hello_world()

#fungsi() // tidak akan bisa apabila pemanggilan fungsi sebelum dibuat

def fungsi():
    '''pemanggilan fungsi harus setelah dibuat'''
    print("ini adalah fungsi")

fungsi()