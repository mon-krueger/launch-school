START
IMPORT json 

PRINT "Welcome to Loan Calculator"

PRINT "Enter the loan amount:"
    GET loan_amount
PRINT "Enter the Annual Percentage Rate (APR)"
    GET apr
PRINT "Enter the loan duration in months"
    GET loan_dur

SET mir = apr divided by 12


monthly_pmt = loan_amount * (mir / (1 - (1 + mir) ** (loan_dur)))


