from behave import given, when, then
from flask import url_for
from json import loads


@given('que a aplicação está funcionando')
def app_is_ok(context):
    ...

@when('receber uma request no Endpoint /liveness')
def make_request(context):
    context.last_request = context.client.get(url_for('healthcheck.liveness'))

@then('a seguinte mensagem deve ser exibida para sinalizar que a aplicação está funcionando')
def check_payload(context):
    assert context.last_request.json == loads('{"status": "green"}')