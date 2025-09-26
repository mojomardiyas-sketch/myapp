import mysql.connector

# Koneksi ke database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password_kamu",
    database="myapp_db"
)

cursor = conn.cursor()

# CREATE
def tambah_user(nama, email):
    query = "INSERT INTO users (name, email) VALUES (%s, %s)"
    cursor.execute(query, (nama, email))
    conn.commit()
    print("✅ User ditambahkan.")

# READ
def tampilkan_users():
    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        print(row)

# UPDATE
def ubah_email(user_id, email_baru):
    query = "UPDATE users SET email = %s WHERE id = %s"
    cursor.execute(query, (email_baru, user_id))
    conn.commit()
    print("✏️ Email diubah.")

# DELETE
def hapus_user(user_id):
    query = "DELETE FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    conn.commit()
    print("❌ User dihapus.")

# Tes fungsi
tambah_user("Denur", "denur@example.com")
tampilkan_users()
ubah_email(1, "denurbaru@example.com")
hapus_user(1)

conn.close()


