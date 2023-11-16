function buscaCep() {
    let cep = document.getElementById('zip_code').value;
    if(cep !== ""){
        let url = "https://brasilapi.com.br/api/cep/v1/" + cep;

        let req = new XMLHttpRequest();
        req.open("GET", url);
        req.send();

        // tratar a resposta
        req.onload = function() {
            if(req.status === 200){
                let endereco = JSON.parse(req.response);
                document.getElementById("id_street_address").value = endereco.street;
                document.getElementById("id_neighborhood").value = endereco.neighborhood;
                document.getElementById("id_city").value = endereco.city;
                document.getElementById("id_state").value = endereco.state;
                document.getElementById("id_country").value = "Brasil";
            }
            else if(req.status === 404){
                alert("CEP Inválido");
            }
            else{
                alert("Erro ao fazer a requisição!")
            }
        }

    }
}

window.onload = function() {
    let zip_code = document.getElementById("zip_code");
    zip_code.addEventListener("blur", buscaCep);
}
