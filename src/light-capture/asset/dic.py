asset_path = "./src/light-capture/asset/"

dic = {
    "rec" : asset_path + "rec_button.png",
    "stop" : asset_path + "stop_button.png",
    "trashbox" : asset_path + "trashbox.png",
}

def get(name):
    return dic[name]