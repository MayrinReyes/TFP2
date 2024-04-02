#Importar liberia Flask
from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

#Inicializar
app = Flask(__name__)

#Navegacion
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/index')
def inicio():
    return render_template("index.html")

@app.route('/login')
def at():
    return render_template("login.html")

@app.route('/sign')
def c():
    return render_template("signup.html")

@app.route('/close')
def t():
    return render_template("close.html")

@app.route('/carro')
def v():
    return render_template("carrito.html")

##Parte de administradores
@app.route('/Alogin')
def g():
    return render_template("Alogin.html")

@app.route('/almacen')
def t():
    return render_template("almacen.html")

@app.route('/table')
def t():
    return render_template("table.html")




@app.route('/area_t', methods=['POST'])
def area():
    if request.method == 'POST':
        A = 0
        B = int(request.form['base'])
        H = int(request.form['altura'])
        A =  B * H / 2
    return render_template("at.html", res =A, r =B, re =H)
#intenta ponerlo en una tupla o lista, en forma de string como las cali
@app.route('/cal', methods=['POST'])
def cal():
    if request.method == 'POST':
        C = int(request.form['cali'])
        if C==10:
            R="Tu calificacion es Excelente"
        elif C==9 or C==8:
            R="Tu calificacion es Notable"
        elif C==7:
            R="Tu calificacion es Regular"
        elif C==6:
            R="Tu calificacion es Suficiente"
        elif C==0 or C<=5:
            R="Tu calificacion es Reprobado"
        else:
            R="Solo introducir números enteros entre 0 a 10"
    return render_template("c.html", res = R, r=C)


@app.route('/viaje', methods=['POST'])
def viaje():
    if request.method == 'POST':
        Cos = 3500
        B = int(request.form['alu'])
        if B<=99 and B>=50:
            R=70
        elif B<=49 and B>=30:
            R=95
        elif B<30:
            R=3500/B
        else:
            R="Introducir un numero valido"
        RE=B*R
        RES=RE-3500
    return render_template("v.html", r=B, re=R, res=Cos, resu=RES)

@app.route('/grados', methods=['POST'])
def grados():
    if request.method == 'POST':
        F = int(request.form['fah'])
        C= (F-32)*5/9
    return render_template("g.html", r =F, re =C)

@app.route('/tm', methods=['POST'])
def tabla():
    if request.method == 'POST':
        N = int(request.form['num'])
        lista=[]
        for x in range(1, 11):
            R=N*x
            G = f"{N} x {x} = {R} "
            lista.append(G)
    return render_template("t.html", r =lista, n=N, g=G)

if __name__ == "__main__":
    app.run(debug=True)
