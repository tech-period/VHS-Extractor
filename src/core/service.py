import os

class service():
    def __init__(self) -> None:
        pass

    def get_drives(self):
        # 参考URL
        # https://www.webdevqa.jp.net/ja/python/python%E3%81%A7%E5%88%A9%E7%94%A8%E5%8F%AF%E8%83%BD%E3%81%AA%E3%81%99%E3%81%B9%E3%81%A6%E3%81%AE%E3%83%89%E3%83%A9%E3%82%A4%E3%83%96%E6%96%87%E5%AD%97%E3%82%92%E4%B8%80%E8%A6%A7%E8%A1%A8%E7%A4%BA%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95%E3%81%AF%E3%81%82%E3%82%8A%E3%81%BE%E3%81%99%E3%81%8B%EF%BC%9F/957989187/
        return [ chr(x) + ":" for x in range(65,90) if os.path.exists(chr(x) + ":") ]
