from flask import Flask

def create_app():
    app = Flask(__name__)

    from .domains.operations.healthcheck import bp_healthcheck
    from .domains.invoice.invoice import bp_invoice
    from .domains.invoice.payment import bp_payment
    
    app.register_blueprint(bp_healthcheck)
    app.register_blueprint(bp_invoice)
    app.register_blueprint(bp_payment)
    return app 