### Интерфейс
|Путь|Описание|
|:---|:---|
|GET /                 | начальная страница сайта |
|GET /history          | история о футбольном клубе |
|GET /contacts         | контактная информация футбольного клуба |
|GET /team             | список игроков и их позиции в команде |
|GET /matches          | результаты прошедших матчей и даты будущих матчей|
|GET /news             | новости о клубе, лента новостей |
|GET /news/%id%        | новости о клубе, конкретная новость, %id% - id новости|
|GET /contentmaker     | начальная панель контентмейкера |
|GET /contentmaker/news| лента новостей и доступ контентмейкера к инструменам редактирования|
|GET /contentmaker/news/new | запрос на создание новой новости, страница создания новости|
|POST /contentmaker/news/new<br>?id=%id%<br>&header=%header%<br>&body=%body%<br>&date=%date%|создать новость, %id% - id новости, %header% - текст заголовка, %body% - тело новости, %date% - дата новости|
|DELETE /contentmaker/news?id=%id%| удалить новость, %id% - id новости|
|GET /contentmaker/matches | список матчей с инструментами редактирования для контентмейкера |
|GET /contentmaker/matches/new|страница с формой создания нового матча|
|POST /contentmaker/matches/new<br>?&date=%date%<br>&score_own=%score_own%<br>&score_rival=%score_rival%<br>&rival=%rival%<br>&place_of_play=%place_of_play%| создать матч,<br> %date% - дата матча,<br> %score_own% - Счет нашей команды,<br> %score_rival% - Счет соперников,<br> %rival% - Имя команды соперников,<br> %place_of_play% - Место игры|
|GET /contentmaker/matches/change?id=%id%|страница с формой изменения матча, %id% - id матча|
|POST /contentmaker/matches/change<br>?id=%id%<br>&date=%date%<br>&score_own=%score_own%<br>&score_rival=%score_rival%<br>&rival=%rival%<br>&place_of_play=%place_of_play%| изменить матч,<br> %id% - id матча,<br> %date% - дата матча,<br> %score_own% - Счет нашей команды,<br> %score_rival% - Счет соперников,<br> %rival% - Имя команды соперников,<br> %place_of_play% - Место игры|
|DELETE /contentmaker/matches?id=%id%| удалить матч, %id% - id матча|
|GET /contentmaker/profile| профиль контент мейкера |
|POST /contentmaker/profile?newpass=%newpass%| изменить пароль для администратора, %newpass% - новый пароль|
|GET /siteadmin| начальная панель администратора |
|GET /siteadmin/profile| профиль администратора |
|POST /siteadmin/profile?newpass=%newpass%| изменить пароль, %newpass% - новый пароль |
|GET /siteadmin/contentmakermanagers| список контентмейкеров с инструментами редактирования это списка |
|POST /siteadmin/contentmakermanagers?login=%login%&mail=%mail%| создать нового контентмейкера, %login% - login, %mail% - почта|
|DELETE /siteadmin/contentmakermanagers?id=%id%| отключить доступ для контентмейкера и удалить его, %id% - индивидуальный номер |
|GET /login|войти как администратор или контент мейкер|
|POST /login<br>?login=%login%<br>&password=%password%|войти как администратор или контент мейкер|
|GET /logout|выйти|