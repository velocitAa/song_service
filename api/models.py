from tensorflow.keras import layers
import keras
import tensorflow as tf
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras import Model, Input, Sequential

def Model_Genre_Classification(weights, input_shape, output_shape):
    inputs = keras.Input(shape=input_shape)
    x = layers.Conv2D(32, 3, activation="relu")(inputs)
    x = layers.Conv2D(64, 3, activation="relu")(x)
    block_1_output = layers.MaxPooling2D(3)(x)

    x = layers.Conv2D(64, 3, activation="relu", padding = "same")(block_1_output)
    x = layers.Conv2D(64, 3, activation="relu", padding = "same")(x)


    block_2_output = layers.add([x, block_1_output])

    x = layers.Conv2D(64, 3, activation="relu", padding = "same")(block_2_output)
    x = layers.Conv2D(64, 3, activation="relu", padding = "same")(x)

    block_3_output = layers.add([x, block_2_output])

    x = layers.Conv2D(64, 3, activation="relu",  padding = "same")(block_3_output)
    x = layers.GlobalAveragePooling2D()(x)
    x = layers.Dense(256, activation = "relu")(x)
    x = layers.Dropout(0.5)(x)
    outputs = layers.Dense(output_shape, activation = 'softmax')(x)

    model_genre_classification = keras.Model(inputs, outputs, name = "Resnet")
    model_genre_classification.load_weights(weights)

    return model_genre_classification

def Model_Mood_Classification(weights, input_shape, output_shape):
    base_model = tf.keras.applications.MobileNet(weights = 'imagenet', include_top = False)
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(256, activation = 'relu')(x)
    x = Dense(128, activation = 'relu')(x)
    x = Dense(64, activation = 'relu')(x)
    preds = Dense(output_shape, activation = 'softmax')(x)

    for layer in base_model.layers[:20]: layer.trainable=False
    model= Model(inputs=base_model.input, outputs=preds)
    inputs = Input(shape=input_shape)
    model_mood_classification = Sequential()
    model_mood_classification.add(inputs)
    model_mood_classification.add(layers.Conv2D(32, 3, activation="relu"))
    for layer in model.layers[2:]:
        model_mood_classification.add(layer)

    model_mood_classification.load_weights(weights)

    return model_mood_classification