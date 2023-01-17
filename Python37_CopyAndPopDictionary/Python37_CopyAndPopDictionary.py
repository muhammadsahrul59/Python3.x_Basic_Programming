# copy dictionary

teman_teman = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dung surudung",
    "sep":"asep si kasep",
    "cuy":"ucuy surucuy"
}

friends = teman_teman.copy()

print(f"teman_teman: {teman_teman}\n")
print(f"friends: {friends}\n")

teman_teman["cup"]="ucup si keren"
print(f"teman_teman: {teman_teman}\n")
print(f"friends: {friends}\n")

# pop dictionary (diambil berdasarkan key)
dataAsep = friends.pop("sep")
print(f"data Asep = {dataAsep}\n")
print(f"friends = {friends}\n")

# popitem dictionary (diambil key terakhir)
dataTerakhir = friends.popitem()
print(f"data terakhir = {dataTerakhir}\n")
print(f"friends = {friends}\n")