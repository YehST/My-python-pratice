import tensorflow as tf


def mlp(x):
    x = tf.keras.layers.Dense(8)(x)
    x = tf.keras.layers.Dense(8)(x)
    x = tf.keras.layers.Dense(3, activation='softmax')(x)
    return x


def model_SGD(X_train, Y_train, X_test, Y_test):
    X_input = tf.keras.Input(shape=4)
    output = mlp(X_input)
    model = tf.keras.Model(X_input, output)
    sgd = tf.keras.optimizers.SGD(0.01)
    model.compile(optimizer=sgd, loss='categorical_crossentropy',
                  metrics=['acc'])
    reduce_lr = tf.keras.callbacks.ReduceLROnPlateau(
        monitor='val_loss', factor=0.8, patience=50, min_lr=0.0001)
    history = model.fit(x=X_train, y=Y_train, epochs=1800,
                        validation_data=(X_test, Y_test), callbacks=[reduce_lr])
    return history


def model_Adam(X_train, Y_train, X_test, Y_test):
    X_input = tf.keras.Input(shape=4)
    output = mlp(X_input)
    model = tf.keras.Model(X_input, output)
    adam = tf.keras.optimizers.Adam(0.005)
    model.compile(optimizer=adam,
                  loss='categorical_crossentropy', metrics=['acc'])
    reduce_lr = tf.keras.callbacks.ReduceLROnPlateau(
        monitor='val_loss', factor=0.8, patience=50, min_lr=0.0001)
    history = model.fit(x=X_train, y=Y_train, epochs=1800,
                        validation_data=(X_test, Y_test), callbacks=[reduce_lr])
    return history


def model_AdaGrad(X_train, Y_train, X_test, Y_test):
    X_input = tf.keras.Input(shape=4)
    output = mlp(X_input)
    model = tf.keras.Model(X_input, output)
    adagrad = tf.keras.optimizers.Adagrad(0.01)
    model.compile(optimizer=adagrad,
                  loss='categorical_crossentropy', metrics=['acc'])
    reduce_lr = tf.keras.callbacks.ReduceLROnPlateau(
        monitor='val_loss', factor=0.8, patience=50, min_lr=0.0001)
    history = model.fit(x=X_train, y=Y_train, epochs=1800,
                        validation_data=(X_test, Y_test), callbacks=[reduce_lr])
    return history


def model_Adadelta(X_train, Y_train, X_test, Y_test):
    X_input = tf.keras.Input(shape=4)
    output = mlp(X_input)
    model = tf.keras.Model(X_input, output)
    adadelta = tf.keras.optimizers.Adadelta(0.01)
    model.compile(optimizer=adadelta,
                  loss='categorical_crossentropy', metrics=['acc'])
    reduce_lr = tf.keras.callbacks.ReduceLROnPlateau(
        monitor='val_loss', factor=0.8, patience=50, min_lr=0.0001)
    history = model.fit(x=X_train, y=Y_train, epochs=3000,
                        validation_data=(X_test, Y_test), callbacks=[reduce_lr])
    return history
