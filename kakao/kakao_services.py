from kakao.kakao_admin import kakao_admin

class kakao_games(kakao_admin):
    kakao_admin_info = None
    games_list = []

    def __init__(self, _kakao_admin) -> None:
        self.kakao_admin_info = _kakao_admin
        pass

    def append_service(self, any_games):
        self.games_list.append(any_games)

    def __str__(self) -> str:
        
        return super().__str__()

        super().set_id(k_a._id)
        super().set_password(k_a._password)
        super().set_name(k_a._name)
        
        pass