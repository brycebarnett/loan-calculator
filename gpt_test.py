# tests.py

import pytest
from flask import template_rendered
from app import *


# Unit tests for Loan class
class TestLoan:
    def test_calculate_discount_factor(self):
        loan = Loan(10000, 5, 0.05)
        loan.calculateDiscountFactor()
        assert loan.getDiscountFactor() == pytest.approx(52.9900, rel=1e-3)

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


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index_route_get_request(client):
    response = client.get("/")
    assert response.status_code == 200

def test_mnthly_pmt_route_post_request(client):
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


# # Integration tests for Flask app

#     @pytest.fixture
#     def client(self, app):
#         return app.test_client()

#     def test_index_and_mnthly_pmt_routes_integration(self, client):
#         response = client.get("/")
#         assert response.status_code == 200

#         response = client.post(
#             "/",
#             data=dict(
#                 loanAmt=100000,
#                 lengthOfLoan=30,
#                 intRate=0.06,
#             ),
#             follow_redirects=True,
#         )
#         assert response.status_code == 200
