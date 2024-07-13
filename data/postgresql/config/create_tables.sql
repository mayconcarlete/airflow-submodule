CREATE TABLE IF NOT EXISTS users (
	id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
	first_name VARCHAR(255),
	last_name VARCHAR(255),
	email VARCHAR(255),
	gender VARCHAR(255),
	ip_address VARCHAR(50),
	birthday TIMESTAMPTZ,
	year INTEGER,
	created_at TIMESTAMPTZ DEFAULT NOW() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT NOW() NOT NULL
);

CREATE TABLE IF NOT EXISTS products (
	id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
	name VARCHAR(255),
	price INTEGER,
	image TEXT,
	buy_date TIMESTAMPTZ,
	created_at TIMESTAMPTZ DEFAULT NOW() NOT NULL,
	updated_at TIMESTAMPTZ DEFAULT NOW() NOT NULL
);