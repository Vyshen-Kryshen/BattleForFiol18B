"""
Модуль с игровыми функциями.
"""
from requests import Response, get
from game_modules.game_constants import DIRECTORY_PATH


def textures_loader() -> None:
    """
    Функция для загрузки всех внутреигровых текстур
    :return: none-object value.
    """
    url_dictionary: dict[str: str] = {
        "CityLogo": "https://static.wikia.nocookie.net/spore/images/f/f5/%D0%AD%D1%82%D0%B0%D0%BF_%28%D0%93%D0%BE"
                    "%D1%80%D0%BE%D0%B4%29.png/revision/latest/scale-to-width-down/250?cb=20131017134214&path"
                    "-prefix=ru",
        "CityConcept": "https://static.wikia.nocookie.net/spore/images/3/31/%D0%9A%D0%BE%D0%BD%D1%86%D0%B5%D0%BF"
                       "%D1%82_%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%B0.png/revision/latest/scale-to-width-down/180"
                       "?cb=20210623020306&path-prefix=ru",
        "FirstCityBackground": "https://static.wikia.nocookie.net/spore/images/a/a8/Texture.png/revision/latest"
                               "/scale-to-width-down/185?cb=20191221162211&path-prefix=ru",
        "SecondCityBackground": "https://static.wikia.nocookie.net/spore/images/d/d6/2_%D0%A4%D0%BE%D0%BD_%D0%93"
                                "%D0%BE%D1%80%D0%BE%D0%B4%D0%B0.png/revision/latest/scale-to-width-down/185?cb"
                                "=20191221162326&path-prefix=ru",
        "CityBackgroundGreenCard": "https://static.wikia.nocookie.net/spore/images/e/ec/3_%D0%A4%D0%BE%D0%BD_%D0"
                                   "%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%B0.png/revision/latest/scale-to-width-down/185"
                                   "?cb=20191221174146&path-prefix=ru",
        "FirstFieldBackgroundWithPlatform": "https://static.wikia.nocookie.net/spore/images/4/47/%D0%A4%D0%BE%D0"
                                            "%BD_%D0%BF%D0%BE%D0%BB%D1%8F_%D1%81_%D0%BF%D0%BB%D0%B0%D1%82%D1%84"
                                            "%D0%BE%D1%80%D0%BC%D0%BE%D0%B9.png/revision/latest/scale-to-width"
                                            "-down/185?cb=20191221174219&path-prefix=ru",
        "SecondFieldBackgroundWithPlatform": "https://static.wikia.nocookie.net/spore/images/3/35/2_%D0%9F%D0%BE"
                                             "%D0%BB%D1%8F_%D0%B0%D0%BA%D0%B0_%D0%A4%D0%B5%D1%80%D0%BC%D0%B0.png"
                                             "/revision/latest/scale-to-width-down/185?cb=20191221162340&path"
                                             "-prefix=ru",
        "FieldOfFarmWithBrickFloor": "https://static.wikia.nocookie.net/spore/images/2/20/%D0%9F%D0%BE%D0%BB%D1"
                                     "%8F_%D0%B0%D0%BA%D0%B0_%D0%A4%D0%B5%D1%80%D0%BC%D0%B0.png/revision/latest"
                                     "/scale-to-width-down/185?cb=20191221162310&path-prefix=ru",
        "FieldOfFarmWithoutBrickFloor": "https://static.wikia.nocookie.net/spore/images/9/97/%D0%A4%D0%BE%D0%BD_"
                                        "%D0%BF%D0%BE%D0%BB%D1%8F_%D0%B1%D0%B5%D0%B7_%D0%BF%D0%BB%D0%B0%D1%82%D1"
                                        "%84%D0%BE%D1%80%D0%BC%D1%8B.png/revision/latest/scale-to-width-down/185"
                                        "?cb=20191221174234&path-prefix=ru",
        "BrickFloor": "https://static.wikia.nocookie.net/spore/images/2/2e/%D0%9A%D0%B8%D1%80%D0%BF%D0%B8%D1%87"
                      "%D0%BD%D1%8B%D0%B9_%D1%84%D0%BE%D0%BD.png/revision/latest/scale-to-width-down/185?cb"
                      "=20191221174305&path-prefix=ru",
        "PosterWithFoodRequirement": "https://static.wikia.nocookie.net/spore/images/9/97/%D0%9F%D0%BB%D0%B0%D0"
                                     "%BA%D0%B0%D1%82_%D1%81_%D1%82%D1%80%D0%B5%D0%B1%D0%BE%D0%B2%D0%B0%D0%BD%D0"
                                     "%B8%D0%B5%D0%BC_%D0%BF%D0%B8%D1%89%D0%B8.png/revision/latest?cb"
                                     "=20191221174618&path-prefix=ru",
        "PosterWithHouseRequirement": "https://static.wikia.nocookie.net/spore/images/2/20/%D0%9F%D0%BB%D0%B0%D0"
                                      "%BA%D0%B0%D1%82_%D1%81_%D1%82%D1%80%D0%B5%D0%B1%D0%BE%D0%B2%D0%B0%D0%BD%D0"
                                      "%B8%D1%8F_%D0%B6%D0%B8%D0%BB%D0%B8%D1%89%D0%B0.png/revision/latest?cb"
                                      "=20191221162551&path-prefix=ru",
        "Crown": "https://static.wikia.nocookie.net/spore/images/a/a9/%D0%9A%D0%BE%D1%80%D0%BE%D0%BD%D0%B0_%D0%AD"
                 "%D1%82%D0%B0%D0%BF_%D0%93%D0%BE%D1%80%D0%BE%D0%B4.png/revision/latest?cb=20191221180112&path"
                 "-prefix=ru",
        "CivilizationLogo": "https://static.wikia.nocookie.net/spore/images/d/d3/%D0%AD%D1%82%D0%B0%D0%BF_%28%D0"
                            "%A6%D0%B8%D0%B2%D0%B8%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%29.png/revision"
                            "/latest/scale-to-width-down/250?cb=20131017134031&path-prefix=ru",
        "DemoCivilizationLogo": "https://static.wikia.nocookie.net/spore/images/f/f0/Civ.gif/revision/latest/scale"
                                "-to-width-down/70?cb=20150810192539&path-prefix=ru",
        "Sporling": "https://static.wikia.nocookie.net/spore/images/4/4c/%D0%A1%D0%BF%D0%BE%D1%80%D0%BB%D0%B8%D0"
                    "%BD%D0%B3.png/revision/latest?cb=20200724134742&path-prefix=ru",
        "Warface": "https://static.wikia.nocookie.net/spore/images/b/b9/%D0%92%D0%BE%D0%B5%D0%BD%D0%BD%D0%B0%D1"
                   "%8F_%D0"
                   "%BC%D0%BE%D1%89%D1%8C%28%D0%91%D0%9B%29.png/revision/latest/scale-to-width-down/30?cb"
                   "=20191208142543"
                   "&path-prefix=ru",
        "Religion": "https://static.wikia.nocookie.net/spore/images/1/16/%D0%A0%D0%B5%D0%BB%D0%B8%D0%B3%D0%B8%D0"
                    "%BE%D0%B7"
                    "%D0%BD%D0%BE%D0%B5_%D0%B2%D0%BE%D0%B7%D0%B4%D0%B5%D0%B9%D1%81%D1%82%D0%B2%D0%B8%D0%B5%28%D0"
                    "%91%D0%9B"
                    "%29.png/revision/latest/scale-to-width-down/30?cb=20191208142620&path-prefix=ru",
        "Economy": "https://static.wikia.nocookie.net/spore/images/3/31/%D0%AD%D0%BA%D0%BE%D0%BD%D0%BE%D0%BC%D0%B8"
                   "%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B5_%D0%B2%D0%BE%D0%B7%D0%B4%D0%B5%D0%B9%D1%81%D1%82%D0%B2%D0"
                   "%B8%D0%B5%28%D0%91%D0%9B%29.png/revision/latest/scale-to-width-down/30?cb=20191208142525&path"
                   "-prefix=ru",
        "CivilizationStage": "https://static.wikia.nocookie.net/spore/images/c/c6/Civilization.png/revision"
                             "/latest?cb=20081026091413&path-prefix=ru",
        "Cosmonaut": "https://static.wikia.nocookie.net/spore/images/0/02/Starman.png/revision/latest?cb"
                     "=20081026101130&path-prefix=ru",
        "Economist": "https://static.wikia.nocookie.net/spore/images/b/bf/Economist.png/revision/latest?cb"
                     "=20081026092121&path-prefix=ru",
        "IronFist": "https://static.wikia.nocookie.net/spore/images/9/9c/Military_Strongman.png/revision/latest"
                    "?cb=20081026094352&path-prefix=ru",
        "Missioner": "https://static.wikia.nocookie.net/spore/images/a/a0/Missionary.png/revision/latest?cb"
                     "=20081026094452&path-prefix=ru",
        "SpiceBaron": "https://static.wikia.nocookie.net/spore/images/d/d7/Spice_Hoarder.png/revision/latest?cb"
                      "=20081026100845&path-prefix=ru",
        "Relentless": "https://static.wikia.nocookie.net/spore/images/c/ca/Relentless.png/revision/latest?cb"
                      "=20081026095804&path-prefix=ru",
        "Thunderer": "https://static.wikia.nocookie.net/spore/images/7/7a/Rolling_Thunder.png/revision/latest?cb"
                     "=20081026095847&path-prefix=ru",
        "Musician": "https://static.wikia.nocookie.net/spore/images/8/8d/Ghetto_Blaster.png/revision/latest?cb"
                    "=20081026093254&path-prefix=ru",
        "BrilliantCivilization": "https://static.wikia.nocookie.net/spore/images/8/8a/Adamantium_Civilization.png"
                                 "/revision/latest?cb=20081026090531&path-prefix=ru",
        "Factory": "https://static.wikia.nocookie.net/spore/images/b/bb/%D0%A0%D0%97_%D0%97%D0%B0%D0%B2%D0%BE%D0%B4"
                   ".png/revision/latest/scale-to-width-down/31?cb=20200226155740&path-prefix=ru",
        "House": "https://static.wikia.nocookie.net/spore/images/3/3e/%D0%A0%D0%97_%D0%96%D0%B8%D0%BB%D0%BE%D0%B9_%D0"
                 "%B4%D0%BE%D0%BC.png/revision/latest/scale-to-width-down/31?cb=20200226155740&path-prefix=ru",
        "EntertainmentCenter": "https://static.wikia.nocookie.net/spore/images/e/e8/%D0%A0%D0%97_%D0%A0%D0%B0%D0%B7"
                               "%D0%B2%D0%BB%D0%B5%D0%BA%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9_%D1%86%D0%B5"
                               "%D0%BD%D1%82%D1%80.png/revision/latest/scale-to-width-down/33?cb=20200226155740&path"
                               "-prefix=ru",
        "Spice": "https://static.wikia.nocookie.net/spore/images/f/f1/%D0%9F%D1%80%D1%8F%D0%BD%D0%BE%D1%81%D1%82%D1"
                 "%8C.png/revision/latest?cb=20200229142625&path-prefix=ru",
        "PlanetLogo": "https://static.wikia.nocookie.net/spore/images/3/33/%D0%98%D0%BA%D0%BE%D0%BD%D0%BA%D0%B0_%D0"
                      "%A0%D0%B0%D0%B7%D0%B4%D0%B5%D0%BB%D0%B0_%D0%9F%D0%BB%D0%B0%D0%BD%D0%B5%D1%82%D1%8B_%D0%98%D0"
                      "%B7_%D0%A1%D0%BF%D0%BE%D1%80%D0%BE%D0%BF%D0%B5%D0%B4%D0%B8%D0%B8.png/revision/latest?cb"
                      "=20200619143914&path-prefix=ru",
        "Quest": "https://static.wikia.nocookie.net/spore/images/d/d6/%D0%98%D0%BA%D0%BE%D0%BD%D0%BA%D0%B0_%D0%A0%D0"
                 "%B0%D0%B7%D0%B4%D0%B5%D0%BB%D0%B0_%D0%92%D1%81%D0%B5_%D0%98%D0%B7_%D0%A1%D0%BF%D0%BE%D1%80%D0%BE%D0"
                 "%BF%D0%B5%D0%B4%D0%B8%D0%B8.png/revision/latest?cb=20200619143311&path-prefix=ru",
        "Technical": "https://static.wikia.nocookie.net/spore/images/a/a4/%D0%98%D0%BA%D0%BE%D0%BD%D0%BA%D0%B0_%D0%A0"
                     "%D0%B0%D0%B7%D0%B4%D0%B5%D0%BB%D0%B0_%D0%A2%D0%B5%D1%85%D0%BD%D0%B8%D0%BA%D0%B0_%D0%98%D0%B7_"
                     "%D0%A1%D0%BF%D0%BE%D1%80%D0%BE%D0%BF%D0%B5%D0%B4%D0%B8%D0%B8.png/revision/latest?cb"
                     "=20200619144038&path-prefix=ru",
        "Creature": "https://static.wikia.nocookie.net/spore/images/1/10/%D0%98%D0%BA%D0%BE%D0%BD%D0%BA%D0%B0_%D0%A0"
                    "%D0%B0%D0%B7%D0%B4%D0%B5%D0%BB%D0%B0_%D0%A1%D1%83%D1%89%D0%B5%D1%81%D1%82%D0%B2%D0%B0_%D0%98%D0"
                    "%B7_%D0%A1%D0%BF%D0%BE%D1%80%D0%BE%D0%BF%D0%B5%D0%B4%D0%B8%D0%B8.png/revision/latest/scale-to"
                    "-width-down/33?cb=20200619144019&path-prefix=ru"
    }
    for key in url_dictionary.keys():
        response: Response = get(url_dictionary[key])
        with open(FR"{DIRECTORY_PATH}\{key}.png", "wb") as image_file:
            image_file.write(response.content)


if __name__ == '__main__':
    textures_loader()
