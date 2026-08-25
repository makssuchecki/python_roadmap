str1 = """multiline
string"""
print(str1)
str2 = (
    "another "
    "multiline "
    "string"
)
print(str2)
str3 = "yet another" \
"multiline string"
print(str3)

str_list = ["list", "of", "strings"]
print(" ".join(str_list))

f_str = f"""f but make it
{str1}
"""
print(f_str)

# SQL 
query = """
SELECT
    customer_id,
    name,
    email,
    created_at
FROM customers
WHERE created_at >= '2026-01-01';
"""