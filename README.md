# Моделирование затменных звёздных систем (CMoEBS)

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Made with Markdown](https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg)](http://commonmark.org)
[![Windows](https://svgshare.com/i/ZhY.svg)](https://svgshare.com/i/ZhY.svg)
[![Wakatime](https://wakatime.com/badge/user/ede740b4-c066-46b1-94e3-8631a44edbbc/project/68c47a79-df9e-405c-aacb-26f8a66702d4.svg)](https://wakatime.com/@matveypol003)
[![GitHub commits](https://flat.badgen.net/github/commits/PM-95025/scientificProject)](https://GitHub.com/PM-95025/scientificProject/commit/)
[![Dependabot](https://flat.badgen.net/github/dependabot/PM-95025/scientificProject)](https://github.com/PM-95025/scientificProject/network/updates)
[![GitHub latest commit](https://flat.badgen.net/github/last-commit/PM-95025/scientificProject)](https://github.com/PM-95025/scientificProject/commits)
[![Maintainability](https://api.codeclimate.com/v1/badges/c366428254a5bf01ae87/maintainability)](https://codeclimate.com/github/PM-95025/scientificProject/maintainability)

Главный файл - `./main.py`

Файл конфигурации - `./data/data.ini`

Презентация - `./src/Моделирование_затменной_звёздной_системы.pptx`

#### Используемые приближения:
- Все прохождения _центральные_
- Обе звезды _всегда_ находятся на _одинаковом_ расстоянии от наблюдателя, равном 10 пк
- Потемнения звезды к краю _не существует_


#### Используемые интернет-источники:
1. https://forum.sources.ru/index.php?showtopic=9381 - тема с форума Sources.Ru (задача о пересечении двух кругов)
2. https://ru.wikipedia.org/wiki/Уравнение_Кеплера#Приближённые_методы
3. Официальная документация к библиотеке matplotlib:
	- https://matplotlib.org/stable/gallery/lines_bars_and_markers/fill_between_demo.html
	- https://matplotlib.org/stable/gallery/shapes_and_collections/hatch_style_reference.html
	- https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html
4. Обсуждения на форуме StackOverflow (настройка matplotlib):
	- https://stackoverflow.com/questions/28132936/axes-invert-axis-does-not-work-with-sharey-true-for-matplotlib-subplots
	- https://stackoverflow.com/questions/56894740/matplotlib-why-does-setting-grid-with-pyplot-setp-causes-error
	- https://stackoverflow.com/questions/19626530/python-xticks-in-subplots
	- https://stackoverflow.com/questions/5993206/is-it-possible-to-have-multiple-pyplot-windows-or-am-i-limited-to-subplots
5. Обсуждения на форуме OverCoder (настройка matplotlib):
	- https://overcoder.net/q/1195838/как-мне-заполнить-область-только-штриховкой-без-фона-в-matplotlib-20
6. https://www.geeksforgeeks.org/how-to-implement-linear-interpolation-in-python/amp/ - учебный материал с портала GeeksForGeeks "How to implement linear interpolation in Python?"
7. Информация о двойных звёздах (в т.ч. их параметры)
	- https://en.wikipedia.org/wiki/AD_Andromedae
	- https://en.wikipedia.org/wiki/CG_Cygni
    - https://en.wikipedia.org/wiki/AR_Cassiopeiae
	- https://www.scirp.org/journal/paperinformation.aspx?paperid=77049 (TT And)
	- http://www.physics.sfasu.edu/astro/ebstar/ebstar.html (битая ссылка, архивная версия на [WayBack Machine](https://web.archive.org/web/20220501021646/http://www.physics.sfasu.edu/astro/ebstar/ebstar.html) - статья из электронной библиотеки SFASU "ECLIPSING BINARY STARS. A Simple Model for Computing Light Curves"
	- http://crydee.sai.msu.ru/ak4/Chapt_11_3_154.htm - статья из электронной библиотеки ГАИШ "§ 154. Общие характеристики двойных систем"
