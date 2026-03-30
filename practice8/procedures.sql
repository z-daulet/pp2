-- upsert procedure
CREATE OR REPLACE PROCEDURE update_contact(
    p_username VARCHAR,
    p_first_name VARCHAR,
    p_phone_number VARCHAR
) AS $$
BEGIN
    INSERT INTO phonebook(username, first_name, phone_number)
    VALUES (p_username,p_first_name, p_phone_number)
    ON CONFLICT (username)
    DO UPDATE SET
        first_name = EXCLUDED.first_name,
        phone_number = EXCLUDED.phone_number;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE delete_contact(
    p_username VARCHAR
) AS $$
BEGIN
    DELETE FROM phonebook WHERE username = p_username;
END;
$$ LANGUAGE plpgsql;

DROP PROCEDURE IF EXISTS insert_many_contacts;
DROP TYPE IF EXISTS user_input;

CREATE TYPE user_input AS (
    username VARCHAR,
    first_name VARCHAR,
    phone_number VARCHAR
);


CREATE OR REPLACE PROCEDURE insert_many_contacts(
    users user_input[]
)
LANGUAGE plpgsql
AS $$
DECLARE
    u user_input;
BEGIN
    FOREACH u IN ARRAY users LOOP
        IF u.phone_number ~ '^\+7[0-9]{10}$' THEN
            INSERT INTO phonebook(username, first_name, phone_number)
            VALUES (u.username, u.first_name, u.phone_number)
            ON CONFLICT (username)
            DO UPDATE SET
                first_name = EXCLUDED.first_name,
                phone_number = EXCLUDED.phone_number;

        ELSE
            RAISE NOTICE 'Invalid phone for user %: %', u.username, u.phone_number;
        END IF;

    END LOOP;
END;
$$;