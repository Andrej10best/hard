import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.adult_mode = adult_mode
        self.title = title
        self.duration = duration
        time_now = 0


class UrTube:

    def __init__(self):
        self.users = users
        self.videos = videos
        self.current_user = None

    def log_in(self, login, password):                                      # Вход пользователя по логину
        for i in users:
            if i['nickname'] == login and i['password'] == password:
                self.current_user = i['nickname']
                print(f'Вход под {self.current_user}')
            else:
                print('Пользователь не зарегистрирован')

    def register(self, nickname, password, age):                            # Регистрация пользователя и добавление
        user = {"nickname": nickname, "password": password, "age": age}     # его в список пользователей
        for i in users:
            if i['nickname'] == user['nickname']:
                print(f'Пользователь {nickname} уже существует')

        users.append(user)
        self.current_user = user['nickname']

    def log_out(self):                                                      # Сбрасывает текущего пользователя
        self.current_user = None

    def add(*args):                                                         # Добавление видео в список videos
        for video in args:
            if isinstance(video, Video):
                videos.append(video)

    def get_videos(self, word):                                             # Поиск видео по названию
        self.is_not_used()
        titles = []
        for video in videos:
            if word.lower() in video.title.lower():
                titles.append(video.title)
        return titles

    def watch_video(self, name_film):                                       # Просмотр видео
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        pass    # Предполагаю, что сюда нужно вставить фильтр по возрасту
        print('Вам нет 18 лет, пожалуйста покиньте страницу')

    def is_not_used(self):
        pass


if __name__ == '__main__':
    users = []
    videos = []
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года',
               200)
    v2 = Video('Для чего девушкам парень программист?',
               10,
               adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    # ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    # ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    # ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    # print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    # ur.watch_video('Лучший язык программирования 2024 года!')
