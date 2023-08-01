Funcionalidade: Endpoint que seja capaz de receber uma lista de débitos para geração de boletos 
    Eu como área financeira
    Desejo registrar todos os débitos a partir de um arquivo CSV em uma API

    Cenário: Recebimento do arquivo CSV com toda a informação necessária para registrar débitos
        Dado que o arquivo CSV foi recebido em uma request
        Quando recebido no Endpoint /invoice/create contendo os campos corretos
        Então a seguinte mensagem deve ser exibida para sinalizar que a lista foi processada
        """
            {"status": "processed"}
        """