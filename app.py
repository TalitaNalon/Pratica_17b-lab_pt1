#from flask import Flask, render_template

#app = Flask(__name__)

#@app.route('/')
#def home():
#    return render_template('index.html')

#if __name__ == '__main__':
#    app.run()

from flask import Flask, render_template

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def home():
    return render_template('index.html')

# Rota para a página "Sobre"
@app.route('/about')
def about():
    return render_template('about.html')

# Rota para a página de "Contato"
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Rota para a página de "Menu"
@app.route('/menu')
def menu():
    return render_template('menu.html')

# Rota para a página de "Serviço"
@app.route('/service')
def service():
    return render_template('service.html')

# Rota para a página de "Equipe"
@app.route('/team')
def team():
    return render_template('team.html')

# Rota para a página de "Depoimentos"
@app.route('/testimonial')
def testimonial():
    return render_template('testimonial.html')

# Rota para a página de "Reserva"
@app.route('/booking')
def booking():
    return render_template('booking.html')

if __name__ == '__main__':
    app.run()