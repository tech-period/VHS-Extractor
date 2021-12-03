asset_path = "./src/light_capture/asset/"

dic = {
    "rec" : asset_path + "rec_button.png",
    "stop" : asset_path + "stop_button.png",
    "setting" : asset_path + "setting_button.png",
    "destination" : asset_path + "destination.png",
    "ok" : asset_path + "ok_button.png",
    "cancel" : asset_path + "cancel_button.png",
    "trashbox" : asset_path + "trashbox.png",
}

def get(name):
    return dic[name]