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
def i():
    return render_template("login.html")

@app.route('/sign')
def s():
    return render_template("signup.html")

@app.route('/close')
def c():
    return render_template("close.html")

@app.route('/carro')
def carro():
    return render_template("carrito.html")

##Parte de administradores
@app.route('/Alogin')
def Al():
    return render_template("Alogin.html")

@app.route('/almacen')
def a():
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


@app.route('/inicio', methods=['POST'])
def iniciar():
    if request.method == 'POST':
        aux_Nom = request.form['nombre']
        aux_Correo = request.form['correo']
        aux_Contra = request.form['contra']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR' )
        cursor = conn.cursor()
        resultado = cursor.fetchone()
        # Comprueba si la base de datos existe
        if resultado:
            print("La base de datos existe.")
        else:
                        # Define the SQL statements for table creation
            sql_statements = """
            
CREATE SCHEMA IF NOT EXISTS `db_OAGR` DEFAULT CHARACTER SET utf8mb4 ;
USE `db_OAGR` ;
-- -----------------------------------------------------
-- Table `db_OAGR`.`admin`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_OAGR`.`admin` (
  `id` INT() PRIMARY KEY AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  `correo` VARCHAR(100) NOT NULL,
  `contra` VARCHAR(10) NOT NULL);
-- -----------------------------------------------------
-- Table `db_OAGR`.`almacen`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_OAGR`.`almacen` (
  `id` INT() PRIMARY KEY AUTO_INCREMENT NOT NULL,
  `producto` VARCHAR(100) NOT NULL,
  `descripcion` VARCHAR(200) NULL DEFAULT NULL,
  `imagen` VARCHAR() NULL DEFAULT NULL,
  `cantidad` INT() NOT NULL,
  `precio` INT() NOT NULL);
-- -----------------------------------------------------
-- Table `db_OAGR`.`cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_OAGR`.`cliente` (
  `id` INT() PRIMARY KEY  AUTO_INCREMENT NOT NULL,
  `nombre` VARCHAR(50) NOT NULL,
  `correo` VARCHAR(100) NOT NULL,
  `contra` VARCHAR(50) NOT NULL);

--admin predeterminado  
insert into admin(nombre, correo, contrasenia) values ('mayrin', 'mayrinreyes1707@gmail.com', '12345');

--Productos

            """

            # Execute the SQL statements
            
            statements = [stmt.strip() for stmt in sql_statements.split(';') if stmt.strip()]

            # Execute each SQL statement
            for statement in statements:
              cursor.execute(statement)
              cursor.commit()


            print("La base de datos no existe.")
            cursor.execute('')
        cursor.execute('insert into cliente (nombre, correo, contra) values (%s, %s, %s)',(aux_Nom, aux_Correo, aux_Contra))
        conn.commit()
    return redirect(url_for('index'))
"""
username = self.username_input.text()
        password = self.password_input.text()
        sql = "SELECT nombre, contrasenia FROM usuarios WHERE nombre = %s"
        con_db.cursor.execute(sql, (username,))
        result = con_db.cursor.fetchone()
        if result is None:
            print("Nombre de usuario incorrecto. Vuelve a intentarlo")
            self.username_feedback.setText(
                "Nombre de usuario incorrecto.")
        else:
            user = result[0]
            db_password = result[1]
            if password == db_password:
                print("Bienvenido")
                self.username_feedback.setText("Usuario correcto")
                self.password_feedback.setText("Contraseña correcta")
                if not hasattr(self, 'home_window'):
                    self.home_window = HomeWindow()
                    self.home_window.show()
                    self.close()
                else:
                    self.show()
                
            else:
                self.password_feedback.setText("Contraseña incorrecta.")
                
                print("Acesso denegado")
        return False

    def red_register(self):
        from signup import SignScreen
        print("Redireccioando")
        if not hasattr(self, 'register'):
            self.register = SignScreen()
            self.register.show()
            self.close()
        else:
            self.show()"""

@app.route('/crudAdmin')
def crudAdmin():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
    cursor = conn.cursor()
    cursor.execute('select id, nombre, correo, contra from admin order by id')
    datos = cursor.fetchall()
    return render_template("crudAdmin.html", comentarios = datos)

@app.route('/editAdmin/<string:id>')
def editAdmin(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
    cursor = conn.cursor()
    cursor.execute('select id, nombre, correo, contra from admin where id = %s', (id))
    dato  = cursor.fetchall()
    return render_template("editAdmin.html", comentar=dato[0])

@app.route('/editar_admin/<string:id>',methods=['POST'])
def editar_admin(id):
    if request.method == 'POST':
        nom=request.form['nombre']
        corr=request.form['correo']
        contra=request.form['contra']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
        cursor = conn.cursor()
        cursor.execute('update admin set nombre=%s, correo=%s, contra=%s where id=%s', (nom,corr,contra,id))
        conn.commit()
    return redirect(url_for('crudAdmin'))

@app.route('/borrar/<string:id>')
def borrarAdmin(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
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
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
        cursor = conn.cursor()
        cursor.execute('insert into admin (nombre,correo,contra) values (%s, %s, %s)',(aux_Nombre, aux_Correo, aux_Contra))
        conn.commit()
    return redirect(url_for('crudAdmin'))

@app.route('/crudClient')
def crudClient():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
    cursor = conn.cursor()
    cursor.execute('select id, nombre, correo, contra from cliente order by id')
    datos = cursor.fetchall()
    return render_template("crudClient.html", comenta = datos)

@app.route('/editClient/<string:id>')
def editClient(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
    cursor = conn.cursor()
    cursor.execute('select id, nombre, correo, contra from cliente where id = %s', (id))
    dato  = cursor.fetchall()
    return render_template("editClient.html", comentar=dato[0])

@app.route('/editar_cliente/<string:id>',methods=['POST'])
def editar_cliente(id):
    if request.method == 'POST':
        nom=request.form['nombre']
        corr=request.form['correo']
        contra=request.form['contra']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
        cursor = conn.cursor()
        cursor.execute('update cliente set nombre=%s, correo=%s, contra=%s where id=%s', (nom,corr,contra,id))
        conn.commit()
    return redirect(url_for('crudClient'))

@app.route('/borrar/<string:id>')
def borrarClient(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
    cursor = conn.cursor()
    cursor.execute('delete from cliente where id = {0}'.format(id))
    conn.commit()
    return redirect(url_for('crudClient'))

@app.route('/agrega_cliente', methods=['POST'])
def agrega_comenta():
    if request.method == 'POST':
        aux_Nombre = request.form['nombre']
        aux_Correo = request.form['correo']
        aux_Contra = request.form['contra']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
        cursor = conn.cursor()
        cursor.execute('insert into cliente (nombre,correo,contra) values (%s, %s, %s)',(aux_Nombre, aux_Correo, aux_Contra))
        conn.commit()
    return redirect(url_for('crudClient'))

if __name__ == "__main__":
    app.run(debug=True)
