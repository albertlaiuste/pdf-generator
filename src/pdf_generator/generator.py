from reportlab.pdfgen import canvas


class FormGenerator:
    def __init__(self, filename: str, name: str, amount: str = 0) -> object:
        self.filename = filename
        self.name = name
        self.amount = amount

    def generate(self):
        c = canvas.Canvas(self.filename)
        c.setLineWidth(.3)
        c.setFont('Helvetica', 12)
        c.drawString(30, 750, 'DEMO TEXT')
        c.drawString(30, 735, 'FOR PROJECT STRUCTURE')
        c.drawString(500, 750, "27.06.2020")
        c.line(480, 747, 580, 747)
        c.drawString(275, 725, 'DEMO AMOUNT:')
        c.drawString(500, 725, self.amount)
        c.line(378, 723, 580, 723)
        c.drawString(30, 703, 'RECEIVED BY:')
        c.line(120, 700, 580, 700)
        c.drawString(120, 703, self.name)
        c.save()
