from behave import given, when, then
from flask import url_for
from json import loads, dumps


@given('que a informação de crédito foi recebida em uma request')
def send_request(context):
    context.headers = {'content-type': 'application/json'}

    context.body = dumps({"debtId": "8291","paidAt": "2022-06-09 10:00:00","paidAmount": 100000.00,"paidBy": "John Doe"})

    context.last_request = context.client.post(url_for('payment.create'), data=dumps(context.body), headers=context.headers)


@when('recebida no Endpoint /payment/create contendo os campos corretos')
def check_fields(context):
    assert context.last_request.json == loads('{"status": "processed"}')


@then(u'a seguinte mensagem deve ser exibida para sinalizar que o pagamento foi processado')
def check_return_payload(context):
    assert context.last_request.json == loads('{"status": "processed"}')