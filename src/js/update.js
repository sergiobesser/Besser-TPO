var args = location.search.substr(1).split('&');
// lee los argumentos pasados a este formulario
var parts = []
for (let i = 0; i < args.length; ++i) {
    parts[i] = args[i].split('=');
}
console.log(args)
document.getElementById("txtId").value = parts[0][1]
document.getElementById("txtNombre").value = parts[1][1]
document.getElementById("txtDuracion").value = parts[2][1]
document.getElementById("txtNivel").value = parts[3][1]
document.getElementById("txtPrecio").value = parts[4][1]
 
function modificar() {
    let id = document.getElementById("txtId").value
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
    let url = "http://localhost:5000/cursos/"+id
    var options = {
        body: JSON.stringify(curso),
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        redirect: 'follow'
    }
    fetch(url, options)
        .then(function () {
            console.log("modificado")
            alert("Registro modificado")
            // Handle response we get from the API
        })
        .catch(err => {
            //this.errored = true
            console.error(err);
            alert("Error al Modificar")
        })      
}
