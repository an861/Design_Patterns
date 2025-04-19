## BEST Architecture for an Email Service
[Client/API Call] ---> [Observer/Event Handler] ---> [Notification Factory]
                                         |
                                         v
                [Builder Constructs Email] ---> [Queue (RabbitMQ/Kafka)]
                                         |
                                         v
                             [Worker Picks Task]
                             [Strategy Selects Provider]
                             [Sends Email via SMTP/SendGrid]
                                         |
                                         v
                              [Log to PostgreSQL]
