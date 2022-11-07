from kakao.kakao_admin import kakao_admin

class kakao_talk(kakao_admin):
    myfriend = []
    def __init__(self, _id, _password, _name, _myfriend) -> None:
        self.myfriend = _myfriend
        super().set_id(_id)
        super().set_password(_password)
        super().set_name(_name)
        
        pass