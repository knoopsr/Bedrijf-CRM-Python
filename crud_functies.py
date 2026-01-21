import mysql.connector


def get_conn():
    return mysql.connector.connect(
        host="localhost",
        user="syntra",
        password="Syntra$2026",
        database="company_manager"
    )



def create_company(name, vat_number):
    conn = get_conn()
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO companies (name, vat_number) VALUES (%s, %s)",
            (name, vat_number)
        )
        conn.commit()
    finally:
        conn.close()


def list_companies():
    conn = get_conn()
    try:
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT id, name, vat_number, created_at FROM companies ORDER BY id")
        return cur.fetchall()
    finally:
        conn.close()


def get_company(company_id):

def update_company(company_id, name, vat_number):

def delete_company(company_id):

def create_contact(company_id, name, email, phone):

def list_contacts(company_id=None):

def get_contact(contact_id):

def update_contact(contact_id, name, email, phone):

def delete_contact(contact_id):



