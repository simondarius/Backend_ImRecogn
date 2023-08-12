import tensorflow as tf
import matplotlib.pyplot as plt
import tensorflow_hub as hub

model = tf.keras.Sequential([
    hub.KerasLayer("https://tfhub.dev/sayakpaul/distill_bit_r50x1_160_feature_extraction/1", trainable=True),
    tf.keras.layers.Dense(101,activation='softmax',kernel_initializer='zeros')
])

checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath='model_checkpoint_{epoch:02d}.h5',  
    save_freq='epoch', 
    period=1  
)
lr = 0.03
SCHEDULE_BOUNDARIES = [200, 300, 400]
lr_schedule = tf.keras.optimizers.schedules.PiecewiseConstantDecay(boundaries=SCHEDULE_BOUNDARIES,
                                                                  values=[lr, lr*0.1, lr*0.001, lr*0.0001])
model.compile(loss="SparseCategoricalCrossentropy",optimizer=tf.keras.optimizers.Adam(learning_rate=lr_schedule),metrics=['accuracy'])

trainDataGen=tf.keras.preprocessing.image.ImageDataGenerator(
    height_shift_range=10,
    zoom_range=10,
    shear_range=20,
    rescale=1/255.,

)
data_pipeline=trainDataGen.flow_from_directory(directory='data/train',target_size=(160,160),batch_size=32,class_mode='sparse')
valDataGen=tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255
)
val_data_pipeline = valDataGen.flow_from_directory(
    directory='data/test',
    target_size=(160, 160),
    batch_size=32,
    class_mode='sparse'
)
model.fit(data_pipeline,epochs=10,validation_data=val_data_pipeline)