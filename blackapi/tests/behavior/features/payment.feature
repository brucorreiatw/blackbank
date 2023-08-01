Funcionalidade: Endpoint que seja capaz de receber um aviso de pagamento
    Eu como área financeira
    Desejo comunicar todos os pagamentos feitos através de uma API

    Cenário: Recebimento de uma request com toda a informação necessária para registrar créditos
        Dado que a informação de crédito foi recebida em uma request
        Quando recebida no Endpoint /payment/create contendo os campos corretos
        """
            {"status": "processed"}
        """
        Então a seguinte mensagem deve ser exibida para sinalizar que o pagamento foi processado
        """
            {"status": "processed"}
        """