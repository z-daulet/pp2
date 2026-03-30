CREATE OR REPLACE FUNCTION get_contacts_by_pattern()
RETURNS TABLE(
    contact_username VARCHAR,
    contact_first_name VARCHAR,
    contact_phone VARCHAR
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        username,
        first_name,
        phone_number
    FROM
        phonebook
    WHERE
        first_name ILIKE 'a%';
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_contacts_by_pattern2()
RETURNS TABLE(
    contact_username VARCHAR,
    contact_firstname VARCHAR,
    contact_phone VARCHAR
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        username,
        first_name,
        phone_number
    FROM phonebook WHERE phone_number ILIKE '%+770';
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_contacts_paginated(
    p_limit INT,
    p_offset INT
)
RETURNS TABLE(
    usern VARCHAR,
    firstname VARCHAR,
    phonenumber VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT
        username,
        first_name,
        phone_number
    FROM phonebook
    ORDER BY username
    LIMIT p_limit
    OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;