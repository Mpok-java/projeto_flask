from dao.db_config import get_connection

class MatriculaDAO:

    sqlSelect = 'SELECT id, aluno_id, curso_id, data_matricula FROM matricula'

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
        lista = cursor.fetchall()
        conn.close()
        return lista

    def salvar(self, id, aluno_id, curso_id, data_matricula):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            if id:
                cursor.execute('UPDATE matricula SET aluno_id = %s, curso_id = %s, data_matricula = %s WHERE id = %s', (aluno_id, curso_id, data_matricula, id))
            else:
                cursor.execute('INSERT INTO matricula (aluno_id, curso_id, data_matricula) VALUES (%s, %s, %s)', (aluno_id, curso_id, data_matricula))
            conn.commit()
            return {"status": "ok"}
        
        except Exception as e:
            return {"status": "erro", "mensagem":f"Erro {str(e)}"}
        finally:
            conn.close()

    def buscar_por_id(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id, aluno_id, curso_id, data_matricula FROM matricula WHERE id = %s', (id,))
        registro = cursor.fetchone()
        conn.close()
        return registro

    def remover(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('DELETE FROM matricula WHERE id = %s', (id,))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro {str(e)}"}
        finally:
            conn.close()