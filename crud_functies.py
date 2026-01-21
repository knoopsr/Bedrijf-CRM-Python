import mysql.connector
from mysql.connector.constants import flag_is_set


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
    conn = get_conn()
    try:
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT id, name, vat_number, created_at FROM companies WHERE id = %s" , (company_id,))
        return cur.fetchone()
    finally:
        conn.close()


def update_company(company_id, name, vat_number):
    conn = get_conn()
    try:
        cur = conn.cursor()
        cur.execute("UPDATE companies SET name = %s, vat_number = %s WHERE id = %s", (name, vat_number, company_id))
        conn.commit()
        return cur.rowcount == 1
    finally:
        conn.close()


def delete_company(company_id):
    conn = get_conn()
    try:
        cur = conn.cursor()
        try:
            cur.execute("DELETE FROM companies WHERE id = %s", (company_id,))
            conn.commit()
        except mysql.connector.IntegrityError as ex:
         return 0
        return cur.rowcount == 1
    finally:
        conn.close()


def create_contact(company_id, name, email, phone):
    conn = get_conn()
    try:
        cur = conn.cursor()
        try:
            (cur.execute
             ("INSERT INTO contacts (company_id, name, email, phone) VALUES (%s, %s, %s, %s)",
             (company_id, name, email, phone)))
            conn.commit()
            return cur.lastrowid
        except mysql.connector.IntegrityError as ex:
            raise ValueError("Ongeldig bedrijf (company_id). Bestaat dit bedrijf wel?") from ex
    finally:
        conn.close()

def list_contacts(company_id=None):
    conn = get_conn()
    try:
        cur = conn.cursor(dictionary=True)

        if company_id is None:
            cur.execute("""
                SELECT
                    id, 
                    company_id, 
                    name,
                    email, 
                    phone, 
                    created_at 
                FROM contacts  
                ORDER BY name""")
            return cur.fetchall()

        cur.execute("""
                SELECT
                    id, 
                    company_id, 
                    name,
                    email, 
                    phone, 
                    created_at 
                FROM contacts
                    WHERE company_id = %s
                ORDER BY name
        """, (company_id,))
        return cur.fetchall()

    finally:
        conn.close()



def get_contact(contact_id):
    conn = get_conn()
    try:
        cur = conn.cursor(dictionary=True)
        cur.execute("""
            SELECT
                ct.id,
                ct.company_id,
      
                ct.name,
                ct.email,
                ct.phone,
                ct.created_at
            FROM contacts ct
            WHERE ct.id = %s
        """, (contact_id,))
        return cur.fetchone()
    finally:
        conn.close()


def update_contact(contact_id, name, email, phone):
    conn = get_conn()
    try:
        cur = conn.cursor()
        cur.execute("""
            UPDATE contacts
            SET
                name = %s,
                email = %s,
                phone = %s
            WHERE id = %s
        """, (name, email, phone, contact_id))
        conn.commit()
        return cur.rowcount == 1
    finally:
        conn.close()



def delete_contact(contact_id):
    conn = get_conn()
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM contacts WHERE id = %s", (contact_id,))
        conn.commit()
        return cur.rowcount == 1
    finally:
        conn.close()


def list_companies_with_contacts_list():
    conn = get_conn()
    try:
        cur = conn.cursor(dictionary=True)
        cur.execute("""
            SELECT
                c.id        AS company_id,
                c.name      AS company_name,
                c.vat_number,
                c.created_at AS company_created_at,

                ct.id       AS contact_id,
                ct.name     AS contact_name,
                ct.email,
                ct.phone,
                ct.created_at AS contact_created_at
            FROM companies c
            LEFT JOIN contacts ct ON ct.company_id = c.id
            ORDER BY c.id, ct.id
        """)
        rows = cur.fetchall()


        companies_by_id = {}

        for r in rows:
            cid = r["company_id"]

            if cid not in companies_by_id:
                companies_by_id[cid] = [
                    cid,
                    r["company_name"],
                    r["vat_number"],
                    r["company_created_at"],
                    []  # contacten
                ]

            if r["contact_id"] is not None:
                companies_by_id[cid][4].append([
                    r["contact_id"],
                    r["contact_name"],
                    r["email"],
                    r["phone"],
                    r["contact_created_at"]
                ])

        return list(companies_by_id.values())
    finally:
        conn.close()