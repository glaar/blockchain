chain = [
        {
            "index": 1,
            "previous_hash": "1",
            "proof": 100,
            "timestamp": 1555255008.59967,
            "transactions": []
        },
        {
            "index": 2,
            "previous_hash": "bb07b539e1eb1f7086f6459c583dd9865bd94cbbf69437f720b191338e98b0f9",
            "proof": 29685,
            "timestamp": 1555258421.0316548,
            "transactions": [
                {
                    "amount": 100,
                    "recipient": "valerie",
                    "sender": "glenn"
                },
                {
                    "amount": 100,
                    "recipient": "valerie",
                    "sender": "glenn"
                },
                {
                    "amount": 100,
                    "recipient": "valerie",
                    "sender": "glenn"
                },
                {
                    "amount": 100,
                    "recipient": "valerie",
                    "sender": "glenn"
                },
                {
                    "amount": 1,
                    "recipient": "c959f2933591464dab38ec9fb1c983e0",
                    "sender": "0"
                }
            ]
        },
        {
            "index": 3,
            "previous_hash": "67b2cf39e6dd1740735e56d0848baf0c6687e105c6c313f7046809282967ceb7",
            "proof": 51733,
            "timestamp": 1555258681.738653,
            "transactions": [
                {
                    "amount": 30,
                    "recipient": "valerie",
                    "sender": "glenn"
                },
                {
                    "amount": 1,
                    "recipient": "c959f2933591464dab38ec9fb1c983e0",
                    "sender": "0"
                }
            ]
        },
{
            "index": 4,
            "previous_hash": "67b2cf39e6dd1740735e56d0848baf0c6687e105c6c313f7046809282967ceb7",
            "proof": 51733,
            "timestamp": 1555258681.738653,
            "transactions": [
                {
                    "amount": 30,
                    "recipient": "glenn",
                    "sender": "valerie"
                },
                {
                    "amount": 1,
                    "recipient": "c959f2933591464dab38ec9fb1c983e0",
                    "sender": "0"
                }
            ]
        }
    ]


amount = 0
user = "glenn"
for item in chain:
    for key in item:
        if key == "transactions":
            for t_item in item[key]:
                if t_item["recipient"] == user:
                    for element in t_item:
                        if element == "amount":
                            amount += t_item[element]

print(amount)



