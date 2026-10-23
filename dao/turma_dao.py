from dao.db_config import get_connection

class TurmaDAO:

    sqlSelect = 'SELECT turma.id, semestre, nome_curso, nome FROM turma JOIN curso on curso_id=turma.curso_id JOIN professor on professor_id=turma.professor_id'

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
        lista = cursor.fetchall()
        conn.close()
        return lista

    def salvar(self, id, semestre, curso, professor):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO turma (semestre, curso_id, professor_id) VALUES (%s, %s, %s)', (semestre, curso, professor))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "erro", "mensagem":f"Erro {str(e)}"}
        finally:
            conn.close()