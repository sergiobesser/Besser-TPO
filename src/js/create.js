function guardar() {
 
    let n = document.getElementById("txtNombre").value
    let d = document.getElementById("txtDuracion").value
    let nv = document.getElementById("txtNivel").value
    let p = parseFloat(document.getElementById("txtPrecio").value)
 
    let curso = {
        nombre: n,
        duracion: d,
        nivel: nv,
        precio: p,
    }
    let url = "http://localhost:5000/cursos"
    var options = {
        body: JSON.stringify(curso),
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
       // redirect: 'follow'
    }
    fetch(url, options)
        .then(function () {
            console.log("creado")
            alert("Grabado")
 
            // Handle response we get from the API
        })
        .catch(err => {
            //this.errored = true
            alert("Error al grabar" )
            console.error(err);
        })
}
