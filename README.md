Hello there! Welcome to GitHub recommendation system repository.

### Overview
The system performance solves several types of machine learning tasks: classification, recognition and unsupervised learning. For this tasks was used computer vision technologies, transformers and metric models (RandomForestClassifier, DecisionTreeClassifier an etc.). The logging of models was produced by Wandb, plotting of data presentation by plotly

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
