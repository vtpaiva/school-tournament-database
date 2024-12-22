# school-tournament-database

The goal of this project is to model and implement a **robust database** for a sports tournament between schools, utilizing ***PostgreSQL*** and the Python ***Psycopg3*** library. The project aims to store and manage information related to sports modalities, competitions, teams, games, and results, providing an efficient and scalable solution to organize the tournament.

The project ranges from the conceptual modeling phase with **Entity-Relation** and **Relational** diagrams to the implementation phase with **PostgresSQL** and **Psycopg3** in **Python**, being a reference on how to build a robust and reliable database system from an abstract idea.

## Technology and Implementation

* **PostgreSQL** was chosen for this project due to its robustness, flexibility, and support for complex queries and large volumes of data. **PostgreSQL** offers support for **ACID** transactions, referential integrity, and advanced queries, which are essential for a tournament management system.

* **Psycopg3**, a **Python** library for **PostgreSQL**, was used to establish the connection and interaction between the **Python** code and the database. With *Psycopg3*, it is possible to execute SQL commands directly on PostgreSQL, manipulate data, and integrate the database system into the application workflow.

## Entity-Relationship Diagram

![Logo](https://i.imgur.com/oz4HHj0.png)

## How to run

In order to install the system requirements to get the application running, execute the following command:

```bash
pip install -r requirements.txt
```

After building the database on a ***PostgreSQL*** terminal with the `schema.sql`and `data.sql` files on `sql` directory, run the following command to get the *CLI* running:

```bash
python -m src.main
```

## Conclusion

This project demonstrates how the combination of ***PostgreSQL*** and ***Psycopg3*** can be **effectively** used to model and implement a database management system for a sports tournament between schools. The use of a **relational database** ensures that information is well-organized, accessible, and secure, while ***Psycopg3*** provides a simple and efficient interface for interacting with the database. The scalability and **flexibility** of the system make it suitable for tournaments of various sizes and complexities, offering a robust solution for managing all aspects of the sports tournament.

## References

🖥️ <a href="https://www.psycopg.org/psycopg3/docs/index.html">Psycopg3 Documentation</a>

🛢️ <a href="https://www.psycopg.org/psycopg3/docs/index.htmlhttps://www.postgresql.org/docs/17/index.html">PostgresSQL Documentation</a>