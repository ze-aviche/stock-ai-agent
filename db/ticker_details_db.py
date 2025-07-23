import sqlite3
import os

def get_db_path():
    db_dir = os.path.dirname(__file__)
    return os.path.join(db_dir, 'ticker_details.db')

def init_ticker_details_db():
    conn = sqlite3.connect(get_db_path())
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS ticker_details (
            ticker TEXT PRIMARY KEY,
            name TEXT,
            market TEXT,
            locale TEXT,
            primary_exchange TEXT,
            type TEXT,
            active INTEGER,
            currency_name TEXT,
            cik TEXT,
            composite_figi TEXT,
            share_class_figi TEXT,
            market_cap INTEGER,
            phone_number TEXT,
            address1 TEXT,
            city TEXT,
            state TEXT,
            postal_code TEXT,
            description TEXT,
            sic_code TEXT,
            sic_description TEXT,
            ticker_root TEXT,
            homepage_url TEXT,
            total_employees INTEGER,
            list_date TEXT,
            logo_url TEXT,
            icon_url TEXT,
            share_class_shares_outstanding INTEGER,
            weighted_shares_outstanding INTEGER,
            round_lot INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def insert_or_update_ticker(details):
    conn = sqlite3.connect(get_db_path())
    c = conn.cursor()
    c.execute('''
        INSERT OR REPLACE INTO ticker_details VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    ''', (
        details.get('ticker'),
        details.get('name'),
        details.get('market'),
        details.get('locale'),
        details.get('primary_exchange'),
        details.get('type'),
        int(details.get('active', False)),
        details.get('currency_name'),
        details.get('cik'),
        details.get('composite_figi'),
        details.get('share_class_figi'),
        details.get('market_cap'),
        details.get('phone_number'),
        details.get('address', {}).get('address1') if details.get('address') else None,
        details.get('address', {}).get('city') if details.get('address') else None,
        details.get('address', {}).get('state') if details.get('address') else None,
        details.get('address', {}).get('postal_code') if details.get('address') else None,
        details.get('description'),
        details.get('sic_code'),
        details.get('sic_description'),
        details.get('ticker_root'),
        details.get('homepage_url'),
        details.get('total_employees'),
        details.get('list_date'),
        details.get('branding', {}).get('logo_url') if details.get('branding') else None,
        details.get('branding', {}).get('icon_url') if details.get('branding') else None,
        details.get('share_class_shares_outstanding'),
        details.get('weighted_shares_outstanding'),
        details.get('round_lot')
    ))
    conn.commit()
    conn.close()

def get_ticker_details_from_db(ticker):
    conn = sqlite3.connect(get_db_path())
    c = conn.cursor()
    c.execute('SELECT * FROM ticker_details WHERE ticker = ?', (ticker,))
    row = c.fetchone()
    conn.close()
    if row:
        columns = [desc[0] for desc in c.description]
        return dict(zip(columns, row))
    return None 