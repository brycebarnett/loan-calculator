# tests.py

from flask import Flask
from flask.testing import FlaskClient
from oop_loan_pmt import Loan
import pytest


# Unit tests for Loan class
class TestLoan:
    def test_calculate_discount_factor(self):
        loan = Loan(100000, 30, 0.06)
        loan.calculateDiscountFactor()
        assert loan.getDiscountFactor() == pytest.approx(197.76716486711662, rel=1e-2)

    def test_calculate_loan_payment(self):
        loan = Loan(100000, 30, 0.06)
        loan.calculateLoanPmt()
        assert loan.getLoanPmt() == pytest.approx(599.5513529958137, rel=1e-2)

    def test_get_loan_amount(self):
        loan = Loan(100000, 30, 0.06)
        assert loan.getLoanAmount() == 100000

    def test_get_periodic_interest_rate(self):
        loan = Loan(100000, 30, 0.06)
        assert loan.getPeriodicIntRate() == pytest.approx(0.005, rel=1e-2)


# Functional tests for Flask routes
class TestFlaskRoutes:
    @pytest.fixture
    def app(self):
        app = Flask(__name__)
        app.testing = True
        return app

    @pytest.fixture
    def client(self, app):
        return app.test_client()

    def test_index_route_get_request(self, client):
        response = client.get("/")
        assert response.status_code == 200

    def test_mnthly_pmt_route_post_request(self, client):
        response = client.post(
            "/",
            data=dict(
                loanAmt=100000,
                lengthOfLoan=30,
                intRate=0.06,
            ),
            follow_redirects=True,
        )
        assert response.status_code == 200


# Integration tests for Flask app
class TestFlaskApp:
    @pytest.fixture
    def app(self):
        app = Flask(__name__)
        app.testing = True
        return app

    @pytest.fixture
    def client(self, app):
        return app.test_client()

    def test_index_and_mnthly_pmt_routes_integration(self, client):
        response = client.get("/")
        assert response.status_code == 200

        response = client.post(
            "/",
            data=dict(
                loanAmt=100000,
                lengthOfLoan=30,
                intRate=0.06,
            ),
            follow_redirects=True,
        )
        assert response.status_code == 200
