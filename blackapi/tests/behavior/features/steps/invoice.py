from behave import given, when, then
from flask import url_for
from json import loads


@given('que o arquivo CSV foi recebido em uma request')
def send_csv(context):
    file = "blackapi/csv_sample/csv_example.csv"
    data = {
        'file': (open(file, 'rb'), file)
    }
    context.last_request = context.client.post(url_for('invoice.create'), data=data)


@when('recebido no Endpoint /invoice/create contendo os campos corretos')
def check_fields(context):
    assert context.last_request.json == loads('{"status": "processed"}')


@then('a seguinte mensagem deve ser exibida para sinalizar que a lista foi processada')
def check_return_payload(context):
    assert context.last_request.json == loads('{"status": "processed"}')