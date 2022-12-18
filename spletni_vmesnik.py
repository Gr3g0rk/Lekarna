import bottle
import model

glavni_model = model.Model()


@bottle.get("/")
def glavna_stran():
    
    podatki = glavni_model.dobi_vse_uporabnike()

    return bottle.template("glavna.html", zdravila = podatki)


bottle.run(debug=True, reloader=True)
