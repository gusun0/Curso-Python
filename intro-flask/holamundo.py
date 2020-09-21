from flask import Flask, request, url_for, redirect,abort, render_template

app = Flask(__name__)

## decoradores

@app.route('/')

def index():
    return "Hola Mundo"


### SE PUEDEN PONER EN DOS METODOS DISTINTOS ####

##PARA AGREGAR MAS RUTAS SE USA @app.route
## METODOS MAS UTILIZADOS => GET, POST, PUT, PATCH, DELETE

#@app.route('/post/<int:post_id>', methods=['GET'])
#
### definimos la funcion para lala
#
#def lala(post_id):
#    return 'Estas en el post '+ str(post_id)
#

##PARA AGREGAR MAS RUTAS SE USA @app.route
## METODOS MAS UTILIZADOS => GET, POST, PUT, PATCH, DELETE
#
#@app.route('/post/<int:post_id>', methods=['POST'])
#
### definimos la funcion para lala
#
#def lili(post_id):                                       
#    return 'Estas en el post '+ str(post_id)

### SE PUEDEN PONER EN DOS METODOS DISTINTOS ###



        #### PONIENDO EN UN MISMO METODO ######

@app.route('/post/<int:post_id>', methods=['GET','POST'])

## definimos la funcion para lala

def lolo(post_id):
    if request.method == 'GET':
        return 'Estas en el post '+ str(post_id)
    else:
        return 'Este es otro metodo y no get'

        #### PONIENDO EN UN MISMO METODO ######



        ##PARA AGREGAR MAS RUTAS SE USA @app.route
@app.route('/lele', methods=['POST','GET'])
def lele():
    #abort(404)
    #return redirect(url_for('lolo',post_id=2))
    #print(request.form)
    #print(request.form['llave1'])
    #print(request.form['llave2'])
    #return 'lele'
    #return render_template('lele.html')
    return {
        "nombre": 'gusun0',
        "email": 'gusun@g.com'
            
    }

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html',mensaje = 'hola mundo')



