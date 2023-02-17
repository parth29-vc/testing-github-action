import os
import cv2
import tensorflow as tf
from keras.models import load_model
from dotenv import load_dotenv

# It will load the environment variables from the file
load_dotenv()

classification_model = load_model(os.getenv("ML_MODEL_PATH"))
print("Loading weights: ", os.getenv("ML_MODEL_PATH"))


def preprocess_image(filepath):
    try:
        if os.path.exists(os.path.join(os.getenv("DOCKER_VOLUME"), filepath)):
            input_image = cv2.imread(os.path.join(os.getenv("DOCKER_VOLUME"), filepath))
        else:
            input_image = cv2.imread(os.path.join(os.getenv("DOCKER_COM_VOLUME"), filepath))
    except:
        input_image = cv2.imread(os.path.join(os.getenv("DOCKER_COM_VOLUME"), filepath))

    resized_image = cv2.resize(input_image, (224,224))
    return resized_image

def run_inference(imagepath):
    # import pdb; pdb.set_trace()

    # Image preprocessing
    image = preprocess_image(imagepath)

    # We need to format the input to match the training data
    imgfeatures = image.reshape(1, image.shape[0], image.shape[1], image.shape[2])
    shape_name = ['Apple', 'Axe', 'Bangles', 'Bell', 'Bird', 'Boat', 'Book', 'Bottle', 'Bow', 'Bulb', 'ButterFly', 'Cap', 'Circle', 'Damru', 'Dhol (Drum)', 'Diya', 'Eye', 'Fire', 'Fish', 'Flag', 'Flower', 'Gada', 'Glass', 'Goggles', 'Hair', 'Hand', 'Heart', 'House', 'Kite', 'Leaf', 'Lips', 'Lotus', 'Mountains', 'Mustache', 'Person', 'Pot', 'River', 'Shield', 'Smile', 'Snake', 'Square', 'Star', 'Sun', 'Swastik', 'Sword', 'Tarazu', 'Tree', 'Triangle', 'Trishul', 'Window']

    # The generator loaded the values as floating point numbers
    # and normalized the pixel values, so...
    imgfeatures = imgfeatures.astype('float32')
    imgfeatures /= 255

    # Use the model to predict the image class
    class_probabilities = classification_model.predict(imgfeatures)
    prediction_probabilities = tf.math.top_k(class_probabilities, k=4)

    # Find the class predictions with the highest predicted probability
    # index = int(np.argmax(class_probabilities, axis=1)[0])

    top_k_values = prediction_probabilities.values.numpy()[0]
    top_k_values = [round(prediction_probabilities.values.numpy()[0][i]*100, 2) for i, val in enumerate(top_k_values)]
    print("percentage",top_k_values)

    top_k_indices = prediction_probabilities.indices.numpy()[0].tolist()

    print("Shape name1:",shape_name[top_k_indices[0]])
    print("Shape name2:",shape_name[top_k_indices[1]])
    print("Shape name3:",shape_name[top_k_indices[2]])
    print("Shape name4:",shape_name[top_k_indices[3]])


    output = dict()
    if top_k_values[0] > 60.0:
        output["shapeClasses"] = [
            {
                "shape" : top_k_indices[0],
                "probability" : top_k_values[0],
                "shape_name" : shape_name[top_k_indices[0]]
            },
            {
                "shape" : top_k_indices[1],
                "probability" : top_k_values[1],
                "shape_name" : shape_name[top_k_indices[1]]
            },
            {
                "shape" : top_k_indices[2],
                "probability" : top_k_values[2],
                "shape_name" : shape_name[top_k_indices[2]]
            },
            {
                "shape" : top_k_indices[3],
                "probability" : top_k_values[3],
                "shape_name" : shape_name[top_k_indices[3]]
            },
        ]
    else:
        output = None
        
    print("Output is:",output)

    return output