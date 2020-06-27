from pdf_generator import generator

file_name = "demo_form.pdf"
name = "DEMO NAME"
amount = "1000"

g = generator.FormGenerator(file_name, name, amount)
g.generate()
