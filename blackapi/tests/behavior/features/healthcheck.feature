Funcionalidade: Endpoint de healthckeck
    Eu como área de tecnologia
    Desejo ter um endpoint para confirmar o funcionamento dessa aplicação

    Cenário: Aplicação funcionando
        Dado que a aplicação está funcionando
        Quando receber uma request no Endpoint /liveness
        Então a seguinte mensagem deve ser exibida para sinalizar que a aplicação está funcionando
        """
        {
            "status": "green"
        }
        """