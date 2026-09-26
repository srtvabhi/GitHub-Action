from train import train_model


def test_train_model():
    accuracy = train_model()
    assert accuracy >= 0.80
