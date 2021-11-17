from os import system as sy

#既存のskコマンド(読み上げ)を実行する関数
def sk(str):
	with open("d.txt","w",encoding="utf-8")as f:f.write(str)
	sy("sk -f d.txt")
