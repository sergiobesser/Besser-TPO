if (document.getElementById("app")) {
    const app = new Vue({
        el: "#app",
        data: {
            cursos: [],
            errored: false,
            loading: true
        },
        created() {
            var url = 'http://localhost:5000/cursos'
            this.fetchData(url)
        },
        methods: {
            fetchData(url) {
                fetch(url)
                    .then(response => response.json())
                    .then(data => {
                        this.cursos = data;
                        this.loading = false;
                    })
                    .catch(err => {
                        this.errored = true
                    })
            },
            eliminar(curso) {
                const url = 'http://localhost:5000/curso/' + curso;
                var options = {
                    method: 'DELETE',
                }
                fetch(url, options)
                    .then(res => res.text()) // or res.json()
                    .then(res => {
                        location.reload();
                    })
            }
        }
    })
}
