import os
from os import path
from pdf_generator import generator


def test_generator_generate():
    # Arrange
    test_filename = "test_form.pdf"
    test_data = "TEST DATA"
    test_amount = "1000"
    # Act
    g = generator.FormGenerator(test_filename, test_data, test_amount)
    g.generate()
    # Assert
    file_exists = path.exists(test_filename)
    if file_exists:
        os.remove(test_filename)
        assert True
    else:
        assert False
