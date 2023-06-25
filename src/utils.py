import psycopg2


def save_data_to_database(vacancies: list, database_name: str, params: dict) -> None:
    """Записываю данные в базу"""
    conn = psycopg2.connect(database=database_name, **params)
    with conn:
        with conn.cursor() as cur:
            for vacancy in vacancies:
                cur.execute('INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', (
                    vacancy['vacancy_id'],
                    vacancy['vacancy_name'],
                    vacancy['vacancy_city'],
                    vacancy['vacancy_url'],
                    vacancy['salary_from'],
                    vacancy['salary_to'],
                    vacancy['employer_name'],
                    vacancy['employer_id']
                ))
    conn.close()
