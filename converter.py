import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_saved_model('model_out', signature_key='predict')
tflite_quantized_model = converter.convert()
open("model.tflite", "wb").write(tflite_quantized_model)
