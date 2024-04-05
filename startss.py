flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("optionLogin.html")

@app.route('/optionl')
def contacto():
    return render_template("optionLogin.html")

@app.route('/login')
def lo():
    return render_template("login.html")

@app.route('/Alogin')
def alo():
    return render_template("Alogin.html")

@app.route('/almacen')
def alm():
    return render_template("almacen.html")

@app.route('/crudAdmin')
def crudAdmin():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR', port=3307)
    cursor = conn.cursor()
    cursor.execute('select id, nombre, correo, contra from admin order by id')
    datos = cursor.fetchall()
    return render_template("crudAdmin.html", Admin = datos)

@app.route('/editAdmin/<string:id>')
def editAdmin(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR', port=3307)
    cursor = conn.cursor()
    cursor.execute('select id, nombre, correo, contra from admin where id = %s', (id))
    dato  = cursor.fetchall()
    return render_template("editAdmin.html", Ad=dato[0])

@app.route('/editar_admin/<string:id>',methods=['POST'])
def editar_admin(id):
    if request.method == 'POST':
        nom=request.form['nombre']
        corr=request.form['correo']
        contra=request.form['contra']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR', port=3307)
        cursor = conn.cursor()
        cursor.execute('update admin set nombre=%s, correo=%s, contra=%s where id=%s', (nom,corr,contra,id))
        conn.commit()
    return redirect(url_for('crudAdmin'))

@app.route('/borrarAd/<string:id>')
def borrarAdmin(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR',port=3307)
    cursor = conn.cursor()
    cursor.execute('delete from admin where id = {0}'.format(id))
    conn.commit()
    return redirect(url_for('crudAdmin'))

@app.route('/agrega_admin', methods=['POST'])
def agrega_admin():
    if request.method == 'POST':
        aux_Nombre = request.form['nombre']
        aux_Correo = request.form['correo']
        aux_Contra = request.form['contra']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR', port=3307)
        cursor = conn.cursor()
        cursor.execute('insert into admin (nombre,correo,contra) values (%s, %s, %s)',(aux_Nombre, aux_Correo, aux_Contra))
        conn.commit()
    return redirect(url_for('crudAdmin'))

@app.route('/crudClient')
def crudClient():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR', port=3307)
    cursor = conn.cursor()
    cursor.execute('select id, nombre, correo, contra, direccion, telefono from cliente order by id')
    datos = cursor.fetchall()
    return render_template("crudClient.html", Admin = datos)

@app.route('/editClient/<string:id>')
def editClient(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR', port=3307)
    cursor = conn.cursor()
    cursor.execute('select id, nombre, correo, contra, direccion, telefono from cliente where id = %s', (id))
    dato  = cursor.fetchall()
    return render_template("editClient.html", Ad=dato[0])

@app.route('/editar_cliente/<string:id>',methods=['POST'])
def editar_cliente(id):
    if request.method == 'POST':
        nom=request.form['nombre']
        corr=request.form['correo']
        contra=request.form['contra']
        direc=request.form['direccion']
        tel=request.form['telefono']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR', port=3307)
        cursor = conn.cursor()
        cursor.execute('update cliente set nombre=%s, correo=%s, contra=%s, direccion=%s, telefono=%s where id=%s', (nom,corr,contra,direc,tel,id))
        conn.commit()
    return redirect(url_for('crudClient'))

@app.route('/borrarC/<string:id>')
def borrarClient(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR', port=3307)
    cursor = conn.cursor()
    cursor.execute('delete from cliente where id = {0}'.format(id))
    conn.commit()
    return redirect(url_for('crudClient'))

@app.route('/agrega_cliente', methods=['POST'])
def agrega_cliente():
    if request.method == 'POST':
        aux_Nombre = request.form['nombre']
        aux_Correo = request.form['correo']
        aux_Contra = request.form['contra']
        aux_Direccion = request.form['direccion']
        aux_Telefono = request.form['telefono']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR', port=3307)
        cursor = conn.cursor()
        cursor.execute('insert into cliente (nombre,correo,contra,direccion,telefono) values (%s, %s, %s, %s, %s)',(aux_Nombre, aux_Correo, aux_Contra, aux_Direccion, aux_Telefono))
        conn.commit()
    return redirect(url_for('crudClient'))

@app.route('/crudAlmacen')
def crudAlmacen():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR', port=3307)
    cursor = conn.cursor()
    cursor.execute('select id, producto, descripcion, imagen, cantidad, precio from almacen order by id')
    datos = cursor.fetchall()
    return render_template("crudAdmin.html", comentarios = datos)

@app.route('/editAlmacen/<string:id>')
def editAlmacen(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR', port=3307)
    cursor = conn.cursor()
    cursor.execute('select id, producto, descripcion, imagen, cantidad, precio from almacen where id = %s', (id))
    dato  = cursor.fetchall()
    return render_template("editAlmacen.html", comentar=dato[0])

@app.route('/editar_almacen/<string:id>',methods=['POST'])
def editar_almacen(id):
    if request.method == 'POST':
        pro=request.form['producto']
        des=request.form['descripcion']
        img=request.form['imagen']
        cant=request.form['cantidad']
        pre=request.form['precio']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR', port=3307)
        cursor = conn.cursor()
        cursor.execute('update almacen set producto=%s, descripcion=%s, imagen=%s, cantidad=%s, precio=%s, where id=%s', (pro,des,img,cant,pre,id))
        conn.commit()
    return redirect(url_for('crudAlmacen'))

@app.route('/borrarAl/<string:id>')
def borrarAlmacen(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR', port=3307)
    cursor = conn.cursor()
    cursor.execute('delete from almacen where id = {0}'.format(id))
    conn.commit()
    return redirect(url_for('crudAlmacen'))

@app.route('/agrega_almacen', methods=['POST'])
def agrega_almacen():
    if request.method == 'POST':
        aux_Produc = request.form['producto']
        aux_Descri = request.form['descripcion']
        aux_Imagen = request.form['imagen']
        aux_Cant = request.form['cantidad']
        aux_Precio = request.form['precio']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR', port=3307)
        cursor = conn.cursor()
        cursor.execute('insert into almacen (producto,descripcion,imagen,cantidad,precio) values (%s, %s, %s,%s,%s)',(aux_Produc,aux_Descri,aux_Imagen,aux_Cant,aux_Precio))
    return redirect(url_for('crudAlmacen'))

if __name__ == "__main__":
    app.run(debug=True)
