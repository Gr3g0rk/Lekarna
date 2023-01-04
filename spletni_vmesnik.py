import bottle
import model

glavni_model = model.Model()



# robi je babe <3
@bottle.route("/static/css/<filename>")
def serve_static_files_css(filename):
    return bottle.static_file(filename,root="./static/css/") #folder v kerm je css file in ne dejanski file



@bottle.route("/static/slike/<filename>")
def serve_static_files_img(filename):
    return bottle.static_file(filename,root="./img") #folder v kerm je slika


@bottle.get("/")
def glavna_stran():
    
    podatki = glavni_model.dobi_vse_uporabnike()

    return bottle.template("glavna.html", zdravila = podatki)


bottle.run(debug=True, reloader=True)
