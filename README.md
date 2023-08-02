<a href="https://codecov.io/gh/brucorreiatw/blackbank" >
<img src="https://codecov.io/gh/brucorreiatw/blackbank/branch/main/graph/badge.svg?token=8WM8Y97396"/>
</a>

# blackbank
Serviço simples para brincar de cobrança e pagamento utilizando BDD e TDD

<img src="https://github.com/brucorreiatw/blackbank/blob/main/images/blackbank.drawio.png?raw=true">

Considerando os benefícios da abordagem de uma linguagem Ubíqua entre áreas de negócio e técnicas, estou criando um projeto que aborda o uso de BDD(Behaviour Driven Development) na escrita de novas features.

Isso quer dizer que o desenvolvimento da API partiu de um erro sendo gerado por um teste de comportamento.
A partir do erro, o desenvolvedor pode iniciar o desenvolvimento da feature para atender a expectativa do teste.


<img src="https://github.com/brucorreiatw/blackbank/blob/main/images/Funcionalidade.png">


Para executar os testes, basta executar o seguinte comando na raiz do projeto:

```
make tests
```

Para aprovisionar esse serviço é necessário atender aos seguintes requisitos:

* docker
* docker-compose

Os passos para aprovisionamento são os seguintes:
```
make build
make run
```