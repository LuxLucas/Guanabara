// Retorna o valor de input 
function getNumero(){
    valor = inputElement.value;
    return valor;
}

// Confirma se o valor está nos parâmetros desejados
function validarNumero(numero){
    // Se não for vazio ou null
    if(!(numero == '' || numero == null)){
        // Se não (não é um número) - sim, pode ser confuso
        if(!isNaN(numero)){
            numero = parseInt(numero);
            // Se (maior ou igual a 0) e (menor ou igual a 100)
            if(numero >= 0 && numero <= 100){
                return true;
            }else{return false;}
        }else{return false;}
    }else{return false;}
}

// Adiciona elementos no select
function newOption(mensagem){
    selectElement.options[selectElement.options.length] = new Option(mensagem);
}

// Declaração de elementos e lista
let boxResultado = document.querySelector('#box-2')
let inputElement = document.querySelector("#numero");
let selectElement = document.querySelector('#lista');
let buttonAdd = document.querySelector('#add');
let buttonFim = document.querySelector('#fim');
let listaSelect = [];

// Adiciona o número validado no select e na lista
buttonAdd.addEventListener('click', function(){
    let Numero = getNumero();
    if(validarNumero(Numero)){
        Numero = parseInt(Numero);
        listaSelect.push(Numero);
        let mensagemSelect = `Você adicionou: ${Numero}`;
        newOption(mensagemSelect);
    }else{
        alert('O valor (ou a falta dele) é INVÁLIDO');
    }
});

buttonFim.addEventListener('click', function(){
    boxResultado.style.display = 'block'
})