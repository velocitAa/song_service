
[ENG] Hello there! Welcome to GitHub recommendation system repository.

### Overview
The system performance solves several types of machine learning tasks: classification, recognition and unsupervised learning. For this tasks was used computer vision technologies, transformers and metric models (RandomForestClassifier, DecisionTreeClassifier and etc.). The logging of models was produced by Wandb, plotting of data presentation by plotly

### Features
- Recommendations based on song features
- Songs classifiaction by genre and by mood
- Songs recognition by hash of spectogramm's peaks and cosine similarity
- Gradio interface which help to see performance of recommendation system 

### Getting Started
To start using recommendation system, simply clone this repository to your local machine. Make sure to have the necessary dependencies installed from 'requirements.txt' before running the system. After this go to "api" folder and run gradio_interface.py 

### Usage
Once the system is up and running, you can start exploring the api. There are three pages: Recommendation, Music Classification and Song recognition
#### Recommendation contains:
- Textbox 'song_list' and slider 'n_songs'. Song_list is a sequence of name of song and year of song for which we want to get a recommendation. N_songs is a number of songs to be recommend 
- Examples. There are examples for input values for quickly start
- Output. There are recommendations which consist of name and artists
#### Music classification contains:
- Type of classification. RadioButton which allow to select type of classification
- Input. Input type is a song for classification
- Output. Output is labels of classes with probability of belonging
#### Song recognition contains:
-  Input. Input type is a song for classification
-  Output. This is name of song which was recognised 

### Contributing
Welcome contributions from the community to enhance the functionality and performance of our recommendation system. If you have ideas for new features or improvements, please submit a pull request or open an issue for discussion.

### Contact
If you have any questions, feedback, or inquiries about our recommendation system, please feel free to reach out to us at [te200228@gmail.com].

Thank you for checking out our GitHub recommendation system. We hope you find it useful and enjoy discovering new repositories that inspire your coding journey! 🚀

Happy coding! 🤖🌟


[RUS] Привет! Добро пожаловать в репозиторий системы рекомендаций GitHub. 

### Обзор 
Работа системы решает несколько типов задач машинного обучения: классификацию, распознавание и обучение без учителя. Для этих задач использовались технологии компьютерного зрения, трансформеры и метрические модели (RandomForestClassifier, DecisionTreeClassifier и т. д.). Журналирование моделей осуществлялось с помощью Wandb, построение графиков представления данных - с помощью plotly. 

### Особенности 
- Рекомендации на основе особенностей песен
- Классификация песен по жанру и настроению
- Распознавание песен по хэшу пиков спектрограммы и косинусной схожести
- Интерфейс Gradio, который помогает увидеть производительность системы рекомендаций
  
### Начало работы
  Чтобы начать использовать систему рекомендаций, просто клонируйте этот репозиторий на свой локальный компьютер. Убедитесь, что у вас установлены необходимые зависимости из 'requirements.txt' перед запуском системы. После этого перейдите в папку "api" и запустите gradio_interface.py
  
### Использование 
Как только система запущена, вы можете начать исследовать API. Есть три страницы: Рекомендации, Классификация музыки и Распознавание песен 

#### Рекомендации содержат: 
- Текстовое поле 'song_list' и ползунок 'n_songs'. Song_list - это последовательность названия песни и года песни, для которой мы хотим получить рекомендацию. N_songs - количество рекомендуемых песен
- Примеры. Есть примеры входных значений для быстрого старта
- Результат. Есть рекомендации, состоящие из названия и исполнителей
#### Классификация музыки содержит: 
- Тип классификации. Переключатель, который позволяет выбрать тип классификации
- Ввод. Тип ввода - песня для классификации
- Вывод. Вывод - метки классов с вероятностью принадлежности
#### Распознавание песен содержит: 
- Ввод. Тип ввода - песня для классификации
- Вывод. Это название песни, которая была распознана
  
### Содействие 
Мы приветствуем вклад сообщества в улучшение функциональности и производительности нашей системы рекомендаций. Если у вас есть идеи для новых функций или улучшений, пожалуйста, отправьте запрос на включение или откройте обсуждение. 

### Контакты 
Если у вас есть вопросы, отзывы или запросы о нашей системе рекомендаций, не стесняйтесь обращаться к нам по адресу [te200228@gmail.com] 

Спасибо за ознакомление с нашей системой рекомендаций GitHub. Мы надеемся, что вы найдете ее полезной и насладитесь открытием новых репозиториев, которые вдохновят ваше программирование! 🚀 

Счастливого кодинга! 🤖🌟
