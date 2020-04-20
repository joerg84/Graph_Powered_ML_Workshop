arangoimport --file "account.csv" --type csv --collection "account" --translate "account_id=_key" --create-collection true --server.database fraud-detection
arangoimport --file "customer.csv" --type csv --collection "customer" --translate "customer_id=_key" --create-collection true --server.database fraud-detection
arangoimport --file "branch.csv" --type csv --collection "branch" --translate "id=_key" --create-collection true --server.database fraud-detection
arangoimport --file "bank.csv" --type csv --collection "bank" --translate "id=_key" --create-collection true --server.database fraud-detection
arangoimport --file "transaction.csv" --type csv --collection "transaction" --translate "transaction_id=_key" --translate "sender_acct_id=_from" --translate "receiver_acct_id=_to" --create-collection true --create-collection-type edge --server.database fraud-detection --to-collection-prefix account --from-collection-prefix account



