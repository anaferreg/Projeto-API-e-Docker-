from flask import Blueprint, jsonify
from controllers import AlunoController, ProfessorController, TurmaController

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return jsonify({"message":"API funcionando!"})

# Rotas dos Alunos
@bp.route('/alunos', methods=['GET'])
def get_all_aluno():                               # Pega todos os Alunos
    return AlunoController.get_all_aluno()

@bp.route('/alunos/<int:id>', methods=['GET'])
def get_aluno_id(id):                                 # Pega um aluno em específico pelo id
    return AlunoController.get_aluno_by_id(id)

@bp.route('/alunos', methods=['POST'])
def create_a_new_aluno():                           # Registra um novo aluno
    return AlunoController.create_aluno()

@bp.route('/alunos/<int:id>', methods=['PUT'])
def update_a_aluno(id):                           # Atualiza a informação do aluno
    return AlunoController.update_aluno(id)

@bp.route('/alunos/<int:id>', methods=['DELETE'])
def delete_a_aluno(id):                           # Deleta o registro do professor
    return AlunoController.delete_aluno(id)

# ----------------------------------------------------------------------------------------

# Rotas dos professores
@bp.route('/professores', methods=['GET'])
def get_all_professor():                               # Pega todos os professores
    return ProfessorController.get_all_professor()

@bp.route('/professores/<int:id>', methods=['GET'])
def get_professor_id(id):                                 # Pega um professor em específico pelo id
    return ProfessorController.get_professor_by_id(id)

@bp.route('/professores', methods=['POST'])
def create_a_new_professor():                           # Registra um novo professor
    return ProfessorController.create_professor()

@bp.route('/professores/<int:id>', methods=['PUT'])
def update_a_professor(id):                           # Atualiza a informação do professor
    return ProfessorController.update_professor(id)

@bp.route('/professores/<int:id>', methods=['DELETE'])
def delete_a_professor(id):                           # Deleta o registro do professor
    return ProfessorController.delete_professor(id)

# ----------------------------------------------------------------------------------------

# Rotas das turmas
@bp.route('/turmas', methods=['GET'])
def get_all_turma():                               # Pega todos as turmas
    return TurmaController.get_all_turma()

@bp.route('/turmas/<int:id>', methods=['GET'])
def get_turma_id(id):                                 # Pega uma turma em específico pelo id
    return TurmaController.get_turma_by_id(id)

@bp.route('/turmas', methods=['POST'])
def create_a_new_turma():                           # Registra uma nova turma
    return TurmaController.create_turma()

@bp.route('/turmas/<int:id>', methods=['PUT'])
def update_a_turma(id):                           # Atualiza a informação da turma
    return TurmaController.update_turma(id)

@bp.route('/turmas/<int:id>', methods=['DELETE'])
def delete_a_turma(id):                           # Deleta o registro da turma
    return TurmaController.delete_turma(id)