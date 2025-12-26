#!/bin/bash

BASE_URL="http://127.0.0.1:5000"

echo "=== Testing Expense Tracker API ==="
echo ""

echo "1. Health Check:"
curl -s $BASE_URL/health | python3 -m json.tool
echo ""

echo "2. List Expenses (should be empty):"
curl -s $BASE_URL/api/expenses | python3 -m json.tool
echo ""

echo "3. Create Expense:"
curl -s -X POST $BASE_URL/api/expenses \
  -H "Content-Type: application/json" \
  -d '{"title": "Lunch", "amount": "12.50", "category": "Food"}' | python3 -m json.tool
echo ""

echo "4. Create Another Expense:"
curl -s -X POST $BASE_URL/api/expenses \
  -H "Content-Type: application/json" \
  -d '{"title": "Coffee", "amount": "4.75", "category": "Food", "expense_date": "2025-12-26"}' | python3 -m json.tool
echo ""

echo "5. List All Expenses:"
curl -s $BASE_URL/api/expenses | python3 -m json.tool
echo ""

echo "6. Get Single Expense (ID=1):"
curl -s $BASE_URL/api/expenses/1 | python3 -m json.tool
echo ""

echo "7. Update Expense (ID=1):"
curl -s -X PUT $BASE_URL/api/expenses/1 \
  -H "Content-Type: application/json" \
  -d '{"amount": "15.00", "notes": "Updated price"}' | python3 -m json.tool
echo ""

echo "8. Delete Expense (ID=2):"
curl -s -X DELETE $BASE_URL/api/expenses/2 -w "Status: %{http_code}\n"
echo ""

echo "9. Final List:"
curl -s $BASE_URL/api/expenses | python3 -m json.tool
echo ""

echo "=== Tests Complete ==="
