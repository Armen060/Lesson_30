class MyShows:
    def __init__(self, title, platform, release_year, current_episode=1, user_rating=None, main_cast=[]):
        self.__title = title
        self.__platform = platform
        self.__release_year = release_year
        self.__current_episode = current_episode
        self.__user_rating = user_rating
        self.__main_cast = main_cast

    def get_title(self):
        return self.__title

    def get_platform(self):
        return self.__platform

    def get_release_year(self):
        return self.__release_year

    def get_current_episode(self):
        return self.__current_episode

    def set_current_episode(self, episode):
        self.__current_episode = episode

    def get_user_rating(self):
        return self.__user_rating

    def set_user_rating(self, rating):
        if rating is not None and 1 <= rating <= 10:
            self.__user_rating = rating
        else:
            print("Invalid rating. Please provide a rating between 1 and 10.")

    def del_user_rating(self):
        del self.__user_rating

    def get_main_cast(self):
        return self.__main_cast

    def update_main_cast(self, cast_list):
        self.__main_cast = cast_list

    def get_full_info(self):
        return (f"Title: {self.__title}, Platform: {self.__platform},"
                f" Release Year: {self.__release_year}, Current Episode: "
                f"{self.__current_episode}, User Rating: {self.__user_rating}, "
                f"Main Cast: {self.__main_cast}")


s = MyShows("Madonna", "Netflix", 1990, 45, 8, ["Alla", "Mickel"])
print(s.get_full_info())
