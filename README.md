```markdown
# 🧾 Sales ETL Project

This is a simple end-to-end **ETL (Extract, Transform, Load)** pipeline project built with **Python**, **Docker**, **PostgreSQL**, and **Metabase**. The goal is to simulate a real-world data engineering workflow where raw data is loaded into a relational database and visualized via dashboards.

---

## 🚀 Tech Stack

- 🐍 Python (ETL script)
- 🐘 PostgreSQL (Database)
- 🐳 Docker & Docker Compose (Containerization)
- 📊 Metabase (Data Visualization)

---

## 📁 Project Structure

```

sales-etl-project/
│
├── docker-compose.yml         # Defines services: db and metabase
├── src/
│   └── etl.py                 # Python ETL script
├── .env                       # DB credentials (safe to show in sample)
├── README.md                  # You're reading this!

````

---

## ⚙️ Setup Instructions

### 1. 🔧 Clone the Repository

```bash
git clone https://github.com/MonicaDasari21/sales-etl-project.git
cd sales-etl-project
````

### 2. 🛠️ Set Up Environment Variables

Create a `.env` file in the project root with the following:

```env
POSTGRES_USER=shopuser
POSTGRES_PASSWORD=shoppass
POSTGRES_DB=shopdb
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

> These are used in `etl.py` to build the database connection string.

### 3. 🐳 Start Docker Containers

```bash
docker compose up -d --build
```

This will:

* Start a PostgreSQL container (port 5432)
* Start a Metabase container (port 3000)

---

## 🛠️ Run the ETL Script

Activate your virtual environment (if not already):

```bash
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

Then run:

```bash
python src/etl.py
```

You should see:

```
Running ETL script...
Connecting to database and loading data...

   order_id product  quantity  price
0       101   Shirt         2  29.99
1       102   Jeans         1  49.99
2       103   Shoes         4  79.99

✅ Data loaded successfully into 'sales' table!
```

---

## 📊 View Dashboard in Metabase

1. Open your browser and go to: [http://localhost:3000](http://localhost:3000)
2. Set up an admin account (only first time).
3. Connect to your PostgreSQL database:

   * **Host**: `db` or `localhost`
   * **Port**: `5432`
   * **Database**: `shopdb`
   * **Username**: `shopuser`
   * **Password**: `shoppass`
4. Start building charts and dashboards from the `sales` table!

---

## 🧪 Verify Data in PostgreSQL (optional)

You can inspect the loaded data from the terminal:

```bash
docker exec -it sales_etl_project-db-1 psql -U shopuser shopdb
```

Inside the PostgreSQL shell:

```sql
SELECT * FROM sales;
```

---

## 📌 What You Learned

✅ Build and run a full ETL pipeline
✅ Use Docker Compose to manage services
✅ Load data into PostgreSQL using Python
✅ Create dashboards using Metabase
✅ Work like a real Data Engineer 💼

---

## 🧑‍💻 Author

**Monica Dasari**
Email: [monicadasari21@gmail.com](mailto:monicadasari21@gmail.com)
GitHub: [@MonicaDasari21](https://github.com/MonicaDasari21)

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

```

---


