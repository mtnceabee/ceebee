#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 17:10:23 2024

@author: chrisbourg
"""

# Accounts Receivable Turnover = Sales / Accounts Receivable

input_sales = input("Enter Sales or None: ")
if input_sales.lower() == "none":
    total_sales = 0
elif float(input_sales) >= 0:
    total_sales = float(input_sales)

input_acc_rev = input("Enter Accounts Receivable or None: ")
if input_acc_rev.lower() == "none":
    acc_rev = 0

elif float(input_acc_rev) >= 0:
    acc_rev = float(input_acc_rev)

if acc_rev:  # Corrected variable name
    acct_rec = total_sales / acc_rev
    formatted_acct_rec = "{:,.2f}".format(acct_rec)
    print(f"Total Accounts Receivable is: {formatted_acct_rec} times")
else:
    print("Total cannot be calculated because total is zero.")

