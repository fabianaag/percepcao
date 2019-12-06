import tensorflow as tf

interpreter = tf.lite.Interpreter(model_path="converted_model.tflite")
interpreter.allocate_tensors()

# Print input shape and type
print(interpreter.get_input_details()[0]['shape'])  
print(interpreter.get_input_details()[0]['dtype'])  
# Print output shape and type
print(interpreter.get_output_details()[0]['shape'])  
print(interpreter.get_output_details()[0]['dtype'])
