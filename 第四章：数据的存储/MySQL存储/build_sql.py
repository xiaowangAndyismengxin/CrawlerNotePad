__all__ = [
    'basic_parse', 'insert_sql'
]


def basic_parse(table: str, data: list[str]) -> tuple[str, str]:
    keys = ', '.join(data)
    values = ', '.join(len(data) * ['%s'])
    return keys, values


def insert_sql(table: str, data: list[str], duplicate_key_update: bool = False)\
        -> str:
    """INSERT {table}({keys}) VALUES(%s);
    or INSERT {table}({keys}) VALUES(%s) ON KEY DUPLICATE UPDATE {keys}=%s
    """
    keys, values = basic_parse(table, data)
    update_keys = ', '.join([f'{key} = %s' for key in keys.split(', ')])
    basic_sql = f'INSERT INTO {table}({keys}) VALUES({values})'
    return (basic_sql + f' ON DUPLICATE KEY UPDATE {update_keys};'
            if duplicate_key_update else basic_sql+';')
