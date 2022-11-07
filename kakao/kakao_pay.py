from kakao.kakao_admin import kakao_admin

class kakao_pay(kakao_admin):
    myaccount = ""
    myprice = 0
    def __init__(self, _id, _password, _name, _myaccount, _myprice) -> None:
        self.myaccount = _myaccount
        self.myprice = _myprice
        super().set_id(_id)
        super().set_password(_password)
        super().set_name(_name)
        
        pass