from ..models import Tarefa


def cadastrar_tarefa(tarefa):
    Tarefa.objects.create(
        titulo=tarefa.titulo,
        descricao=tarefa.descricao,
        data_expiracao=tarefa.data_expiracao,
        prioridade=tarefa.prioridade,
        usuario=tarefa.usuario,
    )


def listar_tarefas(usuario):
    return Tarefa.objects.filter(usuario=usuario).all()


def buscar_tarefa_id(id):
    return Tarefa.objects.get(id=id)


def editar_tarefa(tarefa, tarefa_nova):
    tarefa.titulo = tarefa_nova.titulo
    tarefa.descricao = tarefa_nova.descricao
    tarefa.data_expiracao = tarefa_nova.data_expiracao
    tarefa.prioridade = tarefa_nova.prioridade

    tarefa.save(force_update=True)


def remover_tarefa(tarefa):
    tarefa.delete()
