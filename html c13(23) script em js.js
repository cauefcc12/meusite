document.getElementById('btn-jogar').addEventListener('click', function() {
    // Captura os dados da tela
    const escolhaJogador = document.querySelector('input[name="opcao"]:checked').value;
    const numeroJogador = parseInt(document.getElementById('numero').value);
    const resultadoDiv = document.getElementById('resultado');

    // Validação básica do número
    if (isNaN(numeroJogador) || numeroJogador < 0 || numeroJogador > 5) {
        resultadoDiv.innerHTML = "<strong>Por favor, escolha um número válido entre 0 e 5.</strong>";
        resultadoDiv.className = "result-box derrota"; // Classe de erro/derrota
        return;
    }

    // Computador escolhe de 0 a 5
    const numeroComputador = Math.floor(Math.random() * 6);
    
    // Calcula o resultado
    const soma = numeroJogador + numeroComputador;
    const resultadoParOuImpar = (soma % 2 === 0) ? 'par' : 'impar';
    const jogadorVenceu = (escolhaJogador === resultadoParOuImpar);

    // Monta o texto de exibição usando Template Literals (crases ``)
    let mensagemHTML = `
        <p>Você jogou: <strong>${numeroJogador}</strong> (${escolhaJogador})</p>
        <p>O computador jogou: <strong>${numeroComputador}</strong></p>
        <p>Soma: <strong>${soma}</strong> (Deu <strong>${resultadoParOuImpar.toUpperCase()}</strong>)</p>
        <hr>
        <h3>${jogadorVenceu ? '🎉 Você Venceu!' : '🤖 O Computador Venceu!'}</h3>
    `; 

    // Atualiza a tela com o resultado e a cor correspondente
    resultadoDiv.innerHTML = mensagemHTML;
    resultadoDiv.className = `result-box ${jogadorVenceu ? 'vitoria' : 'derrota'}`;
});
