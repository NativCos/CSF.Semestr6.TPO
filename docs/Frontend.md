### Интерфейс
|Путь|Описание|
|:---|:---|
|GET /                 | начальная страница сайта |
|GET /history          | история о футбольном клубе |
|GET /contacts         | контактная информация футбольного клуба |
|GET /team             | список игроков и их позиции в команде |
|GET /matches?st=%n%          | результаты прошедших матчей и даты будущих матчей, %n% - номер страницы |
|GET /news?st=%n%             | новости о клубе, лента новостей, %n% - номер страницы |
|GET /news/%id%        | новости о клубе, конкретная новость, %id% - id новости|
|GET /contentmaker     | начальная панель контентмейкера |
|GET /contentmaker/news?st=%n% | лента новостей и доступ контентмейкера к инструменам редактирования, %n% - номер страницы|
|GET /contentmaker/news/new | запрос на создание новой новости, перенапраляет на страницу редактирование новости(новосозданной)|
|GET /contentmaker/news/%id%/edit  | конкретная новость и доступ контентмейкера к инструменам редактирования, %id% - id новости |
|POST /contentmaker/news/%id%/edit<br>?header=%header%<br>?body=%body%<br>?date=%date%|изменить новость, %id% - id новости, %header% - текст заголовка, %body% - тело новости, %date% - дата новости|
|DELETE /contentmaker/news/%id%| удалить новость, %id% - id новости|
|GET /contentmaker/matches?st=%n%  | список матчей с инструментами редактирования для контентмейкера, %n% - номер страницы |
|GET /contentmaker/matches/new|запрос на создание нового матча, перенапраляет на страницу редактирование матча(новосозданной)|
|GET /contentmaker/matches/%id%/edit  | страница редактирования матча, %id% - id матча |
|POST /contentmaker/matches/%id%/edit<br>?date=%date%<br>?score_own=%score_own%<br>?score_rival=%score_rival%<br>?rival=%rival%<br>?place_of_play=%place_of_play%| изменить матч,<br> %id% - id матча,<br> %date% - дата матча,<br> %score_own% - Счет нашей команды,<br> %score_rival% - Счет соперников,<br> %rival% - Имя команды соперников,<br> %place_of_play% - Место игры|
|DELETE /contentmaker/matches/%id%| удалить матч, %id% - id матча|
|GET /contentmaker/profile| профиль контент мейкера |
|POST /contentmaker/profile?newpass=%newpass%| изменить пароль для администратора, %newpass% - новый пароль|
|GET /siteadmin| начальная панель администратора |
|GET /siteadmin/profile| профиль администратора |
|POST /siteadmin/profile?newpass=%newpass%| изменить пароль, %newpass% - новый пароль |
|GET /siteadmin/contentmakermanager| список контентмейкеров с инструментами редактирования это списка |
|POST /siteadmin/contentmakermanager?name=%name%?mail=%mail%| создать нового контентмейкера, %name% - имя, %mail% - почта|
|DELETE /siteadmin/contentmakermanager?id=%id%| отключить доступ для контентмейкера и удалить его, %id% - индивидуальный номер |
